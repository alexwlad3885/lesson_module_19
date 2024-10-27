from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse
from task1.models import Buyer, Game


def func_index(request):
    return render(request, 'index.html')


def func_index_1(request):
    Games = Game.objects.all()
    context = {
        'Games': Games,
    }
    return render(request, 'index_1.html', context)


def func_index_2(request):
    return render(request, 'index_2.html')


def sign_up_by_django(request):
    Buyers = Buyer.objects.all()
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

        for buyer in Buyers:
            if username in buyer.name:
                info['Error'] = 'Пользователь уже существует'
                return HttpResponse("Пользователь уже существует")
            elif password != repeat_password:
                info['Error'] = 'Пароли не совпадают'
                return HttpResponse('Пароли не совпадают')
            elif int(age) < 18:
                info['Error'] = 'Вы должны быть старше 18 лет'
                return HttpResponse('Вы должны быть старше 18')
            else:
                Buyer.objects.create(name=username, balance=0.00, age=age)
                HttpResponse(f'Приветствуем {username}')
                info['info'] = f'Приветствуем {username}'
                context = {'info': info, 'Buyers': Buyers}
            return render(request, 'index.html', context)

    else:
        form = UserRegister()

    context = {'info': info, 'form': form, 'Buyers': Buyers}
    return render(request, 'registration_page.html', context)
