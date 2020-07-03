from django.shortcuts import render
from .forms import profile_form,userform,diary_form,update_form
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import user_profile,diary
from django.contrib.auth.models import User

#login includes
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required#decorator whic we can use in any view that requires login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

# Create your views here.
                
#dasboard cbv 
class dashboard(DetailView):
    model=User
    template_name='user_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['text'] = diary.objects.get(user_profile_id=self.kwargs['pk'])
        context['diary'] = diary.objects.filter(user_profile_id=self.kwargs['pk']).order_by('-creation_date')[:3]
        return context
# class user_login(LoginView):
#     template_name='LoginView_form.html'

def index(request):
    
    return render(request,'index.html')

#signup view
def signup(request):
    registered=False
    if request.method=="POST":
        user_info=userform(data=request.POST)
        user_profile_form=profile_form(data=request.POST)
        if user_profile_form.is_valid() and user_info.is_valid():
            user=user_info.save()
            user.set_password(user.password)
            user.save()
            profile=user_profile_form.save(commit=False)
            profile.user=user
            
            if 'profile_pic' in request.FILES:
                print("image saved")
                profile.profile_pic=request.FILES['profile_pic']
            
            profile.save()
            registered=True
        else:
            print(user_profile_form.errors,user_info.errors)
    else:
        user_info=userform()
        user_profile_form=profile_form()            
    
    return render(request,'signup.html',{'user_form':user_info,'profile_form':user_profile_form,'registered':registered})         

# #login view
def user_login(request):
    if request.method=='POST':
     
        #print(p)
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                #p=user_profile.objects.get(user.pk)
                #print(p)
                # user_id=user.pk
                # u=user_profile.objects.get(user.id)
                # print(u)
                return redirect('dashboard',pk=user.pk)
            else:
                return HttpResponse('Account is not Active')
        else:
            error="*invalid username or password"
            return render(request,'LoginView_form.html',{'error':error}) #HttpResponse("Invalid Username or Password")    
    else:
        return render(request,'LoginView_form.html')  
    
#logout view
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))      

#crete view for diary entries
# class create_diary_view(LoginRequiredMixin,CreateView):
#     login_url='/login/'
#     redirect_field_name='journal/user_profile.html'
#     form_class=diary_form
    
#     model=diary   


from django.shortcuts import get_object_or_404
@login_required
def create_diary_view(request,pk):
    if request.method=="POST":
        diary_data=diary_form(data=request.POST)
        if diary_data.is_valid():
            diary=diary_data.save(commit=False)
            diary.user_profile=get_object_or_404(User,pk=pk)
            diary.save()
            return redirect('dashboard',pk=pk)
            
    return render(request,'diary_form.html',{'diary_form':diary_form})   

    
class diary_list(LoginRequiredMixin,ListView):
    login_url='/login/'
    model=diary
    
    def get_queryset(self):
        user = self.request.user
        return diary.objects.filter(user_profile=user)
       
class diary_detail(LoginRequiredMixin,DetailView):
    model=diary

class diary_update(LoginRequiredMixin,UpdateView):     
    model=diary
    
    #redirect_field_name=None
    fields=['text']
    success_url='/diary/update/success'
    # form_class=update_form
  
    template_name='update_diary.html'      

@login_required          
def update_success(request):
 
    return render(request,'update_success.html')  

class diary_delete(LoginRequiredMixin,DeleteView):
    model=diary
    success_url=reverse_lazy('update_success')        
         
         
def search(request):
    
    
    
    #text=diary.objects.get( user_profile_id=request.GET.get('pk'))
    text=diary.objects.filter(creation_date__contains=request.GET.get('search'))
        
    # diarypk=User.diary.pk
    return render(request,'search.html',{'text':text})  
    # try: 
    #     text=diary.objects.get(creation_date__contains=request.GET.get('search'))
        
    
    #     return render(request,'search.html',{'text':text.text})         
    # except:
    #     text='no data'
    #     print(request.GET.get('search'))
    #     print(diary.objects.all())
    #     return render(request,'search.html',{'text':text})