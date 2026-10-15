from django.shortcuts import render
from django.shortcuts import redirect
from managecash.forms import RegistrationForm,LoginForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)   
        if form.is_valid():
            password = form.cleaned_data.get('password1') 
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            return redirect('userlogin')
    else:
        form = RegistrationForm()               
    return render(request, 'register.html', {'form': form})
def User_Login(request):
    if request.method == "POST":
            form = LoginForm(request, data = request.POST)   
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(username = username,password=password)
                if user:
                    login(request,user)
                    return redirect('home')
    else:
            form = LoginForm()
    return render(request,'login.html',{'form':form})   
def user_logout(request):
    logout(request)
    return redirect('login')