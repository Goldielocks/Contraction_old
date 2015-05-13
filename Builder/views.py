from Builder.models import Case, Citation
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from lxml.html.clean import clean_html
import lxml.html
import reversion


def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/Builder/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('login.html', {}, context)


@login_required
def home_page(request):
	caseList = Case.objects.all()

	if caseList.count == 0:
		return HttpResponse("SHIIIIT")
	
	return render_to_response("home.html", {"nodes":Case.objects.all()})

@login_required
def get_case(request):
		c = {}
		c.update(csrf(request))

		context = RequestContext(request)
		if request.method == 'GET':
			caseId = request.GET['caseId']
		
		if caseId:
			case = Case.objects.get(id=caseId)
			html = lxml.html.fromstring(case.value)
			response = ""
			if html.find('.//h1') is None:
				response = "<h1>" + case.name +"</h1>"
			
			response += case.value
			citList=""
			for citation in case.citations.all():
				citList += "<li><a class=\"get_case\" data-id=\"{0}\" href=\"#\">{1}</a></li>".format(citation.link, citation.name)

			return JsonResponse( {"value":response, "name":case.name, "citations":citList} )

@login_required
@reversion.create_revision()
def save_case(request):
	reversion.set_user(request.user)
	c = {}
	c.update(csrf(request))


	context = RequestContext(request)


	if request.method == 'GET':
		caseId = request.GET['caseId']
		caseData = request.GET['caseData']

		if caseId and caseData:
			html = lxml.html.fromstring(caseData)

			name = html.find('.//h1')
			
			case = Case.objects.get(id=caseId)
			if name is not None:
				case.name = name.text_content()

			case.value = clean_html(caseData)
			case.save()


	return JsonResponse({"result":"okay"})

@login_required
@reversion.create_revision()
def add_case(request):
	reversion.set_user(request.user)
	slave = request.GET["slave"]
	newCase = Case.objects.create()
	newCase.name = "Untitled" + str(newCase.id)
	newCase.value = "<h1>" + newCase.name +"</h1><p>TEXT HERE</p>"
	if slave == "True":
		newCase.slaveOnly = True
	newCase.save()
	header = "<li id=\"sideItem{0}\"><a class=\"get_case\" data-id=\"{0}\" href=\"#\">{1}</a></li>".format(str(newCase.id), newCase.name)
	
	return JsonResponse({"value":newCase.value, "id":newCase.id, "header":header}) 

@login_required
@reversion.create_revision()
def move_case(request):
	reversion.set_user(request.user)
	if request.method == 'GET':
		childId = request.GET['childId']
		parentId = request.GET['parentId']

		if childId is not None and parentId is not None:
			child = Case.objects.get(id=childId)
			parent = Case.objects.get(id=parentId)

			child.parent = parent
			child.save()

	return JsonResponse({"result":"okay"})

@login_required
@reversion.create_revision()
def link_case(request):
	reversion.set_user(request.user)

	if request.method == 'GET':
		slaveId = request.GET['primary']
		masterId = request.GET['citation']

		if slaveId is not None and masterId is not None:
			master = Case.objects.get(id=masterId)
			slave = Case.objects.get(id=slaveId)
			if master.slaveOnly is True:
				return JsonResponse({"result":"slave only"})

			#link = "/?caseId=" + slaveId
			link = masterId
			try:
				citation = Citation.objects.get(link = link)
			except Citation.DoesNotExist:
				citation = None


			if citation is None:
				citation = Citation.objects.create(link = link, name = master.name)

			citation.save()

			slave.citations.add(citation)
			slave.save()
			return JsonResponse({"result":"okay"})

	