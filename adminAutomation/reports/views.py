from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from django.http import HttpResponse
import pandas as pd
import json
import http.client 
from django.views.decorators.csrf import csrf_exempt

# import json and json_normalize to send json data to queryset
@csrf_exempt
def getReport(request):
    try:
        data= json.load(request)
        if data['unique_report_id'] == 1:
            user = Users.objects.values()[0:50]
            return downloadReport('Users',user)
        else:
            return HttpResponse('hi')
    except:
        print("An exception occurred")

def downloadReport(report_name,data):
    df = pd.DataFrame(data)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename='+report_name
    df.to_csv(path_or_buf=response)
    return HttpResponse('hi')



