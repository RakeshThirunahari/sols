from django.shortcuts import render
from django.http import HttpResponse
import json, io, time
import requests
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def home(request):
  url = 'http://localhost:8000/api/List'
  r = requests.get(url)
  return render(request, "home.html", {'list':r.json()})

def listview(request):
    r =requests.get(url='http://localhost:8000/api/List?list_id='+request.GET['list_id'])
    return render(request, "test.html", r.json())

def newlist(request):
    return render(request, "newlist.html")

def editlist(request):
    r = requests.get(url='http://localhost:8000/api/List?list_id=' + request.GET['list_id'])
    data = r.json()
    data['data_type'] = {"text":"Short text","textarea":"Long text","number":"Number","date":"Date","select":"List"}
    data['filter_type'] = {"select":"Single selection", "multi_select":"Multi selection", "text":"Text",
                            "date":"Date",
                            "range_number":"Number range",
                            "range_date":"Date range" }
    print(data)
    return render(request, "editlist.html",data)


def tablemeta(request):
    msgl = {"Column":[
        {"Name":"ORD_NUM","Editable":False,"Searchable":True,"Class":"ORD_NUM"},{"Name":"ORD_AMOUNT","Editable":True,"Searchable":True,"Class":"ORD_AMOUNT"},{"Name":"ADVANCE_AMOUNT","Editable":True,"Searchable":True,"Class":"ADVANCE_AMOUNT"},{"Name":"ORD_DATE","Editable":True,"Searchable":True,"Class":"ORD_DATE"},{"Name":"CUST_CODE","Editable":True,"Searchable":True,"Class":"CUST_CODE"},{"Name":"AGENT_CODE","Editable":True,"Searchable":True,"Class":"AGENT_CODE"},{"Name":"ORD_DESCRIPTION","Editable":True,"Searchable":True,"Class":"ORD_DESCRIPTION"},{"Name":"ID","Editable":False,"Searchable":False,"Class":"ID"}],
        "Name":"TableNameHere","Insertable":True,"Deletable":True}
    return HttpResponse(json.dumps(msgl))


def tabledata(request):
    #time.sleep(5)
    msgl = {
  "data": [

    {
      "id": "2",
      "Column1": "Garrett Winters",
      "Column_2": "Accountant",
      "Column_3": 3,
      "Column_4": "2011-07-25",
      "Column_5": "2011-12-25",
      "Column_6": "8422"
    },
    {
      "id": "20",
      "Column1": "Garrett Winters again west",
      "Column_2": "Accountant",
      "Column_3": 3,
      "Column_4": "2011-07-25",
      "Column_5": "2011-12-25",
      "Column_6": "8422"
    },

      {
          "id": "21",
          "Column1": "Garrett Winters again west",
          "Column_2": "Accountant",
          "Column_3": 3,
          "Column_4": "2011-07-25",
          "Column_5": "2011-12-25",
          "Column_6": "8422"
      },
{
      "id": "22",
      "Column1": "Garrett Winters again west",
      "Column_2": "Accountant",
      "Column_3": 3,
      "Column_4": "2011-07-25",
      "Column_5": "2011-12-25",
      "Column_6": "8422"
    },

      {
          "id": "23",
          "Column1": "Garrett Winters again west",
          "Column_2": "Accountant",
          "Column_3": 3,
          "Column_4": "2011-07-25",
          "Column_5": "2011-12-25",
          "Column_6": "8422"
      },

      {
          "id": "24",
          "Column1": "Garrett Winters again west",
          "Column_2": "Accountant",
          "Column_3": 3,
          "Column_4": "2011-07-25",
          "Column_5": "2011-12-25",
          "Column_6": "8422"
      },

      {
          "id": "25",
          "Column1": "Garrett Winters again west",
          "Column_2": "Accountant",
          "Column_3": 3,
          "Column_4": "2011-07-25",
          "Column_5": "2011-12-25",
          "Column_6": "8422"
      },

      {
          "id": "26",
          "Column1": "Garrett Winters again west",
          "Column_2": "Accountant",
          "Column_3": 3,
          "Column_4": "2011-07-25",
          "Column_5": "2011-12-25",
          "Column_6": "8422"
      },

      {
          "id": "27",
          "Column1": "Garrett Winters again west",
          "Column_2": "Accountant",
          "Column_3": 3,
          "Column_4": "2011-07-25",
          "Column_5": "2011-12-25",
          "Column_6": "8422"
      },

      {
          "id": "28",
          "Column1": "Garrett Winters again west",
          "Column_2": "Accountant",
          "Column_3": 3,
          "Column_4": "2011-07-25",
          "Column_5": "2011-12-25",
          "Column_6": "8422"
      },

      {
          "id": "29",
          "Column1": "Garrett Winters again west",
          "Column_2": "Accountant",
          "Column_3": 3,
          "Column_4": "2011-07-25",
          "Column_5": "2011-12-25",
          "Column_6": "8422"
      },

      {
          "id": "30",
          "Column1": "Garrett Winters again west",
          "Column_2": "Accountant",
          "Column_3": 3,
          "Column_4": "2011-07-25",
          "Column_5": "2011-12-25",
          "Column_6": "8422"
      },
    {
      "id": "6",
      "Column1": "Garrett Winters3",
      "Column_2": "Accountantw",
      "Column_3": 8,
      "Column_4": "2011-12-25",
      "Column_5": "2011-12-25",
      "Column_6": "0422"
    }
  ]
    }
    return HttpResponse(json.dumps(msgl))

def createnewlist(request):
    test_dict = dict(request.POST)
    print(test_dict)
    search_key = len([x for x in list(test_dict.keys()) if 'Id' in x])
    cols = []
    for search_key in list(range(0,search_key)):
      res = dict(filter(lambda item: str(search_key) in item[0], test_dict.items()))
      r = {x.replace('_'+str(search_key), ''): y if (len(y) > 1) else y[0] for x, y in res.items()}
      cols.append(r)


    ListDef = {
    "action":"create",
    "data":{
        "Listname":test_dict['Listname'][0],
        "Listdescription": test_dict["Listdescription"][0],
        "columns":cols
        }
    }

    #file = request.FILES['files'].file
    #return HttpResponse(io.TextIOWrapper(file))
    url = 'http://localhost:8000/api/List'
    requests.post(url,json=ListDef)
    return HttpResponseRedirect(reverse('SolsHome'))