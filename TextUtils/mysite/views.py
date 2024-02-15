# Self-Created Python File

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    d= {'name': 'TextUtils', 'use': 'Text Editing Tool'} #creating a dictionary
    return render(request, 'index.html', d) #rendering the html page with data from the dictionary

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def analyze(request):
    yourtext=request.POST.get('text','default') #get the text from textbox
    removepunc=request.POST.get('removepunc','off') #get the checkbox value - removepunc
    fullcaps=request.POST.get('fullcaps','off')  #get the checkbox value - fullcaps
    newlineremover=request.POST.get('newlineremover','off')  #get the checkbox value - newlineremover
    spaceremover=request.POST.get('spaceremover','off')  #get the checkbox value - spaceremover
    extraspaceremover=request.POST.get('extraspaceremover','off')  #get the checkbox value - extraspaceremover
    countchars=request.POST.get('countchars','off')  #get the checkbox value - countchars
    
    print("yourtext:",yourtext)
    print("removepunc:",removepunc)
    print("fullcaps:",fullcaps)
    print("newlineremover:",newlineremover)
    print("spaceremover:",spaceremover)
    print("extraspaceremover:",extraspaceremover)
    print("countchars:",countchars)
    
    # Remove Punctuations
    punctuations= '''!()-[]{};:'"\,<>./?@#$%^&*_'''
    
    if removepunc=='on':
        analyzedtxt=""
        for char in yourtext:
            if char not in punctuations:
                analyzedtxt=analyzedtxt+char
        
        yourtext=analyzedtxt

    # Change to Uppercase
    if fullcaps=='on':
        analyzedtxt=""
        for char in yourtext:
            analyzedtxt=analyzedtxt + char.upper() #converting each character to uppercase

        yourtext=analyzedtxt
    
    # Remove Newlines
    if newlineremover=='on':
        analyzedtxt=""
        for char in yourtext:
            if char!="\n" and char!="\r":
                analyzedtxt = analyzedtxt + char

        yourtext=analyzedtxt
    
    # Remove Spaces
    if spaceremover=='on':
        analyzedtxt=""
        for char in yourtext:
            if char!=" ":
                analyzedtxt = analyzedtxt + char

        yourtext=analyzedtxt
    
    # Remove Extra Spaces
    if extraspaceremover=='on':
        analyzedtxt=""
        for index, char in enumerate(yourtext):
            if not(yourtext[index]==" " and yourtext[index+1]==" "):
                analyzedtxt = analyzedtxt + char

        yourtext=analyzedtxt
    
    # Count Characters
    if countchars=='on':
        i=0
        for char in yourtext:
            i+=1
                
        yourtext += f"\nNumber of Characters: {i}"

    # Rendering Data to HTML
    analyzedtxt=yourtext
    params={'analyzed_text':analyzedtxt} #storing data to dictionary
    return render(request,'analyze.html',params) #rendering data

