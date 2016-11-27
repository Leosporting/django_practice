# Register your models here.
from  django.contrib  import admin
import sys
print sys.path

from  models import  Restaurant,Food,Comment


class RestaurantAdmin(admin.ModelAdmin):
    list_display=('name','phone_number','address')

class FoodAdmin(admin.ModelAdmin):
    list_display=('name','restaurant','price')
    list_filter=('is_spicy',)
admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Food,FoodAdmin)
admin.site.register(Comment)
