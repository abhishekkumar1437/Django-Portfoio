from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid username or password')
            return redirect('signin')
    

    else:
        return render(request,'signin.html')



def signup(request):

    if request.method == 'POST':
        username=request.POST['username']
        first_name= request.POST['first_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username Taken')
                return redirect('signup')
           
            else:    
                user = User.objects.create_user(username=username,first_name=first_name,email=email,password=password1)
                user.save();
                messages.info(request,'User Created')
                return redirect('signin')
        else:        
            messages.error(request,'Password not matching')
            return redirect('signup')
        return redirect('/')

    else:
      return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')



def aboutus(request):
    return render(request,'aboutus.html')