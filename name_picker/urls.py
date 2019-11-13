from django.urls import path
from . import views


urlpatterns = [
    path('', views.overview_page, name='index'),
    path('login-page', views.login, name='login'),
    # path('form-page', views.ghost_name_form, name='form-page')
    path('form-page', views.ghost_name_form, name='form-page'),
    # path('form-page/<str:false>', views.ghost_name_form, name='form-page'),
    path('<logged>', views.overview_page, name='index')
]