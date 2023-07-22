from django.shortcuts import render
# Create your views here.
import random
import string


def home(request):
    return render(request, 'generator/home.html')


def password(request):

    pass_length = int(request.GET.get('length', 8))

    isUpper = request.GET.get('uppercase', False)
    isDigits = request.GET.get('numbers', False)
    isSpecial = request.GET.get('special', False)

    chars = list(string.ascii_lowercase)
    upp_chars = list(string.ascii_uppercase)
    digits = list(string.digits)
    special = list('!@#$%^&*()_+')
    thepassword = ''

    if isUpper:
        chars.extend(upp_chars)
    if isDigits:
        chars.extend(digits)
    if isSpecial:
        chars.extend(special)
    for i in range(0, pass_length):
        thepassword += random.choice(chars)

    return render(
        request,
        'generator/password.html',
        {'password': thepassword}
    )


def about(request):
    return render(request, 'generator/about.html')
