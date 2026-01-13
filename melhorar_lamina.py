#!/usr/bin/env python3
"""
Melhora qualidade de lâminas histológicas
Realça contraste, nitidez e detalhe para visualizar núcleos
"""

import os
import sys
from PIL import Image, ImageEnhance, ImageFilter

def melhorar_lamina(arquivo_entrada, arquivo_saida=None, qualidade=95):
    """
    Melhora qualidade da lâmina histológica
    - Aumenta contraste
    - Melhora nitidez
    - Realça detalhes dos núcleos
    """
    
    if not os.path.exists(arquivo_entrada):
        print(f"❌ Arquivo '{arquivo_entrada}' não encontrado!")
        return False
    
    if not arquivo_saida:
        nome_base = os.path.splitext(arquivo_entrada)[0]
        arquivo_saida = f"{nome_base}_hd.png"
    
    print(f"🔬 Processando: {arquivo_entrada}")
    img = Image.open(arquivo_entrada)
    
    print(f"📏 Dimensões originais: {img.size[0]} x {img.size[1]} pixels")
    
    # 1. CONTRASTE - Realça diferenças entre núcleos e citoplasma
    print("✓ Aumentando contraste...")
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0)  # +100% contraste
    
    # 2. NITIDEZ - Melhora definição dos núcleos
    print("✓ Aumentando nitidez...")
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(2.5)  # +150% nitidez
    
    # 3. BRILHO - Ajusta sem perder detalhe
    print("✓ Ajustando brilho...")
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.1)  # +10% brilho
    
    # 4. COR/SATURAÇÃO - Realça cores da coloração H&E
    print("✓ Aumentando saturação para H&E...")
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(1.3)  # +30% saturação
    
    # 5. FILTRO DE DETALHE - Realça bordas dos núcleos
    print("✓ Aplicando filtro de detalhe...")
    img = img.filter(ImageFilter.DETAIL)
    
    # 6. UNSHARP MASK - Realça bordas sem artefatos
    print("✓ Aplicando Unsharp Mask para nitidez extrema...")
    # Convert para modo que permita unsharp_mask
    img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    
    # Salvar com alta qualidade
    print(f"💾 Salvando como: {arquivo_saida}")
    if arquivo_saida.lower().endswith('.jpg') or arquivo_saida.lower().endswith('.jpeg'):
        img.save(arquivo_saida, 'JPEG', quality=qualidade, optimize=True)
    else:
        img.save(arquivo_saida, 'PNG', optimize=True)
    
    # Informações finais
    arquivo_info = os.path.getsize(arquivo_saida) / (1024 * 1024)
    print(f"\n✅ Concluído!")
    print(f"   📁 Arquivo: {arquivo_saida}")
    print(f"   💾 Tamanho: {arquivo_info:.2f} MB")
    print(f"   🔍 Melhorias aplicadas:")
    print(f"      • Contraste: +100%")
    print(f"      • Nitidez: +150%")
    print(f"      • Unsharp Mask: 150%")
    print(f"      • Saturação: +30%")
    print(f"      • Filtros: DETAIL + UnsharpMask")
    print(f"\n💡 Resultado: Núcleos muito mais visíveis!")
    
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python melhorar_lamina.py <arquivo.png> [saida.png]")
        print("\nExemplo:")
        print("  python melhorar_lamina.py lamina_pronta.png")
        print("  python melhorar_lamina.py lamina_pronta.png lamina_pronta_melhorada.png")
        print("\nProcessará automáticamente todas as imagens se nenhuma for especificada:")
        print("  python melhorar_lamina.py --all")
        sys.exit(1)
    
    if sys.argv[1] == "--all":
        # Processar todas as imagens
        import glob
        arquivos = glob.glob("*.png") + glob.glob("*.jpg")
        if not arquivos:
            print("❌ Nenhuma imagem encontrada!")
            sys.exit(1)
        
        print(f"🔄 Processando {len(arquivos)} imagens...\n")
        for arquivo in arquivos:
            if "_hd" not in arquivo and "watermark" not in arquivo.lower():
                melhorar_lamina(arquivo)
                print()
    else:
        arquivo = sys.argv[1]
        saida = sys.argv[2] if len(sys.argv) > 2 else None
        melhorar_lamina(arquivo, saida)
