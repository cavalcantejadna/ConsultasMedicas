from django.conf.urls import include, url
from appconsultas.views import *
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^medico/list$', medico_list, name='medico_list'),
    url(r'^medico/new/$', medico_new, name='medico_new'),

    url(r'^paciente/list$', paciente_list, name='paciente_list'),
    url(r'^paciente/new/$', paciente_new, name='paciente_new'),

    url(r'^consulta/list$', consulta_list, name='consulta_list'),
    url(r'^consulta/new/$', consulta_new, name='consulta_new'),

]