from django.db import models


class Time(models.Model):

    time = models.CharField(max_length=200)

    def __str__(self):
        return self.time


class Escolha(models.Model):
    Equipe_da_casa = models.OneToOneField("Time", on_delete = models.CASCADE, related_name = "casa", default = "10")
    votes = models.IntegerField(default=0)
    Equipe_de_fora = models.OneToOneField("Time", on_delete = models.CASCADE, related_name = "fora", default = "10")
    votes2 = models.IntegerField(default=0)
    Partida = models.CharField(max_length=55, default = "Partida")

    def __str__(self):
        return self.Partida	

		

		
	
		

