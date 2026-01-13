import sys
from PIL import Image, ImageDraw, ImageFont
import os

def criar_marca_dagua(input_path, output_path, texto):
    try:
        # Carrega a imagem
        img = Image.open(input_path)
        largura, altura = img.size
        
        # Cria uma camada transparente para a marca d'água
        marca = Image.new('RGBA', (largura, altura), (255, 255, 255, 0))
        draw = ImageDraw.Draw(marca)
        
        # Tenta usar uma fonte maior, cai para padrão se não existir
        tamanho_fonte = max(40, int(min(largura, altura) / 8))
        try:
            fonte = ImageFont.truetype("arial.ttf", tamanho_fonte)
        except:
            fonte = ImageFont.load_default()
        
        # Desenha o texto várias vezes na diagonal (padrão repetido)
        cor_texto = (255, 255, 255, 76)  # Branco com 30% de opacidade
        
        bbox = draw.textbbox((0, 0), texto, font=fonte)
        texto_largura = bbox[2] - bbox[0]
        texto_altura = bbox[3] - bbox[1]
        
        # Repete o texto na diagonal por toda a imagem
        import math
        angulo = 45
        
        y = -altura
        while y < altura * 2:
            x = -largura
            while x < largura * 2:
                draw.text((x, y), texto, font=fonte, fill=cor_texto)
                x += texto_largura + 50
            y += texto_altura + 50
        
        # Rotaciona a marca d'água 45 graus
        marca = marca.rotate(45, expand=True)
        
        # Redimensiona a marca para caber na imagem
        marca = marca.crop((0, 0, largura, altura))
        
        # Converte a imagem original para RGBA se necessário
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Compõe a imagem com a marca d'água
        resultado = Image.alpha_composite(img, marca)
        
        # Converte de volta para RGB se for salvar como JPEG
        if output_path.lower().endswith('.jpg') or output_path.lower().endswith('.jpeg'):
            resultado = resultado.convert('RGB')
        
        # Salva o arquivo final
        resultado.save(output_path, quality=95)
        print(f"Sucesso! Imagem salva em: {output_path}")

    except Exception as e:
        print(f"Erro ao processar: {e}")

if __name__ == "__main__":
    # Verifica se os argumentos foram passados
    if len(sys.argv) < 4:
        print("Como usar: python watermark.py imagem.jpg saida.jpg 'Texto da Marca'")
    else:
        criar_marca_dagua(sys.argv[1], sys.argv[2], sys.argv[3])
