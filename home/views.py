import json

from django.contrib.auth import logout, authenticate, login
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from home.forms import SearchForm, SignUpForm
from home.models import Setting, ContactFormMessage, ContactFormu
from django.contrib import messages

from product.models import Category, Cars, Images, Comment


def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    lastproducts = Cars.objects.all().order_by('?')[:4]
    comments = Comment.objects.filter(status='True').order_by('?')
    context = {'setting': setting,
               'category': category,
               'lastproducts': lastproducts,
               'comments': comments ,
               'page': 'home'}
    return render(request, 'index.html', context)


def hakkimizda(request):

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,'page':'hakkimizda','category': category}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,'page':'referanslar','category':category}
    return render(request, 'referanslarimiz.html', context)

def slider(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,'page':'slider'}
    return render(request, 'slider.html', context)

def iletisim(request):

    if request.method =='POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage() # Model ile bağlantı kur
            data.name = form.cleaned_data['name'] #Bilgileri al
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"Mesajiniz Gönderilmistir.")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactFormu()
    context = {'setting': setting,'form':form,'category':category}
    return render(request, 'iletisim.html', context)


def category_cars(request,id,slug):

    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    products = Cars.objects.filter(category_id=id)
    context = {'cars': products,
               'categorydata':categorydata,
               'category': category}
    return render(request,'arabalar.html',context)


def car_detail (request,id,slug):
    category = Category.objects.all()
    car = Cars.objects.get(pk=id)
    images = Images.objects.filter(car_id=id)
    comments = Comment.objects.filter(product_id=id,status='True')
    context = {'car': car,
               'images': images,
               'category': category,
               'comments': comments}
    return render(request,'car_detail.html',context)

def product_search(request):
    if request.method =='POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query'] #formdan bilgiyi al
            products = Cars.objects.filter(title__icontains=query) #arabalardan titleında query olanları al
            context = {'products':products,
                       'category':category,
                       'query':query
                       }
            return render(request,'products_search.html',context)

    return HttpResponseRedirect('/')

def product_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        product = Cars.objects.filter(title__icontains=q)
        results = []
        for rs in product:
            product_json = {}
            product_json = rs.title
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "KULLANICI ADI/ŞİFRE HATALI!")
            return HttpResponseRedirect('/login')


    category = Category.objects.all()
    context = {'category': category,
               }
    return render(request, 'login.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)

            return HttpResponseRedirect('/')



    form = SignUpForm()
    category = Category.objects.all()
    context = {'category': category,
               'form': form,
               }
    return render(request, 'signup.html', context)