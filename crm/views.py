from django.shortcuts import render,redirect
from django.views.generic import View

from crm.forms import EmployeeModelForm,RegistrationForm,LoginForm
from crm.models import Employee

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator


def signin_required(fn):
    def wrapper(request,*args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"Invalid Session")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

# @signin_required  #decorater         
# Create your views here.
@method_decorator(signin_required,name="dispatch")
class EmployeeCreateView(View):
    def get(self,request,*args,**kwargs):
        form=EmployeeModelForm()
        return render(request,"emp_add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=EmployeeModelForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Employee has been created")
            # Employee.objects.create(**form.cleaned_data)
            print("created")        
            return render(request,"emp_add.html",{"form":form}) 
        else:
            messages.error(request,"Failed to create employee")
            return render(request,"emp_add.html",{"form":form}) 

@method_decorator(signin_required,name="dispatch")        
class EmployeeListView(View):
    def get(self,request,*args, **kwargs):
        qs=Employee.objects.all()
        department=Employee.objects.all().values_list("department",flat=True).distinct()
        print(department)
        if "department" in request.GET:
            dept=request.GET.get("department")
            qs=qs.filter(department__iexact=dept)
        return render(request,"emp_list.html",{"data":qs,"department":department}) 
    
    def post(self,request,*args, **kwargs):
        name=request.POST.get("box")
        qs=Employee.objects.filter(name__icontains=name)
        return render(request,"emp_list.html",{"data":qs}) 

@method_decorator(signin_required,name="dispatch")    
class EmployeeDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employee.objects.get(id=id) 
        return render(request,"emp_detail.html",{"data":qs}) 

@method_decorator(signin_required,name="dispatch")    
class EmployeeDeleteView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        Employee.objects.get(id=id).delete()
        messages.success(request,"Employee removed")
        return redirect("emp-all")      

@method_decorator(signin_required,name="dispatch")    
class EmployeeUpdateView(View):
    
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Employee.objects.get(id=id)
        form=EmployeeModelForm(instance=obj)
        return render(request,"emp_edit.html",{"form":form})
    
    def post(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        obj=Employee.objects.get(id=id)
        form=EmployeeModelForm(request.POST,instance=obj,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Employee updated")
            return redirect("emp-detail",pk=id)
        else:
            messages.error(request,"Updation Failed")
            return render(request,"emp_edit.html",{"form":form})       
#signup/

class SignUpView(View):
    def get(self,request,*args, **kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
                
    def post(self,request,*args, **kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"registration successful")
            return render(request,"register.html",{"form":form})
        else:
            messages.error(request,"Failed ")
            return render(request,"register.html",{"form":form})
        
class SignInview(View):
    def get(self,request,*args, **kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args, **kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            usr_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            print(usr_name,pwd)
            user_obj=authenticate(request,username=usr_name,password=pwd)
            # print(usr_name,pwd) # aswan aswan09
            if user_obj:
                print("valid")
                login(request,user_obj)
                return redirect("emp-all")
            

            messages.error(request,"invalid")
            return render(request,"login.html",{"form":form})

  
@method_decorator(signin_required,name="dispatch")          
class SignOutView(View):
    def get(self,request,*args, **kwargs):
        logout(request)  
        return redirect("signin")          
    
     
