from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('', views.index, name='index'),
    path('tree/<int:tree_id>/', views.tree, name='tree'),
    path('person/<int:person_id>/', views.person, name='person')
]