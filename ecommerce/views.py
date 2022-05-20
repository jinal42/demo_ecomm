from django.shortcuts import render
from .forms import User1Form, UserForm
from .models import Add_Cart, Category, Item, MyCategory, MyItem, User1, UserReg
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.hashers import make_password

# from .models import UserProfile
# from .forms import User1Form, UserForm,ProfileForm

from .forms import UserForm,ProfileForm




# Create your views here.


def home(request):

      all_post=MyItem.objects.all().order_by('id')
      # print("🚀 ~ file: views.py ~ line 84 ~ all_post", all_post)
      
      pagi=Paginator(all_post,3)
      # print("🚀 ~ file: views.py ~ line 87 ~ pagi", pagi)
      
      page_number=request.GET.get('page')
      # print("🚀 ~ file: views.py ~ line 90 ~ page_number", page_number)

      page_obj=pagi.get_page(page_number)
      # print("🚀 ~ file: views.py ~ line 93 ~ page_obj", page_obj)
      return render(request,'ecommerce/index.html',{'page_obj':page_obj})
      # return render(request,'ecommerce/index.html')

def shop(request):
      return render(request,'ecommerce/shop.html')

def blog(request):
      return render(request,'ecommerce/blog.html')

def cart(request):
      filter_items= MyItem.objects.all()
      # q=MyItem.objects.select_related(Add_Cart).filter(cart__title_id__icontains=id)
      # print("🚀 ~ file: views.py ~ line 45 ~ q", q)
      print("🚀 ~ file: views.py ~ line 340 ~ filter_items", filter_items)                            

      
      return render(request, 'ecommerce/cart.html', {"filter_items":filter_items})
      # return render(request,'ecommerce/cart.html')

def contact(request):  
      return render(request,'ecommerce/contact-us.html')

def prod_details(request):  
      return render(request,'ecommerce/product-details.html')

def blog_single(request):  
      return render(request,'ecommerce/blog-single.html')
def category(request):  
      return render(request,'ecommerce/category.html')


def user_reg(request):  
      # u_form=User1Form(request.POST)
      

      if request.method == 'POST':
            fm = User1Form(request.POST)
            # if fm.is_valid():                # 1st method
            #  fm.save()

            if fm.is_valid():                  # 2nd method
              username = fm.cleaned_data['username']
              email = fm.cleaned_data['email']
            #   password = fm.cleaned_data['password']
              pwd = make_password(fm.cleaned_data['password'])
              print("🚀 ~ file: views.py ~ line 30 ~ password -------------------------", pwd)

              phone = fm.cleaned_data['phone']
              gender = fm.cleaned_data['gender']
              user_type = fm.cleaned_data['utype']


              reg = User1(username=username,email=email,password=pwd,phone=phone,gender=gender,user_type=user_type)
            #   reg.register()

              reg.save()        
              fm=User1Form()

      
      else:
            fm=User1Form()
      return render(request,'ecommerce/register.html',{'form':fm})
         

      # user_form = UserForm(request.POST)
      # if user_form.is_valid():
      #   user = user_form.save()

      #   if request.method == "POST":
      #         phone = request.POST.get("phone")
      #         gender = request.POST.get("gender")
              
      #         profile = UserProfile(phone=phone,gender=gender)
      #         profile.user = user
                
              
      #         profile.save()


      # profile_form = ProfileForm(request.POST)
           
      # if user_form.is_valid() and profile_form.is_valid():
      #       user = user_form.save()
      #       profile = UserProfile(phone=phone,gender=gender)
      #       print("====================================",profile)
      #       profile.user = user
      #       profile.save()
      #       return render(request,'ecommerce/login.html',{'user_form': user_form,'profile_form': profile_form})

      # else:
      #   user_form = UserForm()
      #   profile_form = ProfileForm()
      # return render(request,'ecommerce/login.html',{'user_form': user_form,'profile_form': profile_form})



# demo 
def demo_view(request):
      all_post=Category.objects.all().order_by('id')
      # print("🚀 ~ file: views.py ~ line 84 ~ all_post", all_post)
      
      pagi=Paginator(all_post,2)
      # print("🚀 ~ file: views.py ~ line 87 ~ pagi", pagi)
      
      page_number=request.GET.get('page')
      # print("🚀 ~ file: views.py ~ line 90 ~ page_number", page_number)

      page_obj=pagi.get_page(page_number)
      # print("🚀 ~ file: views.py ~ line 93 ~ page_obj", page_obj)
      return render(request,'ecommerce/demo.html',{'page_obj':page_obj})
      # return render(request,'ecommerce/demo.html',{'all_post':all_post})


