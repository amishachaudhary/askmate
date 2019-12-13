from django.shortcuts import render,redirect
from .models import UserModel
from django.http import HttpResponse
# Create your views here.

def userauth(request):
    if request.method == 'POST':
        e=request.POST.get('email')
        p = request.POST.get('pass')
        user = UserModel.objects.filter(email=e,password=p)
        if(user.count()>0):
            for user in user:
                request.session['email']=user.email #invokes session
                request.session['id']=user.id
                request.session['name']=user.name
                return redirect('qna:read')
        else:
            return HttpResponse("wrong credentials")
    else:
        return render(request, 'login.html')


def logoutauth(request):
    request.session.flush()
    return redirect('user:login')

def test(request):
    return render(request, 'test.html')