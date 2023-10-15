from django.db import models

# Create your models here.

class EnseignantPricipale(models.Model):
    name = models.fields.CharField(max_length=50)
    age      = models.IntegerField(null=True)
    date_embauche = models.DateTimeField(auto_now=True, auto_now_add=False)
    email    = models.EmailField()
    matiere  = models.CharField(max_length=100)  #La matière que l'enseignant enseigne
    salaire  = models.DecimalField(max_digits=10, decimal_places=2)  #Salaire de l'enseignant
    def __str__(self):
     return f'{self.name}'


class Etudiant(models.Model):
    name     =models.fields.CharField(max_length=100)
    age      =models.fields.IntegerField(null=True)
    date     =models.DateTimeField(auto_now=True, auto_now_add=False)
    mail     =models.EmailField()
    moyenne  =models.FloatField()
    enseignant = models.ForeignKey(EnseignantPricipale, null=True, on_delete=models.SET_NULL) #Cle etrangere
    #Modifier la representation
    def __str__(self):
     return f'{self.name}'
    
