from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Time , Escolha
from .forms import FormTime, FormEscolha

def lista_jogos(request):
	escolhas = Escolha.objects.all()
	return render(request , 'votacoes/lista_jogos.html', {'escolhas': escolhas})

def jogo(request, pk):
    escolha = get_object_or_404(Escolha, pk=pk)
    return render(request, 'votacoes/jogo.html', {'escolha': escolha})

def new_votacao(request):
	if request.method == "POST":
		form = FormEscolha(request.POST)
		if form.is_valid():
			escolha = form.save(commit=False)
			escolha.author = request.user
			escolha.data_criacao = timezone.now()
			escolha.save()
			return redirect('jogos')
			
	else:
		form = FormEscolha()
	return render(request, 'votacoes/new_escolha.html', {'form':form})

def new_time(request):
	if request.method == "POST":
		form = FormTime(request.POST)
		if form.is_valid():
			escolha = form.save(commit=False)
			escolha.author = request.user
			escolha.data_criacao = timezone.now()
			escolha.save()
			return redirect('jogos')
			
	else:
		form = FormTime()
	return render(request, 'votacoes/new_time.html', {'form':form})

