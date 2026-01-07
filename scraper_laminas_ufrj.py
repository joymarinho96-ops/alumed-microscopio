import requests
from bs4 import BeautifulSoup
import json
import os
from urllib.parse import urljoin

# Create folder
os.makedirs('imagens_laminas', exist_ok=True)

# Try to scrape UFRJ site
print("🔬 Tentando pegar lâminas do UFRJ...")

urls_to_try = [
    "http://www.histo.ufrj.br/LIB/banco.htm",
    "https://www.histo.ufrj.br/LIB/banco.htm",
    "http://www.histo.ufrj.br/LIB/",
]

laminas = []
found = False

for url in urls_to_try:
    try:
        print(f"Tentando: {url}")
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Procurar por links de imagens
            images = soup.find_all('img')
            links = soup.find_all('a', href=True)
            
            print(f"  Encontradas {len(images)} imagens e {len(links)} links")
            
            for img in images[:10]:  # Primeiras 10
                src = img.get('src')
                alt = img.get('alt', 'Lâmina')
                if src and ('histo' in src.lower() or '.jpg' in src.lower() or '.png' in src.lower()):
                    full_url = urljoin(url, src)
                    laminas.append({
                        "nome": alt[:50],
                        "url": full_url
                    })
                    print(f"    ✓ {alt[:30]}")
                    found = True
            
            if found:
                break
    except Exception as e:
        print(f"  ✗ Erro: {str(e)[:50]}")

# Se não encontrou no UFRJ, usar as do Leeds que já temos
if not found or len(laminas) == 0:
    print("\n⚠️ UFRJ indisponível, usando imagens locais do Leeds...")
    
    # Gerar lista das imagens locais que já temos
    import glob
    
    local_images = sorted(glob.glob('imagens_laminas/lamina_leeds_*.png')) + sorted(glob.glob('imagens_laminas/lamina_leeds_*.jpg'))
    
    descriptions = {
        '001': 'Estômago - Diagrama',
        '002': 'Estômago - Glândulas gástricas',
        '003': 'Intestino Delgado - Pregas circulares',
        '004': 'Intestino Delgado - Vilosidades',
        '005': 'Intestino Delgado - Enterócito (TEM)',
        '006': 'Intestino Delgado - Epitélio',
        '007': 'Fígado - Fluxo sangüíneo',
        '008': 'Fígado - Espaço de Disse',
        '009': 'Vesícula Biliar',
        '010': 'Apêndice',
        '011': 'Plaquetas',
        '012': 'Cabelo',
        '013': 'Artérias - Diagrama',
        '014': 'Artérias (TEM)',
        '015': 'Sistema vascular',
        '016': 'Capilares - Diagrama',
        '017': 'Capilares (EM)',
        '018': 'Capilares (foto)',
        '019': 'Glomérulo renal',
        '020': 'Capilares fenestrados',
        '021': 'Capilares fenestrados (EM)',
        '022': 'Capilares descontínuos',
    }
    
    for img_path in local_images:
        filename = os.path.basename(img_path)
        # Extract number from filename
        num = filename.split('_')[-1].split('.')[0]
        desc = descriptions.get(num, filename)
        laminas.append({
            "nome": desc,
            "url": img_path
        })

print(f"\n✅ Total de lâminas: {len(laminas)}")

# Save as JSON for the frontend
data = {
    "source": "University of Leeds",
    "total": len(laminas),
    "laminas": laminas
}

with open('laminas_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("💾 Dados salvos em laminas_data.json")
