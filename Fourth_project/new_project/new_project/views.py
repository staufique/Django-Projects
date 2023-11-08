from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import userForm

def aboutus(request):
    return HttpResponse("<b>Welcome to Wscubetech</b>")

def courses(request):
    return HttpResponse("Welcome to Wscubetech course")

#creating dynamic urls
def courseDetails(request,courseid):
    return HttpResponse(courseid)

def home(request):
    data={
        'title':'Home Page',
        'bdata':'Welcome to django python',
        'clist':['python','php','django','java'],
        'numbers':[10,20,30,40,50],
        'student_details':[
            {'name':'Taufique','mobile':994829866},
            {'name':'Shaikh','mobile':865243898}
        ]
    }
    return render(request,'index.html',data)

def submit(request):
    try:
        if request.method=='POST':
            c1=int(request.POST.get('num6'))
            c2=int(request.POST.get('num2'))
            ans=c1+c2
            data={
                'n1':c1,
                'n2':c2,
                'output':ans
            }
            return HttpResponse(ans)
    except:
        pass
    return HttpResponse(request,'submit-form')

def red(request):
    if request.method=='GET':
        output=request.GET.get('output')
    return render(request,'redirect.html',{'output':output})

def form(request):
    '''these codes are for get method'''
    # ans=0
    # try:
        # n1=int(request.GET['num1'])
        # n2=int(request.GET['num2'])
        # n1=int(request.GET.get('num1'))
        # n2=int(request.GET.get('num2'))
        # ans=n1+n2
    # except:
    #     pass
    # return render(request,'userform.html',{'output':ans})

    '''these codes are for post method'''
    ans=0

    fn=userForm()
    data={'form':fn}
    try:
        if request.method=='POST':
            p1=int(request.POST.get('num1'))
            p2=int(request.POST.get('num2'))
            ans=p1+p2
            data={
                'form':fn,
                'output':ans
            }
            url='/redirect-page/?output={}'.format(ans)
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,'userform.html',data)

# def red(request):
#     return render(request,'redirect.html')



def calculator(request):
    c=''
    try:
        if request.method=='POST':
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=='+':
                c=n1+n2
            elif opr=='-':
                c=n1-n2
            elif opr=='*':
                c=n1*n2
            elif opr=='/':
                c=n1/n2
            
    except:
        c='invalid input is given'
    return render(request,'calculator.html',{'c':c,'n1':n1,'n2':n2})

def even_odd(request):
    c=''
    try:
        if request.method=='POST':
            if request.POST.get('num1')=='':
                return render(request,'even_odd.html',{'error':True})
            n1=eval(request.POST.get('num1'))
            if n1%2==0:
                c='Given Number is even'
            else:
                c='Given Number is odd'

            data={'c':c,'n1':n1}
            return render(request,'even_odd.html',data)
    except:
        pass 

    return render(request,'even_odd.html',{'c':c})

def marksheet(request):
    total=''
    per=''
    div=''
    try:
        # if request.POST.get('sub1')=='':
        #     return render(request,'marksheet.html',{'error':True})
        # elif request.POST.get('sub2')=='':
        #     return render(request,'marksheet.html',{'error':True})
        # elif request.POST.get('sub3')=='':
        #     return render(request,'marksheet.html',{'error':True})
        # elif request.POST.get('sub4')=='':
        #     return render(request,'marksheet.html',{'error':True})
        # elif request.POST.get('sub5')=='':
        #     return render(request,'marksheet.html',{'error':True})
        # if request.method=='POST':
            n1=eval(request.POST.get('sub1'))
            n2=eval(request.POST.get('sub2'))
            n3=eval(request.POST.get('sub3'))
            n4=eval(request.POST.get('sub4'))
            n5=eval(request.POST.get('sub5'))
            total=(n1+n2+n3+n4+n5)
            per=(total/500)*100
            
            if per>85:
                div='O Grade'
            elif per>75:
                div='A+ Grade'
            elif per>65:
                div='A Grade'
            elif per>55:
                div='B Grade'
            elif per>45:
                div='C Grade'
            elif per>35:
                div='D Grade'
            else:
                div='Failed'

            data={'total':total,'per':per,'div':div,'n1':n1,'n2':n2,'n3':n3,'n4':n4,'n5':n5}
            return render(request,'marksheet.html',data)
    except:
        pass
    return render(request,'marksheet.html')