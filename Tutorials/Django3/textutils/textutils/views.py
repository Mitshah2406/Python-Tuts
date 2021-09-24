from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyze(request):
    djtext = request.POST.get('text', 'default')

    # getting the value of checkbox:
    removepunc = request.POST.get('check', 'off')
    upper_case = request.POST.get('uppercase', 'off')
    new_line_remover = request.POST.get('newlineremover', 'off')
    extra_space_remover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # checking checkbox is on and performing the operation
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~='''
        analyzed = " "
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations From Entered Text',
                  'analyzed_text': analyzed}
        djtext = analyzed

    if upper_case == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Transform Text To UpperCase',
                  'analyzed_text': analyzed}
        djtext = analyzed

    if new_line_remover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Lines',
                  'analyzed_text': analyzed}
        djtext = analyzed

    if extra_space_remover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Spaces',
                  'analyzed_text': analyzed}

    if removepunc != "on" and new_line_remover != "on" and extra_space_remover != "on" and upper_case != "on":
        return HttpResponse(''' <div style="margin: 20px;"><p style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;font-weight: 700;font-size: 1.5rem;text-transform: capitalize;">Error! You Have Not selected any Utlity Function to Perform Operation.</p><a href="/" style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;font-weight: 300;font-size: 1.2rem;text-decoration: none;background-color: #dc3545; color: white;padding: 9px;border-radius: 8px;" >Go Back!</a></div>''')

    return render(request, 'analyze.html', params)
