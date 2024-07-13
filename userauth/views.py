from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .models import CustomUserModel


from django.contrib.auth.decorators import login_required
from .models import BlogPost, Category
from .forms import BlogPostForm

# Create your views here.


def test(request):
    return render(request,'test.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def home(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request,'index.html',context)

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



@login_required
def create_blog_post(request):
    if request.user.is_doctor:
        if request.method == 'POST':
            form = BlogPostForm(request.POST, request.FILES)
            if form.is_valid():
                blog_post = form.save(commit=False)
                blog_post.author = request.user
                blog_post.save()
                return redirect('my_blog_posts')
        else:
            form = BlogPostForm()
        return render(request, 'create_blog_post.html', {'form': form})
    else:
        return redirect('home')

@login_required
def my_blog_posts(request):
    if request.user.is_doctor:
        blog_posts = BlogPost.objects.filter(author=request.user)
        return render(request, 'my_blog_posts.html', {'blog_posts': blog_posts})
    else:
        return redirect('home')

def blog_posts_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    blog_posts = BlogPost.objects.filter(category=category, is_draft=False)
    return render(request, 'blog_posts_by_category.html', {'category': category, 'blog_posts': blog_posts})


def blog_post_list(request):
    categories = Category.objects.all()
    return render(request, 'blog_post_list.html', {'categories': categories})