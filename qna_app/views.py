from django.shortcuts import render,redirect
from .models import QuestionModel,CategoryModel
from django.http import HttpResponse
from django.views.generic import CreateView,ListView
from .forms import QuestionForm, AnswerModel#import form from forms.py
 
# Create your views here.

class QuestionModelCreateView(CreateView):
    model=QuestionModel
    fields = '__all__'

class QuestionModelListView(ListView):
    model=QuestionModel
    queryset = QuestionModel.objects.all()

def addquestion(request):

    if request.method == 'POST':
        form=QuestionForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                print(form)
                form.save() #saves data in database 
                return HttpResponse("your form is submitted")
            except:
                return HttpResponse("no data was stored")
        else:
            # print('error')
            # print(form, '00000000000000000000')
            return HttpResponse(form.errors)


    else:
        # form=QuestionForm
        category=CategoryModel.objects.all()
        return render(request,'questionmodel_create.html',{'category':category})


def update_question(request,id):
    question=QuestionModel.objects.get(id=id)
    if request.method == 'POST':
        form=QuestionForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save() #saves data in database 
                return redirect('qna:read')
            except:
                return HttpResponse("failure")
        else:
            return HttpResponse(form.errors)
    else:
        form=QuestionForm(instance=question)
        return render(request,'questionmodel_update.html',{'form':form})


def delete(request,id):
    question = QuestionModel.objects.get(id=id)
    question.delete()
    return redirect('qna:read')

def questions(request):
    quest = QuestionModel.objects.all()
    return render(request,'questionmodel_list.html',{'questions':quest})


def question_detail(request,id):
    question= QuestionModel.objects.get(id=id)
    #answer = AnswerModel.objects.get(id=id)

    dic={
        'question' : question,
        #'answer' : answer
    }
    return render(request,'details.html',dic)
    
