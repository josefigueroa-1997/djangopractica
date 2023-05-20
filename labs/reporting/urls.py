from . import views
from django.urls import path

urlpatterns = [

    path('dashboard/', views.dashboard, name="dashboard"),
    path('formreport/',views.formreport,name="formreport"),
]