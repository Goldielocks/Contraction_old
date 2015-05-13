from Builder.models import Agreement, Node, Category, Clause, ClauseProbability
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
                return HttpResponseRedirect('')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('login.html', {}, context)


@login_required
def home_page(request):
	#caseList = Case.objects.all()

	#if caseList.count == 0:
	#	return HttpResponse("SHIIIIT")
	
	return render_to_response("home.html", {"nodes":Node.objects.all()})