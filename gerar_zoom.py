#!/usr/bin/env python3
"""
Gerador de Deep Zoom Tiles usando PIL
Cria estrutura de tiles compatível com OpenSeadragon
"""

import os
import sys
from PIL import Image
import math
import xml.etree.ElementTree as ET

def gerar_deepzoom(arquivo_entrada, tile_size=256, quality=90):
    """Gera tiles Deep Zoom a partir de uma imagem"""
    
    if not os.path.exists(arquivo_entrada):
        print(f"❌ Arquivo '{arquivo_entrada}' não encontrado!")
        return False
    
    nome_base = os.path.splitext(arquivo_entrada)[0]
    pasta_saida = f"{nome_base}_files"
    
    print(f"🔬 Carregando imagem: {arquivo_entrada}")
    img = Image.open(arquivo_entrada)
    largura, altura = img.size
    
    print(f"📐 Dimensões: {largura} x {altura} pixels")
    
    # Cria pasta de saída
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)
    
    # Calcula número de níveis de zoom
    max_dim = max(largura, altura)
    num_niveis = math.ceil(math.log2(max_dim / tile_size)) + 1
    
    print(f"📊 Gerando {num_niveis} níveis de zoom...")
    
    # Converte para RGB se tiver transparência
    if img.mode in ('RGBA', 'LA', 'P'):
        rgb_img = Image.new('RGB', img.size, (255, 255, 255))
        if img.mode == 'P':
            img = img.convert('RGBA')
        rgb_img.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
        img = rgb_img
    
    # Gera cada nível
    for nivel in range(num_niveis):
        # Calcula escala: nível 0 é a menor imagem
        escala = 2 ** (num_niveis - 1 - nivel)
        nova_largura = max(1, largura // escala)
        nova_altura = max(1, altura // escala)
        
        # Redimensiona imagem para este nível
        img_nivelada = img.resize((nova_largura, nova_altura), Image.Resampling.LANCZOS)
        
        # Cria pasta para este nível
        pasta_nivel = os.path.join(pasta_saida, str(nivel))
        if not os.path.exists(pasta_nivel):
            os.makedirs(pasta_nivel)
        
        # Divide em tiles
        num_tiles_x = math.ceil(nova_largura / tile_size)
        num_tiles_y = math.ceil(nova_altura / tile_size)
        
        for y in range(num_tiles_y):
            for x in range(num_tiles_x):
                # Coordenadas do tile
                esquerda = x * tile_size
                topo = y * tile_size
                direita = min(esquerda + tile_size, nova_largura)
                fundo = min(topo + tile_size, nova_altura)
                
                # Extrai tile
                tile = img_nivelada.crop((esquerda, topo, direita, fundo))
                
                # Converte para RGB se necessário (importante para JPEG)
                if tile.mode != 'RGB':
                    tile = tile.convert('RGB')
                
                # Salva com padding se necessário
                if tile.size != (tile_size, tile_size):
                    tile_padded = Image.new('RGB', (tile_size, tile_size), (255, 255, 255))
                    tile_padded.paste(tile, (0, 0))
                    tile = tile_padded
                
                caminho_tile = os.path.join(pasta_nivel, f"{x}_{y}.jpg")
                tile.save(caminho_tile, 'JPEG', quality=quality)
        
        print(f"   ✓ Nível {nivel}: {num_tiles_x}x{num_tiles_y} tiles ({nova_largura}x{nova_altura}px)")
    
    # Cria arquivo DZI (Deep Zoom Image)
    dzi_conteudo = f'''<?xml version="1.0" encoding="UTF-8"?>
<Image xmlns="http://schemas.microsoft.com/deepzoom/2008"
       TileSize="{tile_size}"
       Overlap="0"
       Format="jpg">
  <Size Width="{largura}" Height="{altura}"/>
</Image>'''
    
    arquivo_dzi = f"{nome_base}.dzi"
    with open(arquivo_dzi, 'w') as f:
        f.write(dzi_conteudo)
    
    print(f"\n✅ Sucesso! Deep Zoom criado:")
    print(f"   📁 Pasta de tiles: {pasta_saida}/")
    print(f"   📄 Arquivo DZI: {arquivo_dzi}")
    print(f"\n🚀 Use em OpenSeadragon com:")
    print(f'   tileSources: "{arquivo_dzi}"')
    
    return True

if __name__ == "__main__":
    arquivo = "lamina_pronta.png"
    
    if len(sys.argv) > 1:
        arquivo = sys.argv[1]
    
    gerar_deepzoom(arquivo)
