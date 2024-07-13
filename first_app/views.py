from django.shortcuts import render,redirect
from first_app import models
from django.contrib import messages
from django.contrib.auth import login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,authenticate,PasswordChangeForm,SetPasswordForm


from django.contrib.auth.decorators import login_required
# Create your views here.

def registrationForm(request):
    if request.method == 'POST':
        form = models.registerform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Account Created Successfully!.')
            return redirect("sign_up_page")
    else:
        form = models.registerform()
    return render(request,'register.html',{"form":form,'type':'sign up page'})
            
            
            
def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request.user , data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username , password = password)
            if user is not None:
                login(request,user)
                messages.success(request,'Successfull!')
                return redirect('Profile_page')
    else:
        form = AuthenticationForm(request=request.user)
        
    return render(request,'register.html',{"form":form})

@login_required
def profile_page(request):
    return render(request,'profile.html')

@login_required
def log_out(request):
    logout(request)
    messages.warning(request,'log out successfully!.')
    return redirect('log_in_page')


def change_pass(request):
    if request.user.is_authenticated:
        if request.user.is_authenticated:
            if request.method == 'POST':
                form = PasswordChangeFor(user=request.user , data = request.POST)
                if form.is_valid():
                    form.save()
                    update_session_auth_hash(request,form.user)
                    return redirect("Profile_page")
            else:
                form = PasswordChangeForm(user = request.user)
            return render(request,'pass.html',{'form':form})
        else:
            return redirect('log_in_page')
    else:
        return redirect('log_in_page')



def pass_change_2(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(user = request.user , data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,user = request.user)
                messages.success(request,"your password updated")
                return redirect('change_pass_2')
        else:
            form = SetPasswordForm(user = request.user)
        return render(request,'pass.html',{'form':form})
    else:
        return redirect('log_in_page')