# Register your models here.
from  django.contrib  import admin


import os
os.environ['DJANGO_SETTINGS_MODULE']='mysite.settings'
#print os.environ['DJANGO_SETTINGS_MODULE']
import sys
sys.path.append('C:\Users\luck\Desktop\django_practice\mysite0910')
print sys.path
import mysite0910

from  models import  Restaurant,Food,Comment


class RestaurantAdmin(admin.ModelAdmin):
    list_display=('name','phone_number','address')

class FoodAdmin(admin.ModelAdmin):
    list_display=('name','restaurant','price')
    list_filter=('is_spicy',)
admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Food,FoodAdmin)
admin.site.register(Comment)
