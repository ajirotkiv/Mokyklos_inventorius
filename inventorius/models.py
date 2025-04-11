from django.db import models

class Kategorija(models.Model):
    pavadinimas = models.CharField(max_length=100)

    def __str__(self):
        return self.pavadinimas

class Vieta(models.Model):
    pavadinimas = models.CharField(max_length=100)

    def __str__(self):
        return self.pavadinimas

class Inventorius(models.Model):
    TURTO_TIPAS = (
        ('ILG', 'Ilgalaikis turtas'),
        ('TRU', 'Trumpalaikis turtas'),
    )
    pavadinimas = models.CharField(max_length=100, null=False)
    serijinis_numeris = models.CharField(max_length=100, unique=True)
    inventorinis_numeris = models.CharField(max_length=100)
    kaina = models.DecimalField(max_digits=10, decimal_places=2)
    vieta = models.ForeignKey(Vieta, on_delete=models.CASCADE)
    busena = models.CharField(max_length=50, choices=[
        ('Naudojamas', 'Naudojamas'),
        ('Sandeliuojamas', 'Sandeliuojamas'),
        ('Remontuojamas', 'Remontuojamas'),
    ], default='Naudojamas')
    ivedimo_data = models.DateField(verbose_name="Įvedimo į eksploataciją data")
    kategorija = models.ForeignKey(Kategorija, on_delete=models.CASCADE)
    turto_tipas = models.CharField(max_length=3, choices=TURTO_TIPAS, null=False)

    def __str__(self):
        return f"{self.pavadinimas} - {self.turto_tipas} - {self.inventorinis_numeris}"