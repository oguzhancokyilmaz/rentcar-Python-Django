from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.utils.crypto import get_random_string

from home.models import UserProfile
from order.models import ShopCartForm, ShopCart, OrderForm, Order, OrderProduct
from product.models import Category, Cars


def index(request):
    return HttpResponse('order app')

@login_required(login_url='/login')
def addtocart(request,id):
    url = request.META.get('HTTP_REFERER')  # get last url
    if request.method == 'POST': # form post edildiyse
        form = ShopCartForm(request.POST)
        if form.is_valid():
            current_user = request.user

            data = ShopCart() # model ile bağlantı kur
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = form.cleaned_data['quantity']
            data.save()

            request.session['cart_items']= ShopCart.objects.filter(user_id=current_user.id).count()
            messages.success(request,"Ürün başarı ile sepetinize eklenmiştir.Teşekkür Ederiz.")

            return  HttpResponseRedirect(url)
    messages.warning(request, "Ürün sepete eklenemedi.")
    return  HttpResponseRedirect(url)

def shopcart(request):
    category = Category.objects.all()
    current_user = request.user
    schopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()

    for rs in schopcart:
        total += rs.product.price * rs.quantity

    context = {
        'schopcart': schopcart,
        'category': category,
        'total': total,


    }

    return  render (request,'Shopcart_products.html',context)

@login_required(login_url='/login')
def deletefromcart(request,id):
    ShopCart.objects.filter(id=id).delete()
    current_user = request.user
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
    messages.success(request,"Ürün Sepetten Silinmiştir.")
    return HttpResponseRedirect("/shopcart")

@login_required(login_url='/login')
def orderproduct(request):
    category = Category.objects.all()
    current_user = request.user
    schopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0

    for rs in schopcart:
        total += rs.product.price * rs.quantity


    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.user_id=current_user.id
            data.total = total
            data.ip=request.META.get('REMOTE_ADDR')
            ordercode= get_random_string(5).upper()
            data.code = ordercode
            data.save()


            schopcart= ShopCart.objects.filter(user_id=current_user.id)
            for rs in schopcart:
                detail = OrderProduct()
                detail.order_id = data.id
                detail.product_id = rs.product_id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity

                detail.price = rs.product.price
                detail.amount =rs.amount
                detail.save()

                product = Cars.objects.get(id=rs.product_id)
                product.amount -= rs.quantity
                product.save()

            ShopCart.objects.filter(user_id=current_user.id).delete()
            request.session['cart_items']=0
            messages.success(request,"SİPARİŞİNİZ ALINMIŞTIR.TEŞEKKÜR EDERİZ")
            return render(request,'Order_Completed.html',{'ordercode':ordercode,'category':category})

        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect("/order/orderproduct")

    form = OrderForm
    profile = UserProfile.objects.get(user_id=current_user.id)

    context = {
        'schopcart': schopcart,
        'category': category,
        'total': total,
        'form': form,
        'profile':profile

    }

    return  render (request,'Order_Form.html',context)