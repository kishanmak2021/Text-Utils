from django.http import HttpResponse
from django.shortcuts import render




def index(request):
    
    params = {'name':'Parthiv' ,'place': 'Mars'}
    return render(request,'index.html',params)

def analyze(request):
    text = request.POST.get('text','default value')
    removepunc=request.POST.get('removepunc','off')
    uppercase=request.POST.get('uppercase','off')
    res=request.POST.get('res','off')
    rnl=request.POST.get('rnl','off')
    lowercase=request.POST.get('lowercase','off')

    punc='''!@#$%^&*()_+[]\|}{;',./?><:"`~-_=+'''
    
    analyzed=''
    def removep( str):
        analyzed=''
        for char in str:
                    if char not in punc:
                        analyzed = analyzed + char

        return analyzed
    
    def upca(str):
        analyzed=str.upper()
        return analyzed

    def resp(str):
        
        analyzed = ""
        for index, char in enumerate(text):
            try:
                if not(text[index] == " " and text[index+1]==" "):
                    analyzed = analyzed + char
                    a=analyzed
            except:
                analyzed=a


            
        return analyzed
    
    def lowercasef(str):
        analyzed=str.lower()
        return analyzed
    
    def rnlf(str):
        analyzed=''
        for char in str:
            if not( char == '\n' or char=='\r'):
                analyzed = analyzed+char
        return analyzed

        

            




     
    
    
    list=[]
    if removepunc == 'on':
        list.append('Remove Punctuation')
        analyzed= removep(text)
        params = {'purpose': list , 'analyzed_text': analyzed}
        text = analyzed

    if uppercase=='on':
       list.append('UPPER CASE')
      
       analyzed= upca(text)
       params = {'purpose': list, 'analyzed_text': analyzed}
       text = analyzed
    
    if lowercase=='on' :
       list.append('lowercase')
 
       analyzed= lowercasef(text)
       
       params = {'purpose': list, 'analyzed_text': analyzed}
       text = analyzed
    
    
    if rnl=='on':
       list.append('Remove New Lines')

       analyzed= rnlf(text)
       params = {'purpose': list, 'analyzed_text': analyzed}
       text = analyzed
    
    if res=='on':
        list.append('Remove Extra Spaces')
        analyzed=resp(text)

    purpose=''
    for p in list:
        purpose = p + ' , '+ purpose
    
    print(purpose)
    params = {'purpose': purpose, 'analyzed_text':analyzed}
    return render(request, 'analyze.html', params)