import os
import glob

# Get all images
imagens = sorted(glob.glob('imagens_laminas/lamina_*.png')) + sorted(glob.glob('imagens_laminas/lamina_*.jpg'))

html_selector = '<div class="lamina-selector" id="lamina-selector">\n'

# First thumbnail (lamina_0)
if os.path.exists('imagens_laminas/lamina_0.jpg'):
    html_selector += '    <div class="lamina-thumb active" data-src="imagens_laminas/lamina_0.jpg" title="Cardioesophageal">\n'
    html_selector += '        <img src="imagens_laminas/lamina_0.jpg" alt="Lamina Original">\n'
    html_selector += '    </div>\n'

# Add all Leeds images
for i, img_path in enumerate(imagens, 1):
    img_name = os.path.basename(img_path)
    title = img_name.replace('lamina_leeds_', '').replace('.png', '').replace('.jpg', '')
    
    html_selector += f'    <div class="lamina-thumb" data-src="{img_path}" title="Leeds {title}">\n'
    html_selector += f'        <img src="{img_path}" alt="Lamina {i+1}">\n'
    html_selector += '    </div>\n'

html_selector += '</div>'

print("HTML do Seletor de Lâminas:")
print("=" * 80)
print(html_selector)
print("=" * 80)

# Also save to file
with open('lamina_selector.html', 'w') as f:
    f.write(html_selector)

print(f"\n✅ Seletor gerado! ({len(imagens) + 1} lâminas totais)")
print("📁 Salvo em: lamina_selector.html")
