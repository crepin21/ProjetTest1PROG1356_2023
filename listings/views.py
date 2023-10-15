from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Etudiant
from listings.models import EnseignantPricipale

def hello(request):
    etudiant   = Etudiant.objects.all()
    enseignant = EnseignantPricipale.objects.all()
    return render(request,'listings/hello.html', {'etudiant': etudiant, 'enseignant': enseignant })  #etudiant en jaune utiliser comme etudiant.name...

