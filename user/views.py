from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from home.models import UserProfile
from order.models import Order, OrderProduct
from product.models import Category, Comment
from user.forms import UserUpdateForm, ProfileUpdateForm


def index(request):
    category = Category.objects.all()
    current_user = request.user
    comments = Comment.objects.filter(user_id = current_user.id)
    profile =  UserProfile.objects.get(user_id=current_user.id)
    orders = Order.objects.filter(user_id=current_user.id)
    context = {'category': category,
               'profile': profile,
               'orders': orders,
               'comments': comments,

               }

    return render(request,'user_profile.html',context)


def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Bilgileriniz Güncellenmiştir ! ')
            return redirect('/user')
    else:

        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form =ProfileUpdateForm(instance=request.user.userprofile)
        current_user = request.user
        profile = UserProfile.objects.get(user_id=current_user.id)
        context = {'category': category,
                   'user_form': user_form,
                   'profile_form' : profile_form,
                   'profile':profile,

                   }

        return render(request,'user_update.html',context)




def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Şifreniz Güncellenmiştir ! ')
            return redirect('/user')

        else:
            messages.error(request,'Beklenmeyen Bir Hata Oluştu!'+str(form.errors))
            return HttpResponseRedirect('/user/password')


    else:

        category = Category.objects.all()
        form = PasswordChangeForm(request.user)

        return render(request,'change_password.html',{'form':form,'category':category})


def orders(request):
    category = Category.objects.all()
    current_user = request.user
    orders = Order.objects.filter(user_id=current_user.id)
    context = {'category': category,
               'orders': orders,


               }
    return render(request,'user_orders.html',context)


def orderdetail(request,id):
    category = Category.objects.all()
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id,id=id)
    orderitems = OrderProduct.objects.filter(order_id=id)
    context = {'category': category,
               'order': order,
               'orderitems': orderitems,

               }
    return render(request, 'user_order_detail.html', context)


def deletecomment(request,id):
    current_user = request.user
    Comment.objects.filter(user_id=current_user.id, id=id).delete()
    messages.success(request,'Yorum Başarıyla Silindi!')

    return HttpResponseRedirect('/user')