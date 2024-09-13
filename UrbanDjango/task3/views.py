from django.shortcuts import render
from django.views.generic import TemplateView


class main(TemplateView):
    template_name = 'platform.html'

def cart(request):
    context = {
        'items': ['Atomic Heart',
                  'Cyberpunk 2077',
                  'PayDay 2',
                  'Sega',
                  'Spectum ZX'],
        'back': '/'
    }
    return render(request, template_name='third_task/cart.html', context=context)


def games(request):
    context = {
        'back': '/',
        'cart': '/cart'
    }
    return render(request, template_name='third_task/games.html', context=context)