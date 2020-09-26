from django.shortcuts import render
from django.http import HttpResponse
from .models import BaseImage

def index(request):
    return HttpResponse("You are at the image processing app index.")

def image_detail(request, image_id):
    context = {
        'base_image': BaseImage.objects.get(pk=image_id)
        }
    return render(request, 'imageprocessing/image_detail.html', context)
