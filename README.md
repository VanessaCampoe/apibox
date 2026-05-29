# API Box de Feiras 🎪📱

API simples, direta e otimizada para fornecer dados de boxes de feiras para aplicativos **Android Nativo**.

---

## 🛠️ Tecnologias e Ícones

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/DJANGO--REST-ff1709?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white)

---

## 🔌 Contrato da API (Para o Android)

* **Rota:** `/box/`
* **Método HTTP:** `GET`
* **Formato de Saída:** `JSON`

### 📥 Exemplo de Resposta (`Status 200 OK`):
```json
{
    "id": 1,
    "nome": "Loja Infantil Kids",
    "numero": 101
}
# 1. Clone o projeto e acesse a pasta
git clone <url-do-repositorio>
cd <pasta-do-projeto>

# 2. Crie e ative o ambiente virtual (Venv)
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate

# 3. Instale o Django e o Django REST Framework
pip install django djangorestframework

# 4. Prepare o banco SQLite e inicie o servidor
python manage.py migrate
python manage.py runserver"# apibox" 
