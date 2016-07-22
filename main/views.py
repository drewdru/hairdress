from django.http import HttpResponseRedirect
# from django.contrib import auth
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import RequestContext
# from django.core.mail import send_mail
# from django.core.mail import EmailMessage
from main.models import Book
from main.forms import ContactForm
import datetime


# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = auth.authenticate(username=username, password=password)
#     if user is not None and user.is_active:
#         # Правильный пароль и пользователь "активен"
#         auth.login(request, user)
#         # Перенаправление на "правильную" страницу
#         return HttpResponseRedirect("/account/loggedin/")
#     else:
#         # Отображение страницы с ошибкой
#         return HttpResponseRedirect("/account/invalid/")

# def logout(request):
#     auth.logout(request)
#     # Перенаправление на страницу.
#     return HttpResponseRedirect("/account/loggedout/")

# import settings
   
def home(request):
    now = datetime.datetime.now()
    return render(request, 'home.html', {
        'current_date': now,
    })
def lang(request):
    return render(request, 'lang.html', {
        'redirect_to': '/'
    })

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render('search_results.html',
                {'books': books, 'query': q})
    return render(request, 'search_form.html',
        {'errors': errors})
        
# def contact(request):
#     errors = []   
    
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             send_mail(
#                 cd['subject'],
#                 cd['message'],
#                 cd.get('email', 'noreply@example.com'),
#                 ['siteowner@example.com'],
#             )
#             return HttpResponseRedirect('/contact/thanks/')
#     else:
#         form.clean()# = ContactForm(initial={'subject': 'I love your site!'})
#     return render(request, 'contact_form.html',{'form': form})
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # send_mail(
            #     cd['subject'],
            #     cd['message'],
            #     cd.get('email', 'noreply@example.com'),
            #     ['siteowner@example.com'],
            # )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
    return render(request,'contact_form.html', {'form': form})
    
def day_view(request, month, day):
    now = datetime.datetime.now()
    return render(request, 'today.html',{'now': now, 'month': month, 'day':day})

def user_day_view(request, user):
    now = datetime.datetime.now()
    return render(request, 'today.html',{'user': user})
    
def requires_login(view):
    def new_view(request, *args, **kwargs):
        print(request)
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)
        return view(request, *args, **kwargs)
    return new_view