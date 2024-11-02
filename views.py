from django.http import HttpResponse
from django.shortcuts import render
import string

def index(request):
  return render(request, 'index.html')


def analyze(request):
  
  djtext = request.POST.get('text', 'default')
  print(djtext)
  
  upper_convert = request.POST.get('upper_convert', 'off')
  
  
  
  Punctuation_remover = request.POST.get('Punctuation_remover', 'off')
  
  
  extra_space_remover = request.POST.get('extra_space_remover', 'off')
  
  
  character_counter = request.POST.get('character_counter', 'off')
  
  
  if upper_convert == 'on':
    val = ""
    for char in djtext:
      val = val + char.upper()
    params = {'purpose' : 'Converted to upper case :>', 'analyzed_text' : val}
    djtext = val
  
  
  if Punctuation_remover == 'on':
    
    typesofpunctuation = string.punctuation
    analyzed_text = ""
    for char in djtext:
      if char not in typesofpunctuation:
        analyzed_text = analyzed_text + char
    params = {'purpose' : 'Punctuation Removed', 'analyzed_text' : analyzed_text}
    djtext = analyzed_text
  
  if (extra_space_remover == 'on'):
    val1 = ""
    
    for index,char in enumerate(djtext):
      if djtext[index] == " " and djtext[index + 1] == " ":
        pass
      else:
        val1 = val1 + char
    params = {'purpose' : 'extra space is removed', 'analyzed_text' : val1}
    djtext = val1
  
  if (character_counter == 'on'):
    count = 0
    for char in djtext:
      count = count + 1
    params = {'purpose' : 'Number of characters present in Your Text is : ', 'analyzed_text' : count}
    djtext = count
  
  
  if (upper_convert == 'off' and Punctuation_remover == 'off' and extra_space_remover == 'off' and character_counter == 'off'):
    vaal = "Bro i Think You havn't selected any option!!"
    return render(request, 'analyze.html', {'purpose' : '','analyzed_text' : vaal})
  
  
  return render(request, 'analyze.html', params)