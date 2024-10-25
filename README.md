# Descripción
Este proyecto permite extraer los comentarios de un video de YouTube utilizando la API oficial de YouTube.

# Requisitos previos
- Python 3.x
- Una API Key de YouTube

# Instalación

1. Clonar el repositorio
```git clone https://github.com/KevinAQM/youtube_comments.git```

2. Dirijirse a la carpeta del proyecto:
```cd youtube_comments```

3. Crear el entorno virtual:
```python -m venv .venv```

4. Activar entorno virtual:
## En Windows:
```.venv\\Scripts\\activate```
## En Unix o MacOS:
```source .venv/bin/activate```

3. Instalar dependencias
```pip install -r requirements.txt```

4. Configurar variables de entorno
- Copiar \`.env.example\` a \`.env\`
- Obtener una API KEY de YouTube
- Añadir tu API KEY en el archivo \`.env\`

# Uso
En el terminal:
- Ejecutar la aplicación: ```python main.py```
- Ingresar la URL del video de YouTube.
- ¡Listo! Tu resultado se habrá guardado en la carpeta 'outputs'

# Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles
EOL
