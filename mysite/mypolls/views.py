# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import request
from .models import Question
from django.template import loader
from django.http import Http404

# Create your views here.


def index (request):
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    
    return HttpResponse (output)
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('mypolls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    
    
    
    

def detail (request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404 ("Question does not exist")
    
    return render(request, 'mypolls/detail.html', {'question':question})
    
    #return HttpResponse  ("You're looking at question: %s" % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