# show category
def show_view(request):
      # all_category=Item.objects.all().order_by('id')
      all_category=MyItem.objects.all()

      # print("🚀 ~ file: views.py ~ line 84 ~ all_post", all_post)
      
      pagi=Paginator(all_category,3)
      # print("🚀 ~ file: views.py ~ line 87 ~ pagi", pagi)
      
      page_number=request.GET.get('page')
      # print("🚀 ~ file: views.py ~ line 90 ~ page_number", page_number)

      page_obj=pagi.get_page(page_number)
      # print("🚀 ~ file: views.py ~ line 93 ~ page_obj", page_obj)
      return render(request,'ecommerce/show_category.html',{'page_obj':page_obj})
      # return render(request,'ecommerce/show_category.html',{'all_category':all_category})



      # user_form = UserForm(request.POST)
      # if user_form.is_valid():
      #   user = user_form.save()

      #   if request.method == "POST":
      #         phone = request.POST.get("phone")
      #         gender = request.POST.get("gender")
              
      #         profile = UserProfile(phone=phone,gender=gender)
      #         profile.user = user
                
              
      #         profile.save()


      # profile_form = ProfileForm(request.POST)
           
      # if user_form.is_valid() and profile_form.is_valid():
      #       user = user_form.save()
      #       profile = UserProfile(phone=phone,gender=gender)
      #       print("====================================",profile)
      #       profile.user = user
      #       profile.save()
      #       return render(request,'ecommerce/login.html',{'user_form': user_form,'profile_form': profile_form})

      # else:
      #   user_form = UserForm()
      #   profile_form = ProfileForm()
      # return render(request,'ecommerce/login.html',{'user_form': user_form,'profile_form': profile_form})



def login_view(request):
      if request.method == "POST":
            
            uname=request.POST['username']
            # email=request.POST['email']
            password=request.POST['password']
            
            print("------------------------------------------------",uname)
            # print("------------------------------------------------",email)
            print("------------------------------------------------",password)

            user=authenticate(username=uname,password=password)
            print("🚀 ~ file: views.py ~ line 165 ~ user", user)
            
            if user is not None:
                  login(request,user)
                  # return redirect("profile",uname=user)

                  return render(request,'ecommerce/welcome.html',{'uname':user})
                  # return render(request,'ecommerce/index.html',{'uname':user})

            else:
                  return HttpResponseRedirect('/demo/')
     
      # print('login......')
      return render(request,'ecommerce/login.html')

# ---------------------
def user_profile(request):
      # print("=========================================>>>>>>>..",user_form)
      # if user_form.is_valid():
      #   user = user_form.save()
      # #   print("=================================>>>>>>>>..",user)
              
            #   profile = UserReg(phone=phone,gender=gender)
            #   profile.user = user               
            #   profile.save()

      profile_form = ProfileForm(request.POST)
         

      if request.method == "POST":
              user_form = UserForm(request.POST)
            #   password = make_password(request.POST.get("password"))
            #   print("🚀 ~ file: views.py ~ line 203 ~ password", password)

              phone = request.POST.get("phone")
              gender = request.POST.get("gender")
              user_type=request.POST.get("user_type")
              print("🚀 ~ file: views.py ~ line 245 ~ user_type", user_type)

              if user_form.is_valid() and profile_form.is_valid():

                  user = user_form.save()
                  profile = UserReg(phone=phone,gender=gender,user_type=user_type)

                  print("====================================",profile)
                  profile= profile_form.save(commit=False)
                  profile.user = user
                  profile.save()

                  pwd= user_form.cleaned_data['password']
                  # print(pwd)
                  user.set_password(pwd)
                  user.save()
                  return render(request,'ecommerce/register.html',{'user_form': user_form,'profile_form': profile_form})

      else:
            user_form = UserForm()
            profile_form = ProfileForm()
      return render(request,'ecommerce/register.html',{'user_form': user_form,'profile_form': profile_form})

# def search(request):
#       if request.method == "POST":
#             name=request.POST.get("txt")
#             print("🚀 ~ file: views.py ~ line 246 ~ name--------------------------------", name)
#       return render(request,'ecommerce/search.html')


def search(request):
    """ search function  """
    if request.method == "POST":
        name=request.POST.get("txt")
        print("🚀 ~ file: views.py ~ line 254 ~ name", name)

      #   query_name = request.POST.get('name', None)
      #   print("🚀 ~ file: views.py ~ line 254 ~ query_name", query_name)
        
        if name:
            results = Item.objects.filter(item_category__contains=name)
            print("🚀 ~ file: views.py ~ line 105 ~ results", results)
            
            return render(request, 'ecommerce/search.html', {"results":results})
        else:
          return HttpResponse("not found")
    return render(request, 'ecommerce/search.html')

    
