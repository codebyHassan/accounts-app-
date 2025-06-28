from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.views import View
from .models import Catagery, Subcatagery
from django.contrib.auth.decorators import login_required
from django.db.models import Sum 
from .forms import SignUpForm
from django.contrib import messages

class register(View):
  def get(self ,request):
      form = SignUpForm()
      return render(request, 'register.html',{'form':form})
  
  def post(self , request):
      form = SignUpForm(request.POST)
      if form.is_valid():
          messages.success(request, 'Account Regitser Sucessfully ')
          form.save()
      return render(request, 'register.html',{'form':form})





def delete_catagery(request , pk):
    sub = Catagery.objects.get(id=pk)
    sub.delete()
    return redirect('/')

    
def delete_sub_catagery(request , pk):
    sub = Subcatagery.objects.get(id=pk)
    sub.delete()
    return redirect('/')

    

def subcatagery_add(request, foo): 
    if request.method == 'POST':
        addname = request.POST['addname']
        addamount = request.POST['addamount']
    
        cats = Catagery.objects.get(user=request.user, title=foo)
        subs = Subcatagery.objects.create(user=request.user,catagery=cats ,name=addname ,amount=addamount)
        subs.save() 
        return redirect('/')
    
    return render(request, 'subcatagery-add.html',)     
        

def catageryview(request, foo):
       
    cat = Catagery.objects.get( title=foo)
    sub = Subcatagery.objects.filter( catagery=cat)
    res = sub.aggregate(Sum('amount'))

    
   
    return render(request, 'catageryview.html',{  'cat':cat , 'sub':sub, 'res':res})


@login_required(login_url='login')
def home(request):   
    
    total = Subcatagery.objects.filter(user=request.user).aggregate(Sum('amount'))
 
    data = Catagery.objects.filter(user=request.user)
    if request.method == 'POST':
        title =  request.POST['title']
        
        query = Catagery.objects.create(user=request.user, title=title)
        query.save()
        
    return render(request, 'home.html', {'data':data, 'total':total})

def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, 'invalid username or password')
            return redirect('login')
               

    return render(request, 'login.html')    

def logout_user(request):
    logout(request)
    return redirect('/')
