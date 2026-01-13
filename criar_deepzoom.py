import sys
import os

# Adiciona o caminho do VIPS (caso o Windows tenha esquecido)
os.environ['PATH'] += r';C:\vips\bin'

import pyvips

def criar_deepzoom(imagem_entrada):
    nome_saida = os.path.splitext(imagem_entrada)[0] # Pega o nome sem extensão
    
    print(f"🔬 Processando {imagem_entrada} para Deep Zoom Ultra HD...")
    print("Isso pode levar alguns segundos...")

    try:
        # Carrega a imagem
        img = pyvips.Image.new_from_file(imagem_entrada, access="sequential")
        
        print(f"📊 Dimensões da imagem: {img.width} x {img.height} pixels")
        
        # O SEGREDINHO: dzsave (Deep Zoom Save)
        # Ele cria uma pasta com os quadradinhos e um arquivo .dzi
        img.dzsave(nome_saida, suffix=".jpg[Q=90]")
        
        print(f"✅ Sucesso! Criada a pasta '{nome_saida}_files' e o arquivo '{nome_saida}.dzi'")
        print(f"📂 A pasta contém tiles otimizados para zoom infinito!")
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        print("💡 Dica: Certifique-se que libvips está instalado!")
        print("   Windows: choco install libvips")

if __name__ == "__main__":
    # Troque 'lamina_pronta.png' pelo nome da sua imagem de ALTA RESOLUÇÃO
    arquivo = "lamina_pronta.png" 
    
    if len(sys.argv) > 1:
        arquivo = sys.argv[1]
    
    if not os.path.exists(arquivo):
        print(f"❌ Arquivo '{arquivo}' não encontrado!")
        print("📂 Arquivos disponíveis:")
        for f in os.listdir('.'):
            if f.lower().endswith(('.png', '.jpg', '.jpeg')):
                print(f"   - {f}")
    else:
        criar_deepzoom(arquivo)
