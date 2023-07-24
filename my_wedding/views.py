from django.shortcuts import render
from .models import Article


# Create your views here.

def homeView(request, template_name="wedding/pages/index.html"):
    # context permet à envoyer le code python vers le html
    # declaration du context
    context = {}
    bonjour = "bonjour tout le monde "

    # affectation de la cléf et de la valeur dans le context
    #           key     value
    #intance Object
    a1= Article("java","java description ")
    a2= Article("python","python description ")
    a3= Article("html","html description ")
    a4= Article("css","css description ")
    a5= Article("Poo","Poo description ")
    a6= Article("script","script description ")
    a7= Article("llo","llo description ")
    a8= Article("rest","rest description ")
    list_article =[a1,a2,a3,a4,a5,a6,a7,a8]
    for art in list_article:
        print(art.title)

    print(a1.title)
    context['article'] = a1
    context['name'] = bonjour

    return render(request, template_name, context)

def aboutView(request,template_name="wedding/pages/about.html"):

    #context permet à envoyer le code python vers le html
    #declaration du context
    context = {}
    bonjour = "bonjour tout le monde "

    #affectation de la cléf et de la valeur dans le context
    #           key     value
    context ['name'] = bonjour

    return render(request, template_name,context)
