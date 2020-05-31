from django.contrib import admin
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from .models import Profile
from django.conf import settings
from django.core.mail import send_mail
from .forms import SendEmailForm
# Register your models here.
# admin.site.register(Profile)
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.contrib import messages


# def send_email(modeladmin, request, queryset):
#     ###############
#     if request.method == 'POST':
#         form = SendEmailForm(request.POST)
#         if form.is_valid():
#             form.save()
#             subject = form.cleaned_data.get('subject')
#             text = form.cleaned_data.get('message')
#             users = queryset
#             messages.success(request, f'Сообщение отправлено!')
#
#             for item in queryset:
#                 user = item.user
#                 user.profile.verified = True
#                 user.save()
#                 msg = render_to_string('email_templates/email.html', {'name': user.username, 'id': user.id, 'msg' : text})
#                 send_mail(subject, msg, settings.EMAIL_HOST_USER, ['e.vashinko@gmail.com'])
#
#             return redirect('login-page')
#     else:
#         form = SendEmailForm()
#     return render(request, 'email_templates/send_email.html', {'form': form})
#     ##############

# def send_email(modeladmin, request, queryset):
#     for item in queryset:
#         user = item.user
#         text = ''
#         msg = render_to_string('email_templates/email.html', {'name': user.username, 'id': user.id, 'msg' : text})
#         send_mail('Hello', msg, settings.EMAIL_HOST_USER, ['e.vashinko@gmail.com'])

def send_email(modeladmin, request, queryset):
    form = SendEmailForm(initial={'users': queryset})
    return render(request, 'email_templates/send_email.html', {'form': form})


send_email.short_description = "Send Email"


class ProfileAdmin(admin.ModelAdmin):
    actions = [send_email]


admin.site.register(Profile, ProfileAdmin)
