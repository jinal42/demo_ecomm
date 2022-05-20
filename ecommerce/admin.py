from django.contrib import admin
from .models import  Add_Cart, MyCategory, MyItem, User1,Category,Item,All_Category
# from .models import   UserProfile
from django.contrib.auth.forms import UserCreationForm
from .models import  UserReg



# Register your models here.


# admin.site.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
 list_display=('id','username','email','gender','phone')

admin.site.register(Category)
class PostAdmin(admin.ModelAdmin):
      list_display=['id','title','desc','price','cloth_image']

class User1Admin(admin.ModelAdmin):
      list_display=['id','username','email','password','gender','phone']

# admin.site.register(User1,User1Admin)
# ----------------------------------

@admin.register(UserReg)
class UserAdmin(admin.ModelAdmin):
 list_display=('id','user','phone','gender','user_type')



admin.site.register(Item)
class PostAdmin(admin.ModelAdmin):
      list_display=['id','title','desc','price','item_category','item_image']

admin.site.register(All_Category)
class PostAdmin1(admin.ModelAdmin):
      list_display=['id','title','desc','price','item_category','item_image']

admin.site.register(MyCategory)

admin.site.register(MyItem)
admin.site.register(Add_Cart)
