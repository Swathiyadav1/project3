from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
class GetInput(View):
    def get(self,request):
        return render(request,'getinput.html')
class PostInput(View):
    def get(self,request):
        return render(request,'postinput.html')
class Add(View):
    def get(self,request):
        x = int(request.GET['t1'])
        y = int(request.GET['t2'])
        op_type = request.GET["op"]
        z = None
        if op_type == 'add':
            z = x + y
        elif op_type == 'sub':
                z = x - y
        elif op_type == 'mul':
                z = x * y
        else:
                z = x / y
        return HttpResponse("the" + op_type + " is:" + str(z))
    def post(self,request):
        x = int(request.POST['t1'])
        y = int(request.POST['t2'])
        op_type = request.POST["op"]
        z = None
        if op_type == 'add':
            z = x + y
        elif op_type == 'sub':
                z = x - y
        elif op_type == 'mul':
                z = x * y
        else:
                z = x / y
        return HttpResponse("the" + op_type + " is:" + str(z))