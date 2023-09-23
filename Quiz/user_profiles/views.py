from django.shortcuts import render,redirect
from .forms import update_profile, update_user
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    if request.method == "POST":
        u_form = update_user(request.POST,instance=request.user)
        p_form = update_profile(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            print(p_form)
            p_form.save()
            return redirect ('profile')

    else :
        u_form = update_user(instance=request.user)
        p_form = update_profile(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'profile.html',context)
