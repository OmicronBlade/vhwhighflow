from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', highflowList.as_view()),
    path('list/<pk>/', highflowInidividual.as_view(), name='list'),
    path('create/', highflowCreate.as_view()),
    path('update/<pk>/', highflowUpdateView.as_view()),
    path('<pk>/create/sats/', satsCreate.as_view()),
    path('<pk>/update/sats/', satsUpdateView.as_view())
]
