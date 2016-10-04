from Builder.models import Contract, Node, Category, Clause, ClauseProbability
from docx import Document
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators import csrf
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from lxml.html.clean import clean_html
import lxml.html
import reversion
import os.path

def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/", {}, context)
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('login.html', {}, context)



def home_page(request):
	return render_to_response("home.html", {"nodes":Node.objects.all()})


@login_required
def build(request):
	
	return render_to_response("build.html", {"nodes":Node.objects.all()})


@login_required
def collaborate(request):
	return render_to_response("home.html", {"nodes":Node.objects.all()})


@login_required
def publish(request):
	return render_to_response("home.html", {"nodes":Node.objects.all()})