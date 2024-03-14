from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import *

from .forms import userregistration,auth_form,product_form
from django.contrib.auth.decorators import login_required

import razorpay
from cloth_project.settings import *





def hello(request):
    cat=category.objects.all()
    prod=products.objects.all()[2:10:2]
    prod2=products.objects.all()[10:14]
    
    rate=product_rating.objects.all()

  
    
    
   
    context={'cat':cat,'prod':prod,'prod2':prod2}


    return render(request,'home.html',context)





def register_user(request):

    if request.method=='POST':
        fm=userregistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Data Save Succesfully')
        else:
            messages.error(request,'Error')
        
         
            
    else:
        fm=userregistration()
    

    return render(request,'register.html',{'form':fm})





def login_info(request):

    if request.method=='POST':
        uname=request.POST['username']
        upasss=request.POST['password']

        user=authenticate(request,username=uname,password=upasss)

        if user is not None:
            login(request,user)
            messages.success(request,'Login Succesfully')
            return redirect('home')
        else:
            messages.error(request,'Somethong Went Wrong ')
    






    fm=auth_form()
    return render(request,'login.html',{'form':fm})



def log_out(request):
    logout(request)
    messages.success(request,'Log out Succesfully')
    return redirect('home')




def data2(request,id):
   
    data=products.objects.filter(cat=id)
    cat=category.objects.all()
    
    for i in data:
        d1=i.cat.name
  

    context={'cat':cat,'prod':data,'d1':d1}


    return render(request,'view_products.html',context)



def search(request):
    if request.method=='POST':
        value=request.POST['inp1']
        prod=products.objects.filter(name__contains=value)

        d1='PRODUCTS'
    
        cat=category.objects.all()

        context={'cat':cat,'prod':prod,'d1':d1}
    

        return render(request,'view_products.html',context)



def about(request):

    return render(request,'about.html')



def delete_product(request,id):
    prod=products.objects.get(id=id)
    prod.delete()
    return redirect('home')

# -------------------------------------------------------------------------------------------------------
    


def show_info(request,id):
    prod=products.objects.filter(id=id)

    prod2=products.objects.all()[0::2]


    rate_list=[]
    rate1=product_rating.objects.all()



    review_list=[]
    reviews=product_rating.objects.all()

    for i in reviews:
        if i.product.id==id:
            review_list.append([i.user,i.rating,i.info])


    for i in rate1:
        if id == i.product.id:
            rate_list.append(i.rating)
            avrage=sum(rate_list)/len(rate_list)
    else:
        avrage=0


    
   

    context={'prod':prod,'rate':avrage,'prod2':prod2,'review':review_list}


    return render(request,'prod_info.html',context)



# ==========================================================================================================


# cart views


@login_required
def store_cart(request,id):
    prod=products.objects.get(id=id)
    # cat=cart.objects.all()

    cart_item, item_created = cart.objects.get_or_create(user=request.user, product=prod)
    
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('home')
  
   

@login_required
def show_cart(request):
    
    cart_info=cart.objects.filter(user=request.user)
    total=0+1
    quantity=0
    for i in cart_info:
        subtotal=i.quantity*i.product.prize
        total=total+subtotal
        quantity=quantity+i.quantity
        p_id=i.product.id





    return render(request,'cart.html',{'cart_info':cart_info,'total':total,'cart_value':quantity})





def increase_cart(request,id):
    prod=products.objects.get(id=id)
    cart_item, item_created = cart.objects.get_or_create(user=request.user, product=prod)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('show_cart')

def decrease_cart(request,id):
    prod=products.objects.get(id=id)
    cart_item, item_created = cart.objects.get_or_create(user=request.user, product=prod)
    cart_item.quantity -= 1
    cart_item.save()

    cart_data=cart.objects.filter(quantity=0)
    cart_data.delete()
    
    return redirect('show_cart')


    


def delete_cart(request,id):
    cart_items=cart.objects.get(id=id)
    cart_items.delete()
    return redirect('show_cart')
    


# -------------------------------ADMIN-------------------------------------------------

def add_product(request):
    
    if request.method=='POST':
        fm=product_form(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Data Save Succesfully')
        else:
            messages.error(request,'Error')   
            
    else:
        fm=product_form()

    return render(request,'add_products.html',{'form':fm})
    








# =========================================================================

def rating(request,id):
    prod=products.objects.get(id=id)
    if request.method=="POST":
        rating=request.POST['stars']
        info=request.POST['info']

       

        obj=product_rating.objects.create(user=request.user,product=prod,info=info,rating=rating)
        obj.save()
        return redirect('home')
            
        
    return render(request,'prod_info.html',)







def checkout(request):

    cart_info=cart.objects.filter(user=request.user)
    total=0+1
    quantity=0
    for i in cart_info:
        subtotal=i.quantity*i.product.prize
        total=total+subtotal
        quantity=quantity+i.quantity
        p_id=i.product


    if request.method=='POST':
        F_name=request.POST['name']
        m_number=request.POST['number']
        email_adress=request.POST['email']
        Address=request.POST['address']

        orders_d=orders_data.objects.create(user=request.user,product=p_id,quntity= quantity,Address=Address,total_amount=total,fname=F_name,mobile_no=m_number,email=email_adress)
        orders_d.save()

        cart_info=cart.objects.filter(user=request.user)
        cart_info.delete()
    


    context={'api_key':RAZORPAY_KEY,'total':total}

    return render(request,'checkout.html',context)



def buy(request,id):
    prod=products.objects.get(id=id)


    p_id=prod.id
    total=prod.prize




    
    if request.method=='POST':
        F_name=request.POST['name']
        m_number=request.POST['number']
        email_adress=request.POST['email']
        Address=request.POST['address']


        
        orders_d=orders_data.objects.create(user=request.user,product=prod,quntity= 1,Address=Address,total_amount=total,fname=F_name,mobile_no=m_number,email=email_adress)
        orders_d.save()

      


    context={'api_key':RAZORPAY_KEY,'total':total}

    return render(request,'checkout.html',context)









def order(request):

    order=orders_data.objects.filter(user=request.user)
    return render(request,'orders.html',{'order':order})


def del_order(request,id):
    orders=orders_data.objects.get(id=id)
    orders.delete()
    return redirect('orders')













































# =====================================================cookies=============================================================


def setcookie(request):
    response=render(request,'setcookie.html')
    response.set_cookie('name','Gaurav')
    return response


def getcookie(request):
    name=request.COOKIES['name']
    return render(request,'getcookie.html',{'name':name})