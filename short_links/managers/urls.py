from django.urls import path
from .views import *
from .models import Manager

urlpatterns = [
    path('',list_managers,name="list_managers"),
    path('manager/<int:pk>',page_manager,name="page_manager"),
    path('manager/add_manager',CRUDManger.add_manager,name="add_manager"),
    path('manager/del_manager/<int:pk>',CRUDManger.del_manager,name="del_manager"),
    path('manager/update_manager/<int:pk>',CRUDManger.update_manager,name="update_manager"),
]
# handler404 = "managers.views.page_not_found_view"