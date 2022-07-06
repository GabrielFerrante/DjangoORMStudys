from django.contrib.auth import get_user_model

from django.db import models

# Create your models here.

class Chassi(models.Model):

    numero = models.CharField('Chassi', max_length=32, help_text='Máximo 32 caracteres')

    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'

    
    def __str__(self):
        return self.numero


class Montadora(models.Model):
    nome = models.CharField('Nome', max_length=50)

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'

    
    def __str__(self):
        return self.nome


def set_default_montadora():
    return Montadora.objects.get_or_create(nome='Padrão')[0] # retorna uma tupla (objeto, boolean)

class Carro(models.Model):
    """
    CADA CARRO SÓ PODE SE RELACIONAR COM 1 CHASSI
    E CADA CHASSI SÓ PODE SE RELACIONAR COM 1 CARRO
    1-1
    """
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
    modelo = models.CharField('Modelo', max_length=50, help_text='Máximo 50 caracteres')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

    """
    UM CARRO PODE SE PERTENCER SOMENTE A 1 MONTADORA
    MAS UMA MONTADORA PODE TER FABRICADO VÁRIOS CARROS
    0-N
    """

    #O CARRO N É DELETADO E A MONTADORA SETADA É A COM ID 1
    #montadora = models.ForeignKey(Montadora, on_delete=models.SET_DEFAULT, default=1)

    #MESMO SEM MONTADORA, A MONTADORA PADRÃO VAI SER ATRIBUIDO AOS CARROS
    montadora = models.ForeignKey(Montadora, on_delete=models.SET(set_default_montadora))

    #montadora = models.ForeignKey(Montadora, on_delete=models.CASCADE)


    """
    UM CARRO PODE SER DIRIGIDO POR VÁRIOS MOTORISTAS
    UM MOTORISTA PODE DIRIGIR COM VÁRIOS CARROS
    N-N
    """
    motoristas = models.ManyToManyField(get_user_model())


    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    
    def __str__(self):
        return f'{self.modelo} {self.montadora}'

    