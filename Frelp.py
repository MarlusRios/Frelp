import os
from google import genai
from FastAPI import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class Resposta(BaseModel):
    resposta: str

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

while True:
    print()
    user_input = input("Você: ")
    if user_input.lower() in ["sair", "exit", "quit"]:
        print("Encerrando a conversa. Até mais!")
        break

    resposta = chat.send_message(user_input)
    print("Frelp: " + resposta.text)
    print()