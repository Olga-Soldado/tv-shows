  
from django.shortcuts import render,HttpResponse, redirect
# Create your views here.
from django.contrib import messages
from .models import Show

def index(request):
    context = {
        "programas": Show.objects.all()
    }
    return render(request, "informacion.html", context)

def new(request):
    return render(request, "crear.html")

def create(request):
    errors = Show.objects.show_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value, extra_tags=key)
        return redirect('/shows/new')
    else:
        Show.objects.create(
        title = request.POST['title'],
        tv_network = request.POST['tv_network'],
        release_date = request.POST['release_date'],
        desc = request.POST['desc'],
    )
    messages.success(request, 'Se creo un nuevo programa')
    return redirect("/shows")


def about(request, id):
    context = {
        "show": Show.objects.get(id=id)
    }
    return render(request, "about.html", context)

def edit(request, id):
    context = {
        "show": Show.objects.get(id=id)
    }
    return render(request, "editar.html", context)

def update(request, id):
    errors = Show.objects.edit_validators(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect(f'/shows/{id}/edit')
    else:
        updated = Show.objects.get(id=id)
        updated.title = request.POST['updated_title']
        updated.tv_network = request.POST['updated_tv_network']
        updated.release_date = request.POST['updated_release_date']
        updated.desc = request.POST['updated_desc']
        updated.save()
    messages.success(request,'Se actualizo correctamente. ')
    return redirect(f'/shows/{id}/edit')


def destroy(request, id):
    Show.objects.get(id=id).delete()
    messages.success(request,'Se elimino correctamente. ')
    return redirect('/shows')

def home(request):
    return redirect('/shows')