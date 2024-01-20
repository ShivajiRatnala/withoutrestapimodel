from django.shortcuts import render
from apiapp2.models import Student
from django.views.generic import View
from django.http import HttpResponse
import json
# Create your views here.

# without using mixins
class student_data(View):
    def get(self,request,*args,**kwargs):
        student=Student.objects.get(id=1)
        emp_data={
            'name':student.name,
            'cls' : student.cls,
            'school':student.school,
            'Address':student.Address,
        }
        json_data=json.dumps(emp_data)
        return HttpResponse(json_data,content_type='application/json')


class student_data2(View):
    def get(self,request,id,*args,**kwargs):
        student = Student.objects.get(id=id)
        emp_data = {
            'name': student.name,
            'cls': student.cls,
            'school': student.school,
            'Address': student.Address,
        }
        json_data = json.dumps(emp_data)
        return HttpResponse(json_data, content_type='application/json')

from django.core.serializers import serialize

class student_data4(View):
    def get(self,request,*args,**kwargs):
        qs = Student.objects.all()
        json_data=serialize('json',qs)
        pdict=json.loads(json_data)
        json_data=json.dumps(pdict)
        return HttpResponse(json_data,content_type='application/json')

# by using mixins
from apiapp2.mixins import Mixins

class StudentData5(Mixins,View):
    def get(self,request,*args,**kwargs):
        qs = Student.objects.all()
        return self.serilize(qs)


from apiapp2.forms import StudentForm
# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt,name='dispatch')
class StudentData6(Mixins,View):
    def post(self,request,*args,**kwargs):
        data = request.body
        empdata = json.loads(data)
        form = StudentForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg':'Resource created successfully'})
            return self.serilize(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.serilize(json_data,status=404)





