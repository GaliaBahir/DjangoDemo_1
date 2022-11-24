from django.shortcuts import render

#import django.http as Http

def counter(request):
    #return(Http.HttpResponse(200))
    return render(request, 'counter.html')