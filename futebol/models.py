from django.db import models


# Create your models here.
class Equipa(models.Model):
    equipa = models.CharField(max_length=50)
    codigo = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.equipa} ({self.codigo})'


class Encontro(models.Model):

    equipa1 = models.ForeignKey(
        Equipa,
        on_delete=models.CASCADE,
        related_name = 'equipas1'
        )

    equipa2 = models.ForeignKey(
        Equipa,
        on_delete=models.CASCADE,
        related_name = 'equipas2'
        )

    def __str__(self):
        return f'Jogo {self.pk}: Casa: {self.equipa1} - Visitante: {self.equipa2}'


class Bilhete(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    jogos = models.ManyToManyField(Encontro)

    def __str__(self):
        return f'{self.nome} ({self.idade})'

class Hora(models.Model):
    jogos = models.ManyToManyField(Encontro)
    horas = models.CharField(max_length=50)

    def __str__(self):
        return f'({self.horas})'
