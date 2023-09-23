from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Historyquiz,Geographyquiz,Astronomyquiz
from django.forms import modelform_factory
from crispy_forms.layout import Layout,Submit
from crispy_forms.helper import FormHelper
from django.contrib.auth.decorators import login_required

def intro(request):
    return render(request,"intro.html")

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        user = authenticate(username=username,password=password)
        if user is not None :
            if user.check_password : 
                login(request,user)
                return redirect ('category')
            else : 
                messages.warning(request,"Your password is wrong")
                return redirect('log-in')
        else : 
            messages.warning(request,"You don't have an account with the given information!")
            return redirect('log-in')
    else :
        return render(request,"log_in.html")

def sign_up(request):
    if request.method == 'POST':
        new_user = request.POST.get('new_user')
        first_name = request.POST.get('f_name')
        last_name = request.POST.get('l_name')
        mail = request.POST.get('mail')
        pass1 = request.POST.get('pw1')
        pass2 = request.POST.get('pw2')
        if pass1 == pass2:
            auth = User.objects.create_superuser(new_user,mail,pass1)
            auth.first_name = first_name
            auth.last_name = last_name
            auth.save()
            messages.success(request,'You account has successfully created')
            return redirect('log-in')
    else : 
        return render(request,"sign_up.html")

class HistoryListView(LoginRequiredMixin,ListView):
    model=Historyquiz
    template_name="history.html"
    context_object_name='Historyquizes'
    ordering='pk'
    paginate_by=1
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)     #to get necessary data from parent class and to update our context dict
        total_quizes = self.model.objects.count()        #we use self.models instead of model name, so that it is more flexible
        context['total_quizes']=total_quizes
        return context

def history_finished(request):
    return render(request,'history.html')

class GeographyListView(LoginRequiredMixin,ListView):
    model=Geographyquiz
    template_name="geography.html"
    context_object_name='Geographyquizes'
    ordering='pk'
    paginate_by=1
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)     #to get necessary data from parent class and to update our context dict
        total_quizes = self.model.objects.count()        #we use self.models instead of model name, so that it is more flexible
        context['total_quizes']=total_quizes
        return context

def geography_finished(request):
    return render(request,'geography.html')

class AstronomyListView(LoginRequiredMixin,ListView):
    model=Astronomyquiz
    template_name="astronomy.html"
    context_object_name='Astronomyquizes'
    ordering='pk'
    paginate_by=1
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)     #to get necessary data from parent class and to update our context dict
        total_quizes = self.model.objects.count()        #we use self.models instead of model name, so that it is more flexible
        context['total_quizes']=total_quizes
        return context

def astronomy_finished(request):
    return render(request,'astronomy.html')

class HistoryCreateView(LoginRequiredMixin,CreateView):
    model = Historyquiz
    fields= ['question','ans_A','ans_B','ans_C','ans_D',"correct_ans"]
    success_url = '/history_quiz/intro/'
    def form_valid(self,form):
        form.instance.author = self.request.user
        messages.success(self.request,"You have successuflly added quiz to History Quiz!")
        return super().form_valid(form)
    
class GeographyCreateView(LoginRequiredMixin,CreateView):
    model = Geographyquiz
    fields= ['question','ans_A','ans_B','ans_C','ans_D',"correct_ans"]
    success_url = '/geography_quiz/intro/'
    def form_valid(self,form):
        form.instance.author = self.request.user
        messages.success(self.request,"You have successuflly added quiz to Geography Quiz!")
        return super().form_valid(form)
    
class AstronomyCreateView(LoginRequiredMixin,CreateView):
    model = Astronomyquiz
    fields= ['question','ans_A','ans_B','ans_C','ans_D',"correct_ans"]
    success_url = '/astronomy_quiz/intro/'
    def form_valid(self,form):
        form.instance.author = self.request.user
        messages.success(self.request,"You have successuflly added quiz to Astronomy Quiz!")
        return super().form_valid(form)
    
@login_required
def category(request):
    return render(request,'category.html')

def history_intro(request):
    quiz_type = "history"
    quiz_count = Historyquiz.objects.all().count()
    context = {
        "quiz_type" : quiz_type,
        "quiz_count" : quiz_count
    }
    return render(request,"quiz_intro.html",context)

def geography_intro(request):
    quiz_type = "geography"
    quiz_count = Geographyquiz.objects.all().count()
    context = {
        "quiz_type" : quiz_type,
        "quiz_count" : quiz_count
    }
    return render(request,"quiz_intro.html",context)

def astronomy_intro(request):
    quiz_type = "astronomy"
    quiz_count = Astronomyquiz.objects.all().count()
    context = {
        "quiz_type" : quiz_type,
        "quiz_count" : quiz_count
    }
    return render(request,"quiz_intro.html",context)
