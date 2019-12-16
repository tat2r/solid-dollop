from django.conf.urls import url
from adobe_app import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('test',views.test,name='test'),
    path('formpage/', views.form_name_view, name='form_name'),
]
