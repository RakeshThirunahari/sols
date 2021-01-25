from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name = 'SolsHome'),
    path('t', views.home2, name = 'SolsHome'),
    path('GetTableMeta', views.tablemeta, name = 'tablemeta'),
    path('GetTableData', views.tabledata, name = 'tabledata'),
    path('UpdateTableData', views.updatetabledata, name = 'updatetabledata'),
]