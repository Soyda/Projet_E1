from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path("login_required_page", views.login_required_view, name='login_required_view'),
    path("test_form", views.test_form, name='test_form'),
    path("add_file/", views.FileFieldFormView.as_view(), name='add_file'),
    path('add_file_done/', views.add_file_done, name='add_file_done'),
    path('see_verbatims/', views.see_verbatims, name='see_verbatims'),


]