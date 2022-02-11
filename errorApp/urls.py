from django.urls import path
from . import views


urlpatterns = [
    path('', views.basic, name='basic'),
    #     path('new/', views.new, name='new'),
    #     path('django/', views.django, name='django'),
    #     path('python/', views.python, name='python'),
    #     path('database/', views.database, name='database'),
    #     path('api/', views.api, name='api'),
    #     path('aws/', views.aws, name='aws'),
    #     path('frontend/', views.frontend, name='frontend'),
    #     path('extra/', views.extra, name='extra'),
]
