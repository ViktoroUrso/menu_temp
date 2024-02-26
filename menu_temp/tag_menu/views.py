'''Tag Menu vievs module.'''
from django.shortcuts import render


def index(request, *args, **kwargs):
    return render(request, 'base.html', context={})


def show_selected(request, *args, **kwargs):
    context = {
        'selected_name': kwargs['selected']
    }
    return render(request, 'base.html', context=context)
