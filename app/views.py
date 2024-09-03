from django.shortcuts import render
from .models import Music, Artist
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data = request.GET
    page = data.get('page', 1)
    musics = Music.objects.all()
    page_obj = Paginator(musics, 1)
    context = {
        "musics":page_obj.get_page(page),
    }
    return render(request, 'index.html', context=context)