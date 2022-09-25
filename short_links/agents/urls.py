from django.urls import path
from .views import *
from .models import *


urlpatterns = [
    path('', allAgents, name='all_agents'),
    path('form_add', addAgent, name='page_from_add_agent'),
    path('user/<int:pk>', personalPage, name='personal_page'),
    path('del/<int:pk>', CRUDAgent.del_agent, name='del_agent'),
    path('update/<int:pk>', CRUDAgent.update_agent, name='update_agent'),
    path('add/', CRUDAgent.add_agent, name='add_agent'),
]
# handler404 = "links.views.page_not_found_view"