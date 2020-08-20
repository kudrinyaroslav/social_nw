from django import forms

class LoginForm(forms.Form):
    """
        создаем форму авторизации
        username - имя пользователя
        password - пароль
        CharField - тип данных символьный
        widget - как будет отоборажаться поле
        PasswordInput - отображение поля в виде парольного
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)