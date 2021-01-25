from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def home(request):
    return render(request, "test.html")
def home2(request):
    return render(request, "home.html")

def tablemeta(request):
    msgl = {"Column":[
        {"Name":"ORD_NUM","Editable":False,"Searchable":True,"Class":"ORD_NUM"},{"Name":"ORD_AMOUNT","Editable":True,"Searchable":True,"Class":"ORD_AMOUNT"},{"Name":"ADVANCE_AMOUNT","Editable":True,"Searchable":True,"Class":"ADVANCE_AMOUNT"},{"Name":"ORD_DATE","Editable":True,"Searchable":True,"Class":"ORD_DATE"},{"Name":"CUST_CODE","Editable":True,"Searchable":True,"Class":"CUST_CODE"},{"Name":"AGENT_CODE","Editable":True,"Searchable":True,"Class":"AGENT_CODE"},{"Name":"ORD_DESCRIPTION","Editable":True,"Searchable":True,"Class":"ORD_DESCRIPTION"},{"Name":"ID","Editable":False,"Searchable":False,"Class":"ID"}],
        "Name":"TableNameHere","Insertable":True,"Deletable":True}
    return HttpResponse(json.dumps(msgl))


def tabledata(request):
    msgl = {"draw": 1, "recordsTotal": 34, "recordsFiltered": 34, "data": [
        {"ID": 1, "ORD_NUM": "200100", "ORD_AMOUNT": "1000", "ADVANCE_AMOUNT": "600",
         "ORD_DATE": "8/1/2008 12:00:00 AM", "CUST_CODE": "C00013", "AGENT_CODE": "A003  ", "ORD_DESCRIPTION": "TYU"},
        {"ID": 2, "ORD_NUM": "200100", "ORD_AMOUNT": "1000", "ADVANCE_AMOUNT": "600",
         "ORD_DATE": "8/1/2008 12:00:00 AM", "CUST_CODE": "C00013", "AGENT_CODE": "A003  ", "ORD_DESCRIPTION": "TYU"},
        {"ID": 3, "ORD_NUM": "200100", "ORD_AMOUNT": "1000", "ADVANCE_AMOUNT": "600",
         "ORD_DATE": "8/1/2008 12:00:00 AM", "CUST_CODE": "C00013", "AGENT_CODE": "A003  ", "ORD_DESCRIPTION": "TYU"},
        {"ID": 4, "ORD_NUM": "200100", "ORD_AMOUNT": "1000", "ADVANCE_AMOUNT": "600",
         "ORD_DATE": "8/1/2008 12:00:00 AM", "CUST_CODE": "C00013", "AGENT_CODE": "atyefduat asuedvuasv asuedvuasevd uatevdasuefvd autedvauefvd usedfvasevd uatefduafd auydfuafved autdayuedf autdfayued autdfay8efd audfaeyd acdaedfa dvawuedawvdufauoedfaefvduoafedfaetdfaeuodfaeuodf  ", "ORD_DESCRIPTION": "TYU"},
        {"ID": 5, "ORD_NUM": "200101", "ORD_AMOUNT": "3212", "ADVANCE_AMOUNT": "1000",
         "ORD_DATE": "7/15/2008 12:00:00 AM", "CUST_CODE": "C00001", "AGENT_CODE": "A008  ", "ORD_DESCRIPTION": "TYU"}]}
    return HttpResponse(json.dumps(msgl))

def updatetabledata(request):
    print(request['GET'])
    return HttpResponse('ok')