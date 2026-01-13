import pyvips
import os
from pathlib import Path

print("🔬 Conversor de Lâminas Histológicas (SVS → DZI)")
print("=" * 60)

# Procurar por arquivos SVS
laminas_dir = Path('imagens_laminas')
svs_files = list(laminas_dir.glob('*.svs')) + list(laminas_dir.glob('*.SVS'))

if not svs_files:
    print("⚠️  Nenhum arquivo .svs encontrado em 'imagens_laminas/'")
    print("\n📌 Você pode:")
    print("  1. Baixar slides do UFRJ: http://www.histo.ufrj.br/LIB/")
    print("  2. Colocar arquivo.svs na pasta 'imagens_laminas/'")
    print("  3. Rodar este script novamente")
else:
    for svs_file in svs_files:
        print(f"\n📂 Processando: {svs_file.name}")
        
        try:
            # Carrega a imagem SVS
            print("  ⏳ Carregando imagem...")
            imagem = pyvips.Image.new_from_file(str(svs_file), access='sequential')
            
            print(f"  📏 Dimensões: {imagem.width} x {imagem.height}")
            
            # Define nome de saída (sem extensão)
            output_name = laminas_dir / svs_file.stem
            
            # Converte para DZI (Deep Zoom Image)
            print("  🔄 Convertendo para DZI...")
            imagem.dzsave(str(output_name), tile_size=256, overlap=1, depth=8)
            
            print(f"  ✅ Sucesso! Salvo em: {output_name}.dzi")
            print(f"     Pasta de tiles: {output_name}_files/")
            
        except Exception as e:
            print(f"  ❌ Erro: {str(e)}")

print("\n" + "=" * 60)
print("💡 Para usar no visualizador:")
print("   1. Arquivo gerado: imagens_laminas/[nome].dzi")
print("   2. Folder: imagens_laminas/[nome]_files/")
print("   3. Use OpenSeadragon no HTML para visualizar")
print("=" * 60)
