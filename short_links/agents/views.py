from django.shortcuts import render
from .models import Agent
from .forms import AddAgent
from django.http import HttpResponse
from links.views import generageLink


class CRUDAgent:
    """  Класс CRUD методов для работы с Агентами """

    # Удаление Агента
    @staticmethod
    def del_agent(request, pk :int):
        if request.POST:
            try:
                agent = Agent.objects.get(pk=pk).delete()
                return HttpResponse('True')
            except:
                return HttpResponse('False')


    # Добавление Агента
    @staticmethod
    def add_agent(request):
        if request.POST:
            try:
                agent = AddAgent(request.POST)
                agent.save()
                return HttpResponse('True')
            except Exception as e:
                return HttpResponse('False')


    # Редактирование Агента
    @staticmethod
    def update_agent(request, pk :int):
        if request.POST:
            try:
                managerUpdate = Agent.objects.filter(pk=pk).update(name=request.POST['name'],surname=request.POST['surname'])
                return HttpResponse('True')
            except Exception as e:
                return HttpResponse('False')


# Страница со списком Агентов
def allAgents(request):
    allAgents = Agent.objects.all()
    return render(request, 'agents/all_agents.html', {'allAgents': allAgents})


# Страница добавления Агента
def addAgent(request):
    formAddAgent = AddAgent()
    return render(request, 'agents/add_agent.html', {'formAddAgent': formAddAgent})


# Страница отдельного Агента
def personalPage(request,pk):
    try:
        agent = Agent.objects.get(pk=pk)
        return render(request, 'agents/personal_page.html', {'agent': agent})
    except:
        return render(request, '404.html', status=404)
