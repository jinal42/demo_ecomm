"""ecomm URL Configuration

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

from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path
from ecommerce import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('reg/',views.user_profile,name='user_reg'),

    # path('login/',views.login,name='login'),                           user_profile
    path('login/',views.login_view,name='login_view'),
    


    path('shop/',views.shop,name='shop'),
    path('blog/',views.blog,name='blog'),
    path('cart/',views.cart,name='cart'),
    path('home/',views.home ,name='index'),
    path('contact/',views.contact,name='contact'),
    path('category/',views.category,name='categoryy'),

    path('prod_details/',views.prod_details,name='prod_details'),
    path('blog_single/',views.blog_single,name='blog_single'),

    path('demo/',views.demo_view,name='demo'),
    path('show_category/',views.show_view,name='show_category'),
    path('search/',views.search,name='search'),

    path('get_category/', views.home,name='get_my_category'),  
    # path('get_category/', views.get_my_category,name='get_my_category'),    
  
    path('get_category_id/<int:id>', views.get_my_category_id,name='get_my_category_id'),  
    path('show/',views.show,name='show'),

    path('add_cart/<int:id>',views.add_cart,name='add_cart'),
    path('add_to_cart/<int:id>',views.add_to_cart,name='add_to_cart'),



]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
