from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request):
    """
        функция для входа в систему
    """
    # если тип запроса post(нажата кнопка submit)
    if request.method == 'POST':
        # form - полученные из формы данные, которые заполнил пользлователь
        form = LoginForm(request.POST)
        # проверяем форму на валидность
        if form.is_valid():
            # очишаем форму
            cd = form.cleaned_data
            """
                аутентифицируем пользователя
                authenticate - передаем request, username, password
                если пароль правильный, возвращает объект User
                елси не правильный то None
            """
            user = authenticate(request, username=cd['username'],
                                        password=cd['password'])
            # если authenticate вернул не None значит логин пароль подошли
            if user is not None:
                # is_active - булево, указывает активный аккаунт или нет
                if user.is_active:
                    # Логин - передаем request и обьект user, аутентифицируем пользователя
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        # если тип запроса не POST выдаем пустую форму
        form = LoginForm()
        # рендерим страницу с пустой формой
        return render(request, 'account/login.html', {'form': form})