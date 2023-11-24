from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display= ['title','puplish_date']
    search_fields = ['title','content']
    list_filter = ['puplish_date','author']




admin.site.register(Post,PostAdmin)
