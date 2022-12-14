from django.shortcuts import render, redirect
from .models import Noticia
from services.scrapper import G1Scrapper, OGloboScrapper

# Create your views here.

def index(request):
    context = {}

    query = request.GET.get('q')
    print(query)
    context['query'] = ''

    if query:
        context['dataset'] = Noticia.objects.filter(title__icontains=query) | Noticia.objects.filter(body__icontains=query)
        context['query'] = query
    else:
        context['dataset'] = Noticia.objects.all()

    return render(request, 'index.html', context)

def scrapper(request):
    try:
        g1 = G1Scrapper()
        news = list(g1.parse())

        for item in news:
            # check if news already exists by title
            if not Noticia.objects.filter(title=item['title']).exists():
                Noticia.objects.create(
                    title=item['title'],
                    body=item['description'],
                    link=item['link'],
                    image=item['image']
                )
    except:
        pass

    try:
        oglobo = OGloboScrapper()
        news = list(oglobo.parse())

        for item in news:
            # check if news already exists by title
            if not Noticia.objects.filter(title=item['title']).exists():
                Noticia.objects.create(
                    title=item['title'],
                    body=item['description'],
                    link=item['link'],
                    image=item['image'],
                )
    except:
        pass

    return redirect('/')