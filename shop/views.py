from django.shortcuts import render,HttpResponse,redirect

from .models import Product, Category

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from django import forms

from .forms import SignUpForm,UpdateUserForm

def home(request):

    all_products=Product.objects.all()

    return render(request,'index.html',{'products':all_products})

def about(request):

    return render(request,'about.html')

def login_user(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'با موفقیت وارد شدید')
            return redirect('home')
        else:
            messages.error(request,'نام کاربری و یا رمز عبور نادرست است')
            return redirect('login')

    else:

        return render(request, 'login.html')
def logout_user(request):

    logout(request)

    messages.success(request,("با موفقیت خارج شدید"))

    return redirect("home")

def signup_user(request):

    form = SignUpForm()

    if request.method == 'POST':

        form = SignUpForm(request.POST)

        if form.is_valid():

            form.save()

            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            messages.success(request,('ثبت نام شما با موفقیت انجام شد'))
            return redirect('home')

        else:
            messages.error(request, ('ثبت نام شما انجام نشد'))
            # messages.error(request, form.errors)     نمایش خطاهادر ثبت نام
            return redirect('signup')

    else:
        return render(request,'signup.html', {'form':form})

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form=UpdateUserForm(request.POST or None ,instance=current_user)

        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request,'پروفایل شما ویرایش شد ')
            return redirect('home')
        return render(request,'update_user.html',{'user_form':user_form})

    else:
        messages.error(request,'لاگین کنید')
        return  redirect('login')


def product(request,pk):

    product=Product.objects.get(id=pk)

    return render(request,'product.html',{'product':product})

def category(request , cat):

    cat = cat.replace("-"," ")

    # try:
    category = Category.objects.get(name=cat)
    products = Product.objects.filter(category=category)
    return render(request,'category.html',{'products': products, 'category': category})
    # except:
    #     messages.error(request,'(دسته بندی مورد نظر وجود ندارد)')
    #     return redirect('home')

def category_summary(request):

    all_cat = Category.objects.all()

    return render(request,'category_summary.html',{'category': all_cat})


