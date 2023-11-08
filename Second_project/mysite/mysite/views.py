# I have created this file- Taufique
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newline = request.POST.get('newlineremover','off')
    spremv = request.POST.get('extraspacerem','off')
    charcount = request.POST.get('charcount','off')

    if removepunc == 'on':
        punctuations = ''' !()-[]{};:'"\,,../?@#$%^&*_~ '''
        analyze_txt=""
        for char in djtext:
            if char not in punctuations:
                analyze_txt=analyze_txt+char
        params={'purpose' : 'removed punctations', 'analyze_text':analyze_txt}
        djtext= analyze_txt

    if fullcaps == 'on':
        analyzed =''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose' : 'Upper Case letters', 'analyzed':analyzed}
        djtext=analyzed
    if newline == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'Removed new lines', 'analyzed': analyzed}
        djtext=analyzed

    if spremv == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == ' '  and djtext[index+1] == ' '):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Spaces removed', 'analyzed': analyzed}
        djtext=analyzed

    if charcount == 'on':
        analyzed = ''
        count = 0

        for char in djtext:
            count = count + 1
            analyzed = analyzed + char
        params = {'purpose': 'Counted character', 'count': count, 'analyzed': analyzed}
       

    if (removepunc != 'on' and fullcaps != 'on' and newline != 'on' and 
         spremv != 'on' and charcount != 'on'):
        return HttpResponse('Please check the box')

    return render(request, 'analyaze.html', params)

