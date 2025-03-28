# 🧠 Phi-4 Mini Instruct Chatbot Interface

This is a lightweight web-based chatbot interface powered by the **phi4** model running through [Ollama](https://ollama.com). It features a modern dark-mode UI, streaming word-by-word responses, and Enter-to-submit support.

## 🚀 Features

- 🌙 Default Dark Mode with toggle
- ✨ Smooth and responsive UI using HTML/CSS/JS
- 🧵 Word-by-word streaming output from the LLM
- 💬 Press **Enter** to submit (Shift+Enter for newline)
- ⚡ Fast local inference via Ollama (uses `phi4` model)

---

## 📦 Requirements

- Python 3.8+
- Ollama (installed and `ollama serve` is running)
- `Flask`
- `ollama` Python client

### 📥 Install dependencies

```bash
pip install flask ollama
```

### 📥 Pull the phi4 model (if not yet)

```bash
ollama pull phi4
```

### ▶️ Running the App

```
python app.py
```
Then visit http://localhost:5000 in your browser.

### 📁 Project Structure

```
├── app.py             # Flask backend server
├── templates/
│   └── index.html     # Frontend interface
└── README.md          # Project documentation
```

### ✨ Customizations

- The HTML interface is located in templates/index.html
- Model used: phi4 (you can change this in app.py)
- Streaming logic is implemented in Python for word-by-word display

### 📸 Preview

![resim](https://github.com/user-attachments/assets/326bb5d2-313b-4506-a97e-792bfc4544fd)


### 🧠 Powered By

- [Ollama](https://ollama.com/)
- Phi-4 Mini Instruct
- Flask

### 📄 License

MIT License — use it freely, modify it proudly 🙌
