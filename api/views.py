from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Emp
from .serializers import EmpSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def emp_api(request):
  if request.method =='GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            emp = Emp.objects.get(id=id)
            serializer=EmpSerializer(emp)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        emp=Emp.objects.all()
        serializer=EmpSerializer(emp , many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
  
  
  if request.method=='POST':
      json_data= request.body
      stream= io.BytesIO(json_data)
      pythondata= JSONParser().parse(stream)
      serializer=EmpSerializer(data=pythondata)
      if serializer.is_valid():
          serializer.save()
          res={'msg': 'Data is created'}
          json_data=JSONRenderer().render(res)
          return HttpResponse(json_data, content_type='application/json')
      json_data=JSONRenderer().render(serializer.errors)
      return HttpResponse(json_data, content_type='application/json')
  
  if request.method=='PUT':     
    json_data = request.body
    stream = io.BytesIO(json_data)
    pythondata = JSONParser().parse(stream)
    id = pythondata.get('id')
    print(id)
    emp = Emp.objects.get(id=id)
    serializer = EmpSerializer(emp, data=pythondata)
    if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data updated!!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type='application/json')
  
  if request.method =='DELETE':
    
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        try:
            emp = Emp.objects.get(id=id)
            emp.delete()
            res = {'msg': 'Data Deleted!!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        except Emp.DoesNotExist:
            res = {'msg': 'Student with the given ID does not exist'}
            json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')

      

      
      




