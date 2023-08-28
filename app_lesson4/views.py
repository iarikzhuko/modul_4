from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .models import Advertisment
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required

def index(request):
    advertisements = Advertisment.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'app_lesson4/index.html', context)


def top_sellers(request):
    return render(request, 'app_lesson4/top-sellers.html')

@login_required(login_url= reverse_lazy('login'))
def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement = form.save(commit=False)
            new_advertisement.user = request.user
            new_advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'app_lesson4/advertisement-post.html', context)

