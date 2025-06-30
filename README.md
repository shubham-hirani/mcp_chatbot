# MCP Chatbot 🤖

Welcome to **MCP Chatbot** – an interactive AI-powered chatbot that leverages OpenAI and Groq LLMs with [MCP](https://github.com/open-mcp/mcp) for advanced conversational capabilities and browser automation!

---

## ✨ Features

- **Conversational AI**: Chat with the bot using OpenAI or Groq models.
- **Memory**: Maintains conversation history for context-aware responses.
- **Browser Automation**: Integrates with MCP servers for web automation tasks.
- **Easy Setup**: Just configure your API keys and start chatting!
- **Clear Memory**: Type `clear` to reset the conversation memory.
- **Exit Anytime**: Type `exit` or `quit` to leave the chat.

---

## 🚀 Quick Start

### 1. Clone the Repository

```sh
git clone https://github.com/shubham-hirani/mcp_chatbot.git
cd mcp_chatbot
```

### 2. Install Dependencies

```sh
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Copy `sample.env` to `.env` and add your API keys:

```sh
cp sample.env .env
```

Edit `.env` and set your `GROQ_API_KEY` and `OPENAI_API_KEY`.

### 4. Start MCP Servers

The MCP servers are configured in `browser_mcp.json`. You can start them as needed, or let the chatbot connect automatically.

### 5. Run the Chatbot

```sh
python main.py
```

---

## 💬 Usage

- **Chat**: Type your message and press Enter.
- **Clear Memory**: Type `clear` and press Enter.
- **Exit**: Type `exit` or `quit` and press Enter.

---

## 🛠️ Configuration

- **MCP Servers**: Edit `browser_mcp.json` to add or modify MCP server configurations.
- **VS Code Integration**: See `.vscode/mcp.json` for JetBrains MCP proxy setup.

---

## 📁 Project Structure

```
.
├── main.py               # Main chatbot script
├── requirements.txt      # Python dependencies
├── .env                  # Your API keys (not committed)
├── sample.env            # Example environment file
├── browser_mcp.json      # MCP server configurations
├── .vscode/              # VS Code settings
└── .idea/                # IDE settings (ignored)
```

---

## 📝 License

This project is for educational purposes.

---

## 🙏 Acknowledgements

- [OpenAI](https://openai.com/)
- [Groq](https://groq.com/)
- [LangChain](https://python.langchain.com/)
- [MCP](https://github.com/open-mcp/mcp)

---

Enjoy chatting! 🚀
