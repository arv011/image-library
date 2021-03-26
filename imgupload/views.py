from django.shortcuts import render,redirect
from .forms import imgform
from .models import Pic


# Create your views here.

def Imageuploader(request):
    form = imgform()
    if request.method == 'POST':
        form = imgform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    
    images = Pic.objects.all()
    
    context = {'form': form, 'images': images}

    if (request.method == 'POST') and ('delete' in request.POST) :
        value = request.POST.get('delete')
        img = Pic.objects.get(id=value)
        img.delete()
        return redirect('/')
        
    return render(request, 'home.html', context)
