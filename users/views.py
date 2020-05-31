from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, SendEmailForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from helpers import mail
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hello {username}! Your account has been created! Log in please!')
            return redirect('login-page')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form})


@login_required
def profile(request):                                                                                                                            # pragma: no cover
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile-page')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


def confirm(request, pk):
    user = User.objects.get(id=pk)
    user.profile.verified = True
    user.save()
    return redirect('news:home-page')


def send_mes(request):                                                                                                                  # pragma: no cover
    form = SendEmailForm(request.POST)

    if form.is_valid():
        subject = form.cleaned_data.get('subject')
        text = form.cleaned_data.get('message')
        users = form.cleaned_data['users']
        messages.success(request, f'Сообщение отправлено!')
        count = len(users)
        for item in users:
            user = item.user
            msg = render_to_string('email_templates/email.html', {'name': user.username, 'id': user.id, 'msg' : text})
            # send_mail(subject, msg, settings.EMAIL_HOST_USER, ['e.vashinko@gmail.com'])
            if count != 1:
                mail.send_email(subject, msg, 'e.vashinko@gmail.com')
            else:
                mail.send_email(subject, msg, 'e.vashinko@gmail.com', True)
            count -= 1


        return redirect('/admin/users/profile/')


# def send_mes(request):
#     return HttpResponse('Отправка сообщения')
