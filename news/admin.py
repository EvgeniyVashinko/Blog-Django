from django.contrib import admin
from django.shortcuts import render

from .models import Post, Comment
from django.contrib.auth.models import User
from django.http import HttpResponse
# from .forms import SendEmailForm
# Register your models here.

# admin.site.register(Post)
admin.site.register(Comment)


# @admin.register(User)
# class CustomUserAdmin(admin.ModelAdmin):
#     actions = ['send_email', ]
#
#     def send_email(self, request, queryset):
#         form = SendEmailForm(initial={'users': queryset})
#
#         return render(request, 'email_templates/send_email.html', {'form': form})


def change_name(modeladmin, request, queryset):
    queryset.update(title='p')


change_name.short_description = "Change_name"


class ArticleAdmin(admin.ModelAdmin):
    actions = [change_name]


admin.site.register(Post, ArticleAdmin)
