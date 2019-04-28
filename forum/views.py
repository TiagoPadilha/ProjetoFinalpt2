from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Topico, Post, Coment
from .forms import FormTopico, FormPost, FormComent

def lista_topicos(request):
	topico = Topico.objects.all()
	return render(request , 'forum/lista_topicos.html', {'topicos': topico})

def new_topico(request):
    if request.method == "POST":
        form = FormTopico(request.POST)
        if form.is_valid():
            topico = form.save(commit=False)
            topico.autor = request.user
            topico.data_criacao = timezone.now()
            topico.save()
            return redirect('topicos')
    else:
        form = FormTopico()
    return render(request, 'forum/new_topico.html', {'form': form})

def new_post(request):
    if request.method == "POST":
        form = FormPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.data_criacao = timezone.now()
            post.save()
            return redirect('topicos')
    else:
        form = FormPost()
    return render(request, 'forum/new_post.html', {'form': form})

def new_coment(request):
    if request.method == "POST":
        form = FormComent(request.POST)
        if form.is_valid():
            coment = form.save(commit=False)
            coment.autor = request.user
            coment.data_criacao = timezone.now()
            coment.save()
            return redirect('topicos')
    else:
        form = FormComent()
    return render(request, 'forum/new_coment.html', {'form': form})

def post(request, pk):
	topico = Topico.objects.all().get()
#	topico = Topico.objects.get(pk = pk)
	post = Post.objects.all().get()
#	post = Post.objects.get(pk = pk)


	posts = Post.objects.filter(topico = topico)

	coments = Coment.objects.filter(post = post)

	context = {
	'posts':posts,
	'coments': coments
	}

	return render(request, 'forum/post.html', context)


