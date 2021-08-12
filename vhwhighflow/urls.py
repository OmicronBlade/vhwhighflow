from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', highflowDashboard.as_view()),
    path('redlist/', highflowRedList.as_view()),
    path('list/', highflowList.as_view()),
    path('list_all/', highflowListAll.as_view()),
    path('list/<pk>/', highflowInidividual.as_view(), name='list'),
    path('create/', highflowCreate.as_view()),
    path('update/<pk>/', highflowUpdateView.as_view()),
    path('<int:pk>/create/sats/', satsCreate.as_view()),
    path('<int:pk>/update/sats/', satsUpdateView.as_view())
]
