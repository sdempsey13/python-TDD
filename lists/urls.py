from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^([0-9]+)/$', views.view_list, name='view_list'), # Change \d to r'^([0-9]+)$' to capture numbers greater than 9
    url(r'^([0-9]+)/add_item$', views.add_item, name='add_item'), # Change \d to r'^([0-9]+)$' to capture numbers greater than 9
]
