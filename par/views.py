from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Album, Information,Contact

def home(request):
    latest = Album.objects.all().order_by('-time')
    info = Information.objects.all()
    params = {'latests':latest[0:3],'infos':info}
    return render(request, 'home.html',params)

def music(request):
    info = Information.objects.all()
    music = Album.objects.all().order_by('-time')
    params = {'title':'Music','infos':info,'musics':music}
    return render(request, 'music.html',params)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        con = Contact(name=name, email=email, message=message)
        con.save()
        messages.success(request, "Message successfully sent.")
        return redirect('home')
    info = Information.objects.all()
    params = {'title':'Contact','infos':info}
    return render(request, 'contact.html',params)

