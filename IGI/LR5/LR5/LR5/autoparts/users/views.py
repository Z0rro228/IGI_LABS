from datetime import datetime
import re

import pytz
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_user, logout
from django.contrib import messages
from .forms import LoginForm, SignUpForm
from .models import CustomUser
import logging

logging.basicConfig(level=logging.INFO, filename='app.log', format='%(asctime)s - %(levelname)s - %(message)s')

# Create your views here.


def login(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                logging.info(" вошел в аккаунт")
                logging.info(f"{user.username} вошел в аккаунт")
                login_user(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('/')
            else:
                msg = 'invalid info'
                messages.success(request, "Ошибка, неправильный логин или пароль, повторите попытку!")
                return redirect('.')
            # return redirect('/')
        else:
            msg = 'error valid form'

    return render(request, 'users/login.html', {'form': form, 'msg': msg})


def calculate_age(birth_date: datetime):
    current_date = datetime.now().date()
    age = current_date.year - birth_date.year
    if current_date.month < birth_date.month or (
            current_date.month == birth_date.month and current_date.day < birth_date.day):
        age -= 1
    return age


def registration(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            address = request.POST.get('address', '')
            telephone = request.POST.get('tel', '')
            PHONE_NUMBER_REGEX = r"^\+375(\s+)?\(?(17|29|33|44)\)?(\s+)?[0-9]{3}-[0-9]{2}-[0-9]{2}$"
            if not re.match(PHONE_NUMBER_REGEX, telephone):
                form.add_error('username', 'Некорректный формат телефонного номера')
                return render(request, 'users/registration.html', {'form': form, 'msg': 1})

            date_of_birth = form.cleaned_data.get('date_of_birth')
            user_age = calculate_age(date_of_birth)
            if user_age < 18:
                form.add_error('date_of_birth', 'Вам нет 18!')
                return render(request, 'users/registration.html', {'form': form, 'msg': 1})

            user.is_customer = True
            user.save()
            CustomUser.objects.create(user=user, address=address, phone=telephone)
            logging.info(f"{user.username} зарегистрирован")
            return redirect('/')
    logging.info(f"Вызвана страница регистрации")
    return render(request, 'users/registration.html', {'form': form, 'msg': 1})


@login_required
def logout_user(request):
    logout(request)
    logging.info(f"{request.user.username} вышел из аккаунта")
    return redirect('/')
