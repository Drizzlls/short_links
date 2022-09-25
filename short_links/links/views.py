from turtle import pos
from urllib import request
from pytils.translit import slugify
import random
import string
from django.http import HttpRequest, HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from managers.models import Manager
# from .forms import CreateLink,AddManager
from agents.models import Agent


# Генератор рандомной строки
def generageLink():
    return ''.join(random.choice(string.ascii_letters.lower()) for x in range(9))

# Страница редиректа на нужный домен
def pageRedirect(request, link :str):
    domen = 'https://www.google.com/'
    try:
        agent = Agent.objects.get(link_agent=link)
        linkGeneration = f'{domen}?personal_manager={agent.manager_personal.id}?id_agent={agent.pk}'
        return redirect(linkGeneration)
    except:
        return render(request, '404.html', status=404)


#
# # Страница генерации ссылки и сохранения данных в бд
# def generate_link(request):
#     random_link = random_char()
#     data = {
#         'name': request.POST['name'],
#         'surname': request.POST['surname'],
#         'agent_phone': request.POST['agent_phone'],
#         'manager_personal': Manager.objects.get(pk=request.POST['manager_personal']),
#         'link_agent': random_char(),
#     }
#     createLinfForm = CreateLink(data)
#     createLinfForm.save()
#     agent = Agent.objects.get(link_agent=data['link_agent']).manager_personal
#     agent.agents+=1
#     agent.save()
#     return HttpResponse(data['link_agent'])
#
# # Страница 404
# def page_not_found_view(request, exception):
#     return render(request, '404.html', status=404)
#


# def userRgister(request):
#     return render(request, 'user/register.html')
#
# def userSigIn(request):
#     return render(request, 'user/sigin.html')


# class RegisterUser(DataMixin, CreateView):
#     form_class = UserCreationForm
#     template_name = 'user/sigin.html'
#     success_url = reverse_lazy('login')

