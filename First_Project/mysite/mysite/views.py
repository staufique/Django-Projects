from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # data={
    #     'title':'new Home ',
    #     'bdata':'Welcome to my site (:',
    #     'clist': ['php','java','python','c++'],
    #     'numbers':[10,20,30,40,50],
    #     'student':[
    #         {'name':'pradeep','phone':6958865402},
    #         {'name':'shaikh','phone':9594829866},
    #         {'name':'Taufique','phone':856985654}
    #     ]
    # }
    return render(request,"index.html")

def aboutUs(request):
    return HttpResponse("Wlcome to mysite")

def course(request):
    return HttpResponse("Courses")

def courseDetails(request,courseD):
    return HttpResponse(courseD)