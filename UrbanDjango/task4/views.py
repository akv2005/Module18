from django.shortcuts import render
from django.views.generic import TemplateView


class main(TemplateView):
    template_name = 'platform.html'

def cart(request):
    mydict = {'games': ["Atomic Heart", "Cyberpunk 2077", "ZX Spectrum 1982"]}
    context = {
        'mydict': mydict,
    }

    return render(request, 'fourth_task/cart.html', context)




def games(request):
    context = {
        'back': '/',
        'cart': '/cart'
    }
    return render(request, template_name='fourth_task/games.html', context=context)




