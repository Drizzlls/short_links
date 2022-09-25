from turtle import pos
from urllib import request
from pytils.translit import slugify
import random
import string
from django.http import HttpRequest, HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import AddManager
from .models import Manager


class CRUDManger:
    """  Класс CRUD методов для работы с Менеджерами """

    # Удаление менеджера
    @staticmethod
    def del_manager(request, pk :int):
        try:
            manager = Manager.objects.get(pk=pk).delete()
            return HttpResponse('True')
        except:
            return HttpResponse('False')


    # Добавление менеджера
    @staticmethod
    def add_manager(request):
        if request.POST:
            try:
                manager = AddManager(request.POST)
                manager.save()
                return HttpResponse('True')
            except:
                return HttpResponse('False')


    # Редактирование менеджера
    @staticmethod
    def update_manager(request, pk :int):
        if request.POST:
            try:
                managerUpdate = Manager.objects.filter(pk=pk).update(name=request.POST['name'],surname=request.POST['surname'])
                return HttpResponse('True')
            except Exception as e:
                return HttpResponse('False')



# Страница списка всех менеджеров
def list_managers(request):
    managers = Manager.objects.all()
    formAddManager = AddManager()
    return render(request, 'managers/list_managers.html', {'list': managers,'formAddManager':formAddManager})

# Страница менеджера
def page_manager(request, pk :int):
    try:
        manager = Manager.objects.get(pk=pk)
        return render(request, 'managers/one_manager.html', {'manager': manager})
    except:
        return render(request, '404.html', status=404)
