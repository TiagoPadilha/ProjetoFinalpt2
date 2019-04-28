from django.shortcuts import render

from django.shortcuts import redirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Time , Escolha

def pagina_Inicial(request):
    
    return render(request, 'votacoes/paginaInicial.html', {})

def lista_jogos(request):
	escolhas = Escolha.objects.all()
	return render(request , 'votacoes/lista_jogos.html', {'escolhas': escolhas})

def jogo(request, pk):
    escolha = get_object_or_404(Escolha, pk=pk)
    return render(request, 'votacoes/jogo.html', {'escolha': escolha})