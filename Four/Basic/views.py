from django.shortcuts import render

from Basic.forms import UserForm,UserProfileInfoForm

from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect,HttpResponse

from django.contrib.auth import authenticate,login,logout

from django.urls import reverse





# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    registration=False
    if request.method=="POST":
        print("Post")
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)
        if (user_form.is_valid() and profile_form.is_valid()):
             user=user_form.save()
             user.set_password(user.password)
             user.save()
             profile=profile_form.save(commit=False)
             profile.user=user
             if  'Image_Profile' in request.FILES:
                profile.Image_Profile=request.FILES['Image_Profile']
                profile.save()
             registration = True
        else:
                print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    return render(request,'regestration.html',
                                            {'profile_form':profile_form,
                                              'user_form':user_form,
                                             'regestration':registration})

def Relative(request):
    return render(request,'index.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))



@login_required
def special(request):
    return HttpResponse("You are logged in ,that was just the first step.Lets Begin")


def user_login(request):
    if request.method=="POST":
        print("Post")
        username=request.POST.get("Username")
        password=request.POST.get("Password")
        user=authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account is not Active")
        else:
            print("Someone logged in and failed")
            return HttpResponse("Wtf")
    else:
        return render(request,"login.html",{})
