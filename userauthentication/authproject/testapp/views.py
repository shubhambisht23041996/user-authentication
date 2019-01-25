from django.shortcuts import render
from django.contrib.auth.decorators  import login_required
from testapp.forms import signupForm
from django.http import HttpResponseRedirect

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')


@login_required
def python_views(request):#this is the python exam view if
#you want to give a test first you signup and then login the page then you give the test
    return render(request,'testapp/pythonexam.html')


@login_required   #decorator
def django_view(request):
    return render(request,'testapp/djangoexam.html')



def signup_view(request):#this is the signup form where you signup
    form=signupForm()
    if request.method=='POST':
        form=signupForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})


@login_required #decorator
def apptitude_view(request):
    return render(request,'testapp/apptitude.html')
