from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name = 'SolsHome'),
    path('List', views.listview, name = 'SolsList'),
    path('GetTableMeta', views.tablemeta, name = 'tablemeta'),
    path('GetTableData', views.tabledata, name = 'tabledata'),
    path('CreateList', views.createnewlist, name = 'updatetabledata'),
    path('NewList', views.newlist, name = 'Newlist'),
    path('EditList', views.editlist, name='Editlist'),
]