from django.shortcuts import render
from .models import QuestionModel

# Create your views here.
def addquestion(request):
    ques = QuestionModel.objects.all()
    return render(request,'newquestion.html',{'question':ques})