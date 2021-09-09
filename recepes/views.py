from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from .models import Recepes,Review
from django.db.models import Q
from .forms import RecepesForm
from django.http import JsonResponse
import json


# Create your views here.

def home(request):
    recepes = Recepes.objects.all()
    context = {'recepes':recepes}
    return render(request, 'home.html', context)

def detail_recepes(request,pk):
    recepes = Recepes.objects.get(id=pk)
    title =recepes.title
    user =recepes.user
    image =recepes.image
    method =recepes.method
    service_size =recepes.service_size
    cooking_time =recepes.cooking_time
    date_created =recepes.date_created
    calories =recepes.calories
    fat = recepes.fat
    protein =recepes.protein
    fibre = recepes.fibre
    carbohidrates = recepes.carbohidrates
    salt =recepes.salt

    if request.method == 'POST':
        Review.objects.create(
            content=request.POST['comment'],
            recipes=recepes,
            user=request.user,
        )

    context = {
        'title':title,
        'user':user,
        'image':image,
        'method':method,
        'service_size':service_size,
        'cooking_time':cooking_time,
        'date_created':date_created,
        'calories':calories,
        'fat':fat,
        'protein':protein,
        'fibre':fibre,
        'carbohidrates':carbohidrates,
        'salt':salt,
        'recepes':recepes,
    }
    return render(request, 'detail.html', context)

@login_required(login_url= 'login')
def profile_page(request):
    user = request.user
    recepes = Recepes.objects.filter(user=user)
    context = {'recepes':recepes}
    return render(request, 'profile.html', context)

@login_required(login_url= 'login')
def recepes_form(request):
    form = RecepesForm()
    if request.method == 'POST':
        user = request.user
        author = Recepes(user=user)

        form = RecepesForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
        return redirect('profile')

    context = {'form': form}
    return render(request, 'recepes_form.html', context)


@login_required(login_url= 'login')
def edit_recepes(request,pk):
    recepes = Recepes.objects.get(id=pk)
    form = RecepesForm(instance=recepes)
    if request.method == 'POST':
        form = RecepesForm(request.POST, request.FILES, instance=recepes,)
        if form.is_valid():
            form.save()
        return redirect('profile')
    context = {'form':form}
    return render(request, 'recepes_form.html', context)

@login_required(login_url= 'login')
def delete_recepes(request, pk):
    recepes = Recepes.objects.get(id=pk)
    title = recepes.title
    if request.method == 'POST':
        recepes.delete()
        return redirect('profile')
    context = {'recepes':recepes,'title':title}
    return render(request, 'delete.html', context)


def about_page(request):
    context = {}
    return render(request, 'about.html', context)

def contact_page(request):
    context = {}
    return render(request, 'contact.html', context)


def sendEmail(request):
    if request.method == 'POST':
        template = render_to_string('email_templates.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['gersondelacruzdeveloper@gmail.com']
        )

        email.fail_silently = False
        email.send()
    return render(request, 'email_sent.html')


def navbar_search_result(request):
    navbar_input = request.GET.get('search')
    recepes = Recepes.objects.all()
    if navbar_input:
        recepes = Recepes.objects.filter(Q(title__icontains=navbar_input) | Q(method__icontains=navbar_input))
    context = {'recepes':recepes, 'navbar_input':navbar_input}
    return render(request, 'result.html', context)
