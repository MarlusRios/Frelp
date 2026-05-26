import os
from google import genai
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

class request(BaseModel):
    problema: str

with open("personalidade.txt", 'r', encoding='utf-8') as file:
    personalidade = file.read()

app = FastAPI();

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
);

cliente = genai.Client();

chat = cliente.chats.create(
    model="gemini-2.5-flash",  # Uma dica: o 2.5-flash é o modelo padrão atual, super rápido para chat!
    config=genai.types.GenerateContentConfig(
        system_instruction=personalidade
    )
)

@app.post("/chat")
def apoioEmocional(apoio: request):
    pergunta = apoio.problema
    resposta = chat.send_message(pergunta)

    return {"resposta": resposta}