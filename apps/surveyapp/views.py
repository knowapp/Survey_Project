from django.shortcuts import render, HttpResponse, redirect
from django import forms

#app = Flask(__name__)

def surveyapp(request):
    return render(request, 'surveyapp/surveyapp.html')

# def reset(request):
#     request.session['counter'] -=1   
#     return redirect('/')

def name(request):
    return render(request, 'surveyapp/result.html')

def result(request):
    try:
        request.session['counter'] += 1
    except KeyError:
        request.session['counter'] = 0
    request.session['name'] = request.POST['name']
    request.session['cities'] = request.POST['cities']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('/name')
