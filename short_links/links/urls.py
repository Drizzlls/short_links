from django.urls import path
from .views import *
from .models import *

urlpatterns = [
    path('<str:link>', pageRedirect, name="redirect"),

]
# handler404 = "links.views.page_not_found_view"