# def get_value(request):  
#       if request.method=="GET":
#             # name=request.POST.get("tshirt")
#             name=request.POST["value"]

#             print("🚀 ~ file: views.py ~ line 272 ~ name", name)
      
#       return render(request,'ecommerce/index.html')

# def get_value(request):
#   if request.method == 'POST':
#       answer = request.POST["value"]
#       print("🚀 ~ file: views.py ~ line 285 ~ answer", answer)
#   return render(request,'ecommerce/index.html')



# -----------

def show(request):
      all_item=MyItem.objects.all().order_by()
      return render(request,'ecommerce/myitem.html',{'all_data':all_item})


def get_my_category(request):
      all_post= MyCategory.objects.all().order_by()

      print("🚀 ~ file: views.py ~ line 294 ~ all_post", all_post)

      return render(request,'ecommerce/index.html',{'page_obj':all_post})
      # return render(request,'ecommerce/demo.html',{'all_post':all_post})


def get_my_category_id(request, id):

      print("------------------------",id )
      filter_items= MyItem.objects.filter(item_category=id)
      print(filter_items)

      return render(request,'ecommerce/myitem.html',{'filter_items':filter_items})

# def add_cart(request,id):

#       print("------------------------",id )
#       filter_items= MyItem.objects.filter(id=id)
#       data=filter_items.object.get()
#       print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",data)
#       # print(filter_items)
#       return render(request,'ecommerce/add_cart.html',{'filter_items':filter_items})
# #       # return HttpResponse("add cart....")

def add_cart(request,id):

      print("------------------------",id )
      filter_items= MyItem.objects.filter(id=id)
      print("🚀 ~ file: views.py ~ line 340 ~ filter_items", filter_items)
      
      # all_data=MyItem.objects.all()
      # print("++++++++++++++++++++++++++++++++",all_data)

      # item_image = Add_Cart.objects.create(item_image=item_image)
      # item_details = Add_Cart.objects.create(item_details=id)
      # print("--------------------------------------", filter_items).first()
      # cart = Add_Cart.objects.create()
      # add_cart=Add_Cart.objects.create(id=MyItem.objects.all())
      all_cart=Add_Cart.objects.all()


      if filter_items:
            add_cart=Add_Cart.objects.create(title_id=id)
            print("🚀 ~ file: views.py ~ line 359 ~ add_cart", add_cart)
            add_cart.save()
      return render(request, 'ecommerce/add_cart.html', {"add_cart":add_cart,'filter_items':filter_items,'all_cart':all_cart})
      # return render(request, 'ecommerce/add_cart.html',{'filter_items':filter_items})

      # print(filter_items)
      # return render(request,'ecommerce/add_cart.html',{'filter_items':filter_items})
      # return HttpResponse("add cart....")



# def add_cart(request,id):

#       print("------------------------",id )
#       filter_items= MyItem.objects.filter(id=id)
#       data=filter_items.object.get()
#       print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",data)
#       # print(filter_items)
#       return render(request,'ecommerce/add_cart.html',{'filter_items':filter_items})
# #       # return HttpResponse("add cart....")


#add to cart 
def add_to_cart(request,id):

      print("---------- id  ----------",id )

      get_quantity= Add_Cart.objects.filter(title_id=id).first()
      print("---------- quantity  ---------- ", get_quantity.quantity)


      # q=Add_Cart.objects.values('quantity')
      # q=Add_Cart.objects.filter(quantity=get_quntity)

      # print("quntity ---------------------",q)
      
      # all_data=MyItem.objects.all()
      # print("++++++++++++++++++++++++++++++++",all_data)

      # item_image = Add_Cart.objects.create(item_image=item_image)
      # item_details = Add_Cart.objects.create(item_details=id)
      # print("--------------------------------------", filter_items).first()
      # cart = Add_Cart.objects.create()
      # add_cart=Add_Cart.objects.create(id=MyItem.objects.all())
      # all_cart=Add_Cart.objects.all()


      # if filter_items:
      #       add_cart=Add_Cart.objects.create(title_id=id)
      #       print("🚀 ~ file: views.py ~ line 359 ~ add_cart", add_cart)
      #       add_cart.save()
      # return render(request, 'ecommerce/add_cart.html', {"add_cart":add_cart,'filter_items':filter_items,'all_cart':all_cart})
      # # return render(request, 'ecommerce/add_cart.html',{'filter_items':filter_items})

      # print(filter_items)
      # return render(request,'ecommerce/add_cart.html',{'filter_items':filter_items})
      return HttpResponse("add to cart....")