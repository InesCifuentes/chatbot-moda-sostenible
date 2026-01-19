# 💬 Chat de Moda Sostenible

[![Python](https://img.shields.io/badge/Python-3.9+-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-✔️-green)](https://streamlit.io/)
[![Cohere](https://img.shields.io/badge/Cohere-✔️-purple)](https://cohere.ai/)

Un **asistente conversacional de moda sostenible** que responde preguntas sobre marcas ecológicas, materiales responsables y tendencias de moda sostenible. Utiliza la base de datos de **Sustainable Fashion Trends 2024** y Cohere para generar respuestas inteligentes.  

🌿 **Ideal para:** Aprender sobre moda sostenible, explorar materiales ecológicos y descubrir marcas responsables.  

## 🚀 Uso de la aplicación
Ejecuta la aplicación localmente y chatea con el asistente sobre moda sostenible:
```bash
streamlit run app.py
```

## 📂 Estructura del Proyecto
```
.
├── agents/
│   ├── agent.py           # Clase CohereAgent y lógica de chat
│   ├── context.py         # Prompt del asistente
│   └── data_queries.py    # Consultas a la base de datos de moda sostenible
├── data/
│   └── sustainable_fashion_trends_2024.csv  # Dataset limpio de Kaggle
├── app.py                 # Aplicación Streamlit
├── requirements.txt       # Dependencias
└── .env                   # Variables de entorno (API Key de Cohere)
```

## ⚡ Instalación Rápida
1. Clonar el repositorio:

```bash
git clone https://github.com/InesCifuentes/chatbot-moda-sostenible.git
cd chatbot-moda-sostenible
```

2. Crear y activar un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar la API Key de Cohere en un archivo .env:
```bash
COHERE_API_KEY=tu_api_key_aqui
```

5. Ejecutar la app:
```bash
streamlit run app.py
```

## 🛠 Funcionalidades
- Responde preguntas sobre:
  - Países con mayor huella de carbono en moda.
  - Materiales más utilizados en ropa sostenible.
  - Marcas de moda más sostenibles.
- Recomienda ropa ecológica y explica su impacto positivo.
- Mantiene historial de chat con interfaz amigable y colores inspirados en la naturaleza.

## 📊 Dataset

Se utiliza el dataset:  
[Sustainable Fashion Eco-Friendly Trends 2024 - Kaggle](https://www.kaggle.com/datasets/waqi786/sustainable-fashion-eco-friendly-trends)  

> Nota: Antes de usarlo, el dataset fue **limpiado y procesado** para eliminar inconsistencias y facilitar las consultas.  
> El archivo `sustainable_fashion_trends_2024.csv` ya preparado se encuentra en la carpeta `data/`.