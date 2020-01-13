#hound_77
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
      #this dictionary can be access in templates
    return render(request,'index.html',)
   # return HttpResponse(''' <button> <a href='http://127.0.0.1:8000/copy'>forward </a></button>''')
def analyze(request):
    #get the text
  yotext= (request.POST.get('text','default '))
  removepunc=(request.POST.get('removepunc','off'))
  fullcaps=(request.POST.get('fullcaps','off'))
  newlineremover=(request.POST.get('newlineremover','off'))
  spaceremover=(request.POST.get('spaceremover','off'))
  charcount=(request.POST.get('charcount','off'))
  if removepunc=="on":
      punctution='''.,;:?[]{}()&/' " \-@#$%^&*_!~'''
      analyzed=""
      for char in yotext:
        if char not in punctution:
            analyzed=analyzed+char
      params={'purpose':'remove punctution','analyzed_text':analyzed}
        #  analyze the text
      #return render(request, 'analyze.html',params)
  if(fullcaps=="on"):
      analyzed=""
      for char in yotext:                     #FOR ALL THIS FUNCTION TO RUN SIMULTANEOUSLY
                                              # WE WILL NOT RENDER THEM AT EACH JUNCTION
          analyzed=analyzed+ char.upper()     #WE WILL JUST analyze and take it to next condition
      params = {'purpose': 'CHANGED TO UPPERCASE', 'analyzed_text': analyzed}
      #  analyze the text
      yotext=analyzed
      #return render(request, 'analyze.html', params)   #GIVE OUTPUT
  if(newlineremover=="on"):
      analyzed=""
      for char in yotext:
          if char !="\n" and char !="\r":
            analyzed=analyzed+ char
      params = {'purpose': 'remove new line', 'analyzed_text': analyzed}
      #  analyze the text
      yotext = analyzed
      #return render(request, 'analyze.html', params)
  if(spaceremover=="on"):
      analyzed=""
      for index, char in enumerate(yotext):
          if yotext[index] ==" " and yotext[index+1]==" ":
              pass
          else:
            analyzed=analyzed+ char
      params = {'purpose': 'remove space', 'analyzed_text':analyzed }
      #  analyze the text
      yotext = analyzed
      #return render(request, 'analyze.html', params)
  if(charcount=="on"):
      analyzed=""
      for  char in (yotext):

            analyzed=len(yotext)
      params = {'purpose': 'character count', 'analyzed_text': len(yotext)}
      #  analyze the text
      yotext = analyzed
      #return render(request, 'analyze.html', params)
  if(removepunc!="on" and charcount!="on" and spaceremover!="on" and newlineremover!="on" and fullcaps!="on"):
      return HttpResponse("kuch kro bhi")
  return render(request, 'analyze.html', params)
#def wiki(request):
   # return HttpResponse("haaa haa sb pta h")
#def copy(request):
      #  return HttpResponse('''<h1>Capitalize First</h1><br><button type="button"><a href = "http://127.0.0.1:8000/">Go Back</a></button>''')
