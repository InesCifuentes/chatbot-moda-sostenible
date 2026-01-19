import streamlit as st
from agents.agent import CohereAgent
from agents.data_queries import DataQueries

def main():
    st.set_page_config(page_title="Cohere Chat", page_icon="💬", layout="wide")

    # CSS personalizado
    st.markdown(
        """
        <style>
        /* Fondo general claro y tipografía */
        .stApp {
            background-color: #d7ccc8; /* Tono marrón terroso */
            font-family: 'Arial', sans-serif;
        }

        /* Título principal en tono más suave */
        .main-title {
            color: #4e342e; /* Marrón suave */
            font-size: 2.5em;
            font-weight: bold;
            text-align: left;
            margin-bottom: 20px;
        }

        /* Subtítulo descriptivo */
        .description {
            color: #6d4c41; /* Tono complementario más suave */
            font-size: 1.2em;
            text-align: left;
            margin-bottom: 40px;
        }

        /* Mensaje del usuario */
        .user-message {
            background-color: #e0f7fa; /* Azul muy claro */
            color: #006064;            /* Azul profundo */
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            border: none; /* Eliminar bordes oscuros */
        }

        /* Mensaje del asistente */
        .assistant-message {
            background-color: #f1f8e9; /* Verde muy claro */
            color: #33691e;            /* Verde profundo */
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            border: none; /* Eliminar bordes oscuros */
        }

        /* Estilo del input del chat */
        .stTextInput > div > div > input {
            border: 1px solid #d7ccc8; /* Coincidir con el fondo */
            border-radius: 5px;
            padding: 10px;
            background-color: #f5f5f5; /* Aclarar el cuadro de entrada */
            color: #4e342e; /* Color de texto más suave */
        }

        /* Eliminar bordes oscuros de los contenedores de Streamlit */
        .css-1cpxqw2 {
            border: none;
        }
        .css-1v3fvcr {
            border: none;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Título y descripción
    st.markdown("<div class='main-title'>💬 Chat de Moda Sostenible</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='description'>Bienvenido al chat de moda sostenible. Aquí puedes hacer preguntas sobre sostenibilidad, materiales ecológicos y marcas responsables. ¡Comienza escribiendo tu mensaje abajo! 🌿</div>",
        unsafe_allow_html=True
    )

    # Inicializar consultas y agente
    queries = DataQueries("data/sustainable_fashion_trends_2024.csv")
    agent = CohereAgent(queries=queries)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostrar historial de chat
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f'<div class="user-message">{msg["content"]}</div>', unsafe_allow_html=True)
        elif msg["role"] == "assistant":
            st.markdown(f'<div class="assistant-message">{msg["content"]}</div>', unsafe_allow_html=True)

    # Input del usuario
    user_input = st.chat_input("Escribe tu mensaje...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.markdown(f'<div class="user-message">{user_input}</div>', unsafe_allow_html=True)

        response = agent.chat_with_history(user_input, st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.markdown(f'<div class="assistant-message">{response}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
