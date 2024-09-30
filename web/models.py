from django.db import models

# Create your models here
    
class BalkonTerasse(models.Model):
    image1 = models.ImageField(upload_to='balkon_terasa/', null=True, blank=True)    
    image2 = models.ImageField(upload_to='balkon_terasa/', null=True, blank=True)
    image3 = models.ImageField(upload_to='balkon_terasa/', null=True, blank=True)
    image4 = models.ImageField(upload_to='balkon_terasa/', null=True, blank=True)
    image5 = models.ImageField(upload_to='balkon_terasa/', null=True, blank=True)
    image6 = models.ImageField(upload_to='balkon_terasa/', null=True, blank=True)
    image7 = models.ImageField(upload_to='balkon_terasa/', null=True, blank=True)
    image8 = models.ImageField(upload_to='balkon_terasa/', null=True, blank=True)
    # Dodaj još slike ako je potrebno

class WC_Bad(models.Model):
    image1 = models.ImageField(upload_to='wc/', null=True, blank=True)    
    image2 = models.ImageField(upload_to='wc/', null=True, blank=True)
    image3 = models.ImageField(upload_to='wc/', null=True, blank=True)
    image4 = models.ImageField(upload_to='wc/', null=True, blank=True)
    image5 = models.ImageField(upload_to='wc/', null=True, blank=True)
    image6 = models.ImageField(upload_to='wc/', null=True, blank=True)
    image7 = models.ImageField(upload_to='wc/', null=True, blank=True)    
    image8 = models.ImageField(upload_to='wc/', null=True, blank=True)
    # Dodaj još slike ako je potrebno

class Küche(models.Model):
    image1 = models.ImageField(upload_to='kuhinja/', null=True, blank=True)    
    image2 = models.ImageField(upload_to='kuhinja/', null=True, blank=True)
    image3 = models.ImageField(upload_to='kuhinja/', null=True, blank=True)
    image4 = models.ImageField(upload_to='kuhinja/', null=True, blank=True)
    image5 = models.ImageField(upload_to='kuhinja/', null=True, blank=True)
    image6 = models.ImageField(upload_to='kuhinja/', null=True, blank=True)
    # Dodaj još slike ako je potrebno

class Flur(models.Model):
    image1 = models.ImageField(upload_to='hodnik/', null=True, blank=True)    
    image2 = models.ImageField(upload_to='hodnik/', null=True, blank=True)
    image3 = models.ImageField(upload_to='hodnik/', null=True, blank=True)
    image4 = models.ImageField(upload_to='hodnik/', null=True, blank=True)
    image5 = models.ImageField(upload_to='hodnik/', null=True, blank=True)
    image6 = models.ImageField(upload_to='hodnik/', null=True, blank=True)
    # Dodaj još slike ako je potrebno

class Umbau(models.Model):
    image1 = models.ImageField(upload_to='umbau/', null=True, blank=True)    
    image2 = models.ImageField(upload_to='umbau/', null=True, blank=True)
    image3 = models.ImageField(upload_to='umbau/', null=True, blank=True)
    image4 = models.ImageField(upload_to='umbau/', null=True, blank=True)
    image5 = models.ImageField(upload_to='umbau/', null=True, blank=True)
    image6 = models.ImageField(upload_to='umbau/', null=True, blank=True)
    image7 = models.ImageField(upload_to='umbau/', null=True, blank=True)
    image8 = models.ImageField(upload_to='umbau/', null=True, blank=True)
    # Dodaj još slike ako je potrebno

