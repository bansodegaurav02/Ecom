"""Ecom_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecom_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.hello,name='home'),
    path('register/',views.register_user,name='register'),
    path('login/',views.login_info,name='login'),
    path('logout/',views.log_out,name='log_out'),
    path('cat/<int:id>/',views.data2,name='cat'),
    path('search/',views.search,name='search'),
    path('show/<int:id>',views.show_info,name='show'),
    path('about/',views.about,name='about'),
    path('delete_product/<int:id>',views.delete_product,name='delete_product'),
    



    # -----------------cart------------------------
    path('cart2/',views.show_cart,name='show_cart'),
    path('add_cart/<int:id>',views.store_cart,name='addcart'),
    path('increase_cart/<int:id>',views.increase_cart,name='increase_cart'),
    path('decrease_cart/<int:id>',views.decrease_cart,name='decrease_cart'),
    path('delete_cart/<int:id>',views.delete_cart,name='delete_cart'),
    path('checkout/',views.checkout,name='ch'),
    path('buy/<id>',views.buy,name='buy'),

    path('orders/',views.order,name='orders'),
    path('delete_orders/<id>',views.del_order,name='del_order'),  





    # ------------------ADMIN--------------------------------------------

    path('add_product/',views.add_product,name='add_product'),



    # ---------------------------------------------
    

    path('cookie/',views.setcookie),
    path('getcookie/',views.getcookie),


    # ==============================

    path('add_rating/<int:id>',views.rating,name='add_rating'),

    

]
