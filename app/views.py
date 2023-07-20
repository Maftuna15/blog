from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm
def lala(request):
    return render(request, 'index.html')

def forms(request):
    form= CustomerForm(request.POST)
    if request.POST and form.is_valid():
        form.save()
        return redirect('customer-list')
    ctx={
        'form':form
    }
    return render(request, 'form.html', ctx)