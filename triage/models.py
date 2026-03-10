from django.db import models

from django.db import models
 
class Triage(models.Model):
 
    age = models.IntegerField()
    
    symptom1 = models.CharField(max_length=100)
    symptom2 = models.CharField(max_length=100)
    symptom3 = models.CharField(max_length=100,blank=True) #Not mandatory
    description = models.CharField(max_length=500)
    duration = models.IntegerField(help_text='Duração em dias')
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Triagem {self.id} - {self.created_at}"
 
 
class AIanalyses(models.Model):
 
    triage = models.ForeignKey(
    Triage,
    on_delete=models.CASCADE,
    related_name='analise'
    )
    
    prompt = models.TextField()
    resposta = models.JSONField()
    
    model = models.CharField(max_length=50) #Gemini
    
    created_at = models.DateTimeField(auto_now_add=True)