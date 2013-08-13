# coding: utf-8
import re
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from log.models import Event

def search(request):
    event_list = Event.objects.all().order_by('-devicereportedtime')[:1000]
    errors = []
    if 'q' not in request.GET:
        q = ""
    else:
        q = request.GET['q']
        if not q:
            errors.append('%юзернейм%, задай слово для поиска')
        elif len(q) > 10:
            errors.append('%юзернейм%, поиск слов меньше 10 символов')
        elif not re.match(r"\w",q):
            errors.append('%юзернейм%, поиск только английскими символами')
        else:
            event_list = Event.objects.filter(Q(fromhost__icontains=q) | Q(message__icontains=q)).order_by('-devicereportedtime')[:1000]
    paginator = Paginator(event_list, 25) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        events = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        events = paginator.page(paginator.num_pages)
    return render(request,'log/index.html', {'events':events, 'query':q, 'errors':errors})
#    return render(request,'log/index.html',{'events':events, 'errors':errors})
    

def index(request):
    events = Event.objects.all().order_by('-devicereportedtime')[:100]
    return render(request,'log/index.html', {'events':events})
