from django.db import models
from django.conf import settings

class Topico(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=10000, blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey('auth.User', blank=True, null=True, on_delete=models.CASCADE)
    
    

    def __str__(self):
        return  self.titulo



class Post(models.Model):
    titulo = models.CharField(max_length=60, verbose_name=("Titulo"))
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey('auth.User', blank=True, null=True, related_name="%(class)s_posts", on_delete=models.CASCADE)
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    body = models.TextField(max_length=10000)

    def save(self, *args, **kwargs):
        self.topico.user_lst = str(self.autor.id)
        self.topico.save()
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo
    #short.allow_tags = True

class Coment(models.Model):

	autor = models.ForeignKey('auth.User', blank=True, null=True , on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	body = models.TextField(max_length=10000)

	