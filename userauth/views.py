from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .models import CustomUserModel
# Create your views here.


def test(request):
    return render(request,'test.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def home(request):

    return render(request,'index.html')

def register(request):
    page = 'register' 
    context  = {"page":page}
    if request.method == 'POST':
        
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        profile_picture = request.FILES.get('profile_picture')
        ac_type = request.POST.get('type')

        is_doctor = True if ac_type=='doctor' else False
        is_patient = not is_doctor
        
        if password != re_password:

            messages.error(request,"Password do not match! re-enter again")

            return render(request,'auth_form.html',context)

        try:
            
            user = CustomUserModel.objects.create(email=email,
                                                  first_name = fname,
                                                  last_name = lname,
                                                  city= city,
                                                  state = state,
                                                  zipcode = zipcode,
                                                  profile_picture = profile_picture,
                                                  is_doctor = is_doctor,
                                                  is_patient = is_patient
                                                  )    
            user.set_password(password)
            user.save()
            
            login(request,user)
            print(request.user.is_authenticated)

            messages.success(request,f"Successfully registered as {fname}")
            return render(request,'index.html')
            
        except Exception as e:
            messages.error(request,f"error Occured! {e}")
            
            return render(request,'auth_form.html',context)
        

    return render(request,'auth_form.html',context)


def login_user(request):
    page = 'login'
    context = {'page': page}

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Attempt to authenticate the user
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.first_name}!")
            return redirect('home')  # Redirect to dashboard or home page after login

        else:
            messages.error(request, 'Invalid email or password. Please try again.')

    return render(request, 'auth_form.html', context)