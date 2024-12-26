from django.shortcuts import render
from django.http import HttpResponse



def home(request):

    return render(request, 'home.html')

def intro_page(request):
    print("Intro Page")
    return render(request, 'intro.html')
def overview(request):
    return render(request, 'quizapp/intro.html') 

