# Voice Assistant

A Python-based voice assistant that can perform various tasks such as searching Wikipedia, opening applications, and sending emails.

## Features

- **Speech Recognition**: Converts spoken language into text.
- **Text-to-Speech**: Converts text into spoken voice.
- **Application Control**: Opens applications like Notepad and Paint.
- **Web Search**: Searches Wikipedia and opens websites.
- **Email Sending**: Sends emails through Gmail.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/voice-assistant.git
2. Navigate to the project directory:

   ```sh
   cd voice-assistant
3. Install the required packages:
   Create a requirements.txt file in your project directory with the following content:

   ```sh
    pyttsx3
    SpeechRecognition
    wikipedia
   ```
Then run:
   ```sh
    pip install -r requirements.txt
  ```
4. Usage
Run the script:

 ```sh
  python voice_assistant.py
 ```
Interact with the assistant: Follow the voice prompts to interact with the assistant. You can issue commands like "open Wikipedia," "open Notepad," or "send email to [email address]."
5. Configuration
Update Email Credentials:
Open voice_assistant.py and update the sendEmail function with your email credentials:

```sh
sender_email = 'your-email@gmail.com'
app_password = 'your-app-password'
```
Note: Use an App Password if two-factor authentication is enabled on your Gmail account. You can generate an App Password from your Google Account settings.

Specify Recipient Email:
When calling the sendEmail function, provide the recipient's email address:

 ```sh
   to_email = 'recipient@example.com
