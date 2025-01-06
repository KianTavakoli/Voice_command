# 🎙️ **Voice-Activated Assistant** 🎙️

This project implements a simple **voice-activated assistant** that listens for user commands and performs actions such as opening YouTube, performing a Google search, or exiting the program.

---

## ✨ **Features**

- **Voice Activation**: The assistant activates based on a trigger condition.
- **Command Recognition**: Supports voice commands for:
  - 🔗 **YouTube**: Opens YouTube.
  - 🔍 **Search**: Performs a Google search.
  - ❌ **Exit**: Exits the assistant.
- **Error Handling**: If the command is not recognized, the assistant prompts the user to repeat it.

---

## 🛠️ **Requirements**

- `speech_recognition`
- `pyaudio` (for microphone input)
- Custom modules:
  - `Google`
  - `YouTube`
  - `Voice`
  - `Activation`

You can install the required Python packages using:
```bash
pip install SpeechRecognition pyaudio
```

---

## 🚀 **How It Works**

1. **Initialization**:
   - The script initializes the microphone and speech recognizer.
2. **Activation**:
   - The assistant waits for a trigger condition (`Activation.Activation.activate`) to become true.
   - Once activated, it greets the user with "Hello Kian".
3. **Listening for Commands**:
   - The assistant prompts the user with "What do you want?".
   - It listens for voice input and processes the command using `recognize_google`.
4. **Command Execution**:
   - Based on the recognized command:
     - 🖥️ **YouTube**: Calls the YouTube module to open YouTube.
     - 🌐 **Search**: Calls the Google module to perform a search.
     - ❌ **Exit**: Exits the assistant.
5. **Error Handling**:
   - If the speech is not recognized or any error occurs, it prompts the user to "Say again".

---

## 📋 **Usage Instructions**

1. Clone the repository and navigate to the project directory.
2. Ensure you have all required modules and dependencies installed.
3. Run the script:
   ```bash
   python voice_assistant.py
   ```
4. Follow the voice prompts and give appropriate commands.

---

## 🔧 **Customization**

- You can add more commands by extending the `if-elif` block in the script.
- Additional modules can be created for new actions and integrated into the main loop.

---

## 💡 **Notes**

- Ensure your microphone is properly configured and has the necessary permissions.
- Background noise may affect the recognition accuracy. Try to run the assistant in a quiet environment.

---

## 📄 **License**

This project is licensed under the **MIT License**.

