import requests
from bs4 import BeautifulSoup
import json
import re

# Lâminas conhecidas do UFRJ
laminas_ufrj = [
    {
        "id": 1,
        "nome": "Traqueia e Esôfago",
        "aumento": "10x",
        "url": "http://www.histo.ufrj.br/LIB/Lamina%2015%20Traqueia%20e%20Esofago%2010x/Lamina%2015.htm",
        "descricao": "Visão geral da traqueia e esôfago"
    },
    {
        "id": 2,
        "nome": "Pulmão",
        "aumento": "10x",
        "url": "http://www.histo.ufrj.br/LIB/",
        "descricao": "Tecido pulmonar"
    },
    {
        "id": 3,
        "nome": "Estômago",
        "aumento": "10x",
        "url": "http://www.histo.ufrj.br/LIB/",
        "descricao": "Camadas do estômago"
    },
    {
        "id": 4,
        "nome": "Intestino Delgado",
        "aumento": "10x",
        "url": "http://www.histo.ufrj.br/LIB/",
        "descricao": "Vilosidades intestinais"
    },
    {
        "id": 5,
        "nome": "Fígado",
        "aumento": "10x",
        "url": "http://www.histo.ufrj.br/LIB/",
        "descricao": "Lóbulo hepático"
    }
]

# Salvar como JSON para usar no HTML
with open('laminas_ufrj.json', 'w', encoding='utf-8') as f:
    json.dump(laminas_ufrj, f, indent=2, ensure_ascii=False)

print("✅ Lâminas UFRJ catalogadas!")
print(f"📊 Total: {len(laminas_ufrj)} lâminas")
print("💾 Salvo em: laminas_ufrj.json")
