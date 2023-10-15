from django.contrib import admin

# Register your models here.
from listings.models import EnseignantPricipale, Etudiant

admin.site.register(Etudiant)
admin.site.register(EnseignantPricipale)

