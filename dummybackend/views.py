from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
import json, ast

# Create your views here.
@csrf_exempt
def listAPIView(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data['action'] == "create":
            data = data['data']
            obj = models.lists(Listname=data['Listname'],Listdescription=data['Listdescription'],columns=data['columns'])
            obj.save()
            return HttpResponse('ok')
        elif data['action'] == "update":
            pass
        elif data['action'] == 'delete':
            pass

    elif request.method == 'GET':
        return HttpResponse(json.dumps(getlist(request)))

def getlist(request):
    if 'list_id' in list(request.GET.keys()):

        list_desc = list(models.lists.objects.filter(id=request.GET['list_id']).values())[0]
        data={k:v for k,v in list_desc.items() if k != 'columns'}
        data["columns"]=ast.literal_eval(list_desc['columns'])
    else:
        data = list(models.lists.objects.filter().values())
    return data


def data(request):
    pass