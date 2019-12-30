from django.shortcuts import get_object_or_404, render,redirect
from .models import Question, Choice 
from django.template import loader 
from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse

#Get que and display them 

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5] 
    
    return render(request,'polls/index.html',{'latest_question_list': latest_question_list })

#Show specific question and choices 

def detail(request,question_id):
    try:
        question=Question.objects.get(pk=question_id) 
    except Question.DoesNotExist:
        raise Http404("Question does not exist") 
    return render(request,'polls/detail.html',{'question': question }) 

#get question and display result 
def results(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    

    return render(request,'polls/results.html', { 'question' : question })

#Vote for a question choice 
def vote(request , question_id):
    #print(request.POST['choice']) 
    question=get_object_or_404(Question, pk=question_id) 
 
    try: 
        selected_choice=question.choice_set.get(pk=request.POST['choice'])  
    except(KeyError , Choice.DoesNotExist): 
        #Redisplay the question voting form 
        return render(request, 'polls/detail.html', 
        { 'question': question, 
        'error_message' : "You didn't select a choice."  
        })
     
    else:
        selected_choice.votes+=1 
        selected_choice.save()   
        return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))
        


    # try: 
    #     selected_choice=question.choice_set.get(pk=request.POST['choice'])  
    
    # except(KeyError , Choice.DoesNotExist): 
    #     #Redisplay the question voting form 
    #     return render(request, 'polls/detail.html', 
    #     { 'question': question, 
    #     'error_message' : "You didn't select a choice."  
    #     })