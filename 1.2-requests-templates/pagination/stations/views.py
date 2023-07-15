from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator

from pagination.settings import BUS_STATION_CSV
from csv import DictReader

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(BUS_STATION_CSV, encoding='utf-8') as f:
        station = []
        for row in DictReader(f):
            station.append(row)
        paginator = Paginator(station, 10)
        page_number = int(request.GET.get('page', 1))
        page = paginator.get_page(page_number)
    context = {
         'bus_stations': page,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
