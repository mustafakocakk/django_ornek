from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404
from .models import Futbolcu


# Create your views here.
def index_view(request):
    players=Futbolcu.objects.all().order_by('id')[14:24]

    return render(request, 'futbolcu/home.html', {'posts': players})
def player_detail(request,id):
    post = get_object_or_404(Futbolcu, id=id)
    context = {
        'post': post
    }
    return render(request, 'futbolcu/detail.html', context)
