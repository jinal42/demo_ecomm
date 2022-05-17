from django.shortcuts import render
from .forms import User1Form, UserForm
from .models import Category, Item, MyCategory, MyItem, User1, UserReg
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.hashers import make_password

# from .models import UserProfile
# from .forms import User1Form, UserForm,ProfileForm

from .forms import UserForm,ProfileForm




# Create your views here.


def home(request):
      # {% static 'css/style.css' %}

      # all_post=MyCategory.objects.all()
      # print("🚀 ~ file: views.py ~ line 294 ~ all_post", all_post)

      # # if request.method == "POST":
      # #   query_name = request.POST.get('name', None)
        
      # #   if query_name:
      # #       results = MyCategory.objects.filter(username__contains=query_name)
      # #       print("🚀 ~ file: views.py ~ line 105 ~ results", results)
            
      # #       return render(request, 'ecommerce/index.html', {"results":results,'page_obj':all_post})
      # #   else:
      # #     return HttpResponse("not found")
      # # return render(request, 'ecommerce/index.html')
     
      # return render(request,'ecommerce/index.html',{'page_obj':all_post})
      return render(request,'ecommerce/index.html')

def shop(request):
      return render(request,'ecommerce/shop.html')

def blog(request):
      return render(request,'ecommerce/blog.html')

def cart(request):
      return render(request,'ecommerce/cart.html')

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

              reg = User1(username=username,email=email,password=pwd,phone=phone,gender=gender)
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
      all_category=Item.objects.all()

      # print("🚀 ~ file: views.py ~ line 84 ~ all_post", all_post)
      
      pagi=Paginator(all_category,2)
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
              if user_form.is_valid() and profile_form.is_valid():

                  user = user_form.save()
                  profile = UserReg(phone=phone,gender=gender)

                  # print("====================================",profile)
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



def get_my_category(request):
      all_post= MyCategory.objects.all().order_by()

      print("🚀 ~ file: views.py ~ line 294 ~ all_post", all_post)

      # results = MyItem.objects.filter(item_category__contains=id)

      # i = MyCategory.objects.filter(category=all_post).order_by('id')
      # print("🚀 ~ file: views.py ~ line 315 ~ results", i)

      # i=MyItem.objects.all(pk=id)
      # print("🚀 ~ file: views.py ~ line 314 ~ i", i)
      

      return render(request,'ecommerce/index.html',{'page_obj':all_post})
      # return render(request,'ecommerce/demo.html',{'all_post':all_post})

def show(request):
      all_item=MyItem.objects.all().order_by()
      return render(request,'ecommerce/myitem.html',{'all_data':all_item})


def get_my_category_id(request, id):

      print("------------------------",id )
      filter_items= MyItem.objects.filter(item_category=id)
      print(filter_items)
      # results = MyItem.objects.filter(item_category__contains=id)

      # i = MyCategory.objects.filter(category=all_post).order_by('id')
      # print("🚀 ~ file: views.py ~ line 315 ~ results", i)

      # i=MyItem.objects.all(pk=id)
      # print("🚀 ~ file: views.py ~ line 314 ~ i", i)
      

      return render(request,'ecommerce/myitem.html',{'filter_items':filter_items})