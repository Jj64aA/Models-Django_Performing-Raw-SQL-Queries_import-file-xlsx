from django.db import models

# Create your models here.

class creance(models.Model):
    ref=models.CharField(max_length=15,null=False)
    montant=models.FloatField(null=False)


#----------------------------------------------------
class commune(models.Model):
    come_code = models.CharField(max_length=5,null=False)
    ad_code =  models.CharField(max_length=3,null=False)
    


#----------------------------------------------------
class function1(models.Model):
    ref_f1 = models.CharField(max_length=15,null=False)
    montant_f1 = models.FloatField(null=False)
    ad_code_f1 = models.CharField(max_length=3,null=False)

class function2(models.Model):
    ref_f2 = models.CharField(max_length=15,null=False)
    montant_f2 = models.FloatField(null=False)
    Nb_Fact = models.IntegerField(null=False)
    ad_code_f2 = models.CharField(max_length=3,null=False)

class function3(models.Model):
    ad_code_f3 = models.CharField(max_length=3,null=False)
    Nb_Fact_all = models.IntegerField(null=False)
    Nb = models.IntegerField(null=False)
    montant_f3 = models.FloatField(null=False)