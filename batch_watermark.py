import os
import subprocess

# --- CONFIGURAÇÕES ---
# O texto da sua marca
TEXTO_MARCA = "Propriedade ALUMED"
# Nome da pasta onde vão ficar as imagens prontas
PASTA_SAIDA = "Laminas_Prontas"

# Cria a pasta de saída se não existir
if not os.path.exists(PASTA_SAIDA):
    os.makedirs(PASTA_SAIDA)
    print(f"Pasta '{PASTA_SAIDA}' criada!")

# Procura todas as imagens na pasta atual
arquivos = [f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

print(f"Encontrei {len(arquivos)} imagens. Começando...")

for arquivo in arquivos:
    # Pula o próprio script ou imagens já prontas para não dar erro
    if arquivo.startswith("lamina_pronta"):
        continue
        
    caminho_entrada = arquivo
    caminho_saida = os.path.join(PASTA_SAIDA, arquivo)
    
    print(f"Carimbando: {arquivo}...")
    
    # Chama o seu script watermark.py para cada imagem
    subprocess.run(["python", "watermark.py", caminho_entrada, caminho_saida, TEXTO_MARCA])

print("-" * 30)
print(f"TUDO PRONTO, AMOR! ✨")
print(f"As imagens marcadas estão na pasta: {PASTA_SAIDA}")
