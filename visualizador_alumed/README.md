# 🔬 Visualizador ALUMED - Django Setup

Estrutura criada com sucesso! 

## 📁 Estrutura de Pastas

```
visualizador_alumed/
├── manage.py                    # Gerenciador Django
├── db.sqlite3                   # Banco de dados (será criado)
├── visualizador_alumed/         # Configurações do projeto
│   ├── __init__.py
│   ├── settings.py             # Configurações Django
│   ├── urls.py                 # Rotas da aplicação
│   └── wsgi.py                 # WSGI para produção
├── templates/                   # Arquivos HTML
│   ├── index.html              # Home
│   └── visualizador.html       # Visualizador de lâminas
└── static/                      # Arquivos estáticos
    ├── css/
    │   └── style.css
    ├── js/
    │   └── app.js
    └── images/
        └── (suas imagens aqui)
```

## 🚀 Como Usar

### 1. Instalar Django
```bash
pip install django
```

### 2. Criar superuser (opcional para admin)
```bash
python manage.py createsuperuser
```

### 3. Executar servidor
```bash
python manage.py runserver 8000
```

Acesse: **http://localhost:8000**

## 📝 Próximos Passos

1. Criar arquivo `static/css/style.css` com seus estilos
2. Criar arquivo `static/js/app.js` com sua lógica
3. Colocar imagens na pasta `static/images/`
4. Criar template `visualizador.html` para o viewer

## ⚙️ Configuração

- **DEBUG**: True (mudar para False em produção)
- **ALLOWED_HOSTS**: '*' (configurar em produção)
- **LANGUAGE**: pt-br
- **TIMEZONE**: America/Sao_Paulo

---
© 2026 ALUMED
