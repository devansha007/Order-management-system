from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
  

@login_required(login_url="/loginpage/")
def recipie(request):

    if(request.method == "POST"):
        data=request.POST

        recipie_name=data.get('recipie_name')
        recipie_description=data.get('recipie_description')
        recipie_img=request.FILES.get('recipie_img')

        print(recipie_name)
        print(recipie_description)

        Recipie.objects.create(

            recipie_name=recipie_name,

            recipie_description=recipie_description,

            recipie_img = recipie_img,


        )

        return redirect('/')


    quareyset=Recipie.objects.all()
    
    if request.GET.get('search'):

        print(request.GET.get('search')) 
        
        quareyset = quareyset.filter(recipie_name__icontains = request.GET.get('search') )




    context={'recep': quareyset}
    return render(request,"index.html",context)



def delete_recip(request, id):
    print(id)
    quarey=Recipie.objects.get(id = id)
    quarey.delete()
    return redirect('/')
    


def update_recip(request , id):
    quarey=Recipie.objects.get(id = id)

    if request.method == "POST":
         
         data=request.POST

         recipie_name =data.get('recipie_name') 
         recipie_description = data.get('recipie_description')
         recipie_img=request.FILES.get('recipie_img')


         quarey.recipie_name =recipie_name
         quarey.recipie_description =recipie_description

         if recipie_img:
             quarey.recipie_img =recipie_img
         
         
         
         quarey.save()

         return redirect('/')

    context={'recipe' : quarey}
    return render(request,"update.html",context)

# 
# 
# Authenticaton part starts
# 
# 

def login_page(request):

    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        if not User.objects.filter(username = username).exists():
            messages.error(request, "incorrect username")
            print("hi")
            return redirect('/loginpage')
    
        user = authenticate(username = username , password = password)
  

        if user is None :
            messages.error(request, "incorrect passwod")
            return redirect('/loginpage')

        else:
            login(request,user)
            return redirect('/')
  
    
    return render(request,"login.html")



def logout_page(request):
    logout(request)
    return redirect('/loginpage')


def register(request):
    
    if request.method == "POST" :
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=User.objects.filter(username = username)

        if(user.exists()):
            messages.error(request, "user already exists")
            return redirect('/register')


        user = User.objects.create(

                    first_name = first_name,
                    last_name  = last_name,
                    username =username,
                    
        )
        user.set_password(password)
        user.save()
        messages.info(request, "your account is  created.")
        return redirect('/register')



    return render(request,"register.html")

