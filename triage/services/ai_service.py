import google.genai as genai
from django.conf import settings
import json
 
client = genai.Client(api_key='AIzaSyB3j0V_OMudq_7122WZwzSt3jSZvYzAPrE')
 
class GeminiService:

    def analise(self, triage):
 
        sintomas = [
        triage.symptom1,
        triage.symptom2,
        triage.symptom3,
        ]
 
        symptoms_text= "\n".join([s for s in sintomas if s])
 
        prompt = f"""
        Você é um assistente de triagem médica.
        
        Idade do paciente: {triage.age}
        Duração dos sintomas: {triage.duration} dias
        
        Sintomas:
        {symptoms_text}
        
        Descrição adicional:
        {triage.description}
        
        Retorne SOMENTE JSON no formato
        
        {{
        "risco": "baixo | moderado | alto",
        "possiveis_causas": [],
        "especialidades_recomendadas": [],
        "recomendacoes": ""
        }}
        
        Não escreva nada fora do JSON.
        """
        
        response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
        )
        
        text = response.text
        
        try:
            return json.loads(text)
        except:
            return {
            "erro": "resposta inválida",
            "raw": text
        }