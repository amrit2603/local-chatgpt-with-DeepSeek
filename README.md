
# Local ChatGPT

This project leverages DeepSeek-R1 and Chainlit to create a 100% locally running mini-ChatGPT app.

## Installation and setup

**Setup Ollama**:
   ```bash
   # setup ollama on linux 
   curl -fsSL https://ollama.com/install.sh | sh
   # pull the DeepSeek-R1 model
   ollama pull deepseek-r1 
   ```


**Install Dependencies**:
   Ensure you have Python 3.11 or later installed.
   ```bash
   pip install pydantic==2.10.1 chainlit ollama
   ```

**Run the app**:

   Run the chainlit app as follows:
   ```bash
   chainlit run app.py -w
   ```
## Demo 
<img width="1911" height="997" alt="Screenshot 2026-02-27 114717" src="https://github.com/user-attachments/assets/3afbadff-6798-4836-bf0b-df1bab940c6e" />

## Demo Video

Click below to watch the demo video of the AI Assistant in action:

[Watch the video](https://github.com/user-attachments/assets/7c32b459-4024-4d2f-9f9a-648fbf491861)

---


## Contribution

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.
