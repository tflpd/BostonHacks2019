from django.contrib import admin
from django.urls import path

from remempill import views
from remempill.views import *


urlpatterns = [
    # path('', views.index, name='index'),
    path('', Index.as_view()),
    path('pillcase', views.pillcase, name="pillcase"),
    path('logout/', views.logout, name="logout", ),
    path('callresponse/<str:consumption_id>', views.callresponse, name="callresponse"),
    path('dynamic_call_creator/<str:consumption_id>', views.dynamic_call_creator, name="dynamic_call_creator"),
]

admin.site.site_header = 'RememPill Administration Site'
admin.site.site_title = 'RememPill Administration Site'
