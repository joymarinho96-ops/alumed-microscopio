import os
import sys

print("-" * 40)
print("INICIANDO DIAGNÓSTICO ALUMED")
print("-" * 40)

# 1. Verifica se a pasta existe no local padrão que combinamos
vips_dir = r"C:\vips\bin"
if os.path.exists(vips_dir):
    print(f"[OK] A pasta {vips_dir} existe.")
    
    # 2. Verifica se a DLL principal está lá
    dll_path = os.path.join(vips_dir, "libvips-42.dll")
    if os.path.exists(dll_path):
        print("[OK] O arquivo libvips-42.dll está dentro da pasta.")
    else:
        print("[ERRO] A pasta existe, mas a 'libvips-42.dll' NÃO está lá.")
        print("Verifique se você baixou a versão 'w64-all' correta.")
else:
    print(f"[ERRO] A pasta {vips_dir} NÃO foi encontrada.")
    print("Verifique se você extraiu o zip direto no Disco C: e se a pasta se chama 'vips'.")

print("-" * 40)

# 3. Tenta importar e mostra o erro real se falhar
print("Tentando carregar o pyvips...")
try:
    import pyvips
    print("\n[SUCESSO] O pyvips carregou perfeitamente! Pode rodar o script da marca d'água.")
except OSError as e:
    print("\n[FALHA] O Windows recusou o carregamento.")
    print("Causa provável: O caminho (PATH) não está configurado ou o VS Code não foi reiniciado.")
    print(f"Erro técnico: {e}")
except Exception as e:
    print(f"\n[FALHA] Outro erro aconteceu: {e}")

print("-" * 40)

if len(sys.argv) > 1:
    print('\nNote: additional args provided:', sys.argv[1:])
