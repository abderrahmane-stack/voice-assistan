# Voice Assistant

A Python-based voice assistant that automates various tasks, such as searching Wikipedia, opening applications, and sending emails.

## Features

- **Speech Recognition**: Converts spoken language into text for command processing.
- **Text-to-Speech**: Provides vocal responses to your commands.
- **Application Control**: Opens commonly used applications like Notepad and Paint.
- **Web Search**: Retrieves information from Wikipedia and opens websites.
- **Email Sending**: Sends emails using Gmail.

## Setup

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/abderrahmane-stack/voice-assistan.git
```

### 2. Navigate to the Project Directory

Move into the project directory:

```bash
cd voice-assistant
```

### 3. Set Up a Virtual Environment (Optional but Recommended)

It's recommended to create a virtual environment to manage dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies

Create a `requirements.txt` file in your project directory with the following content:

```
pyttsx3
SpeechRecognition
wikipedia
```

Then, install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Run the Script

To start the voice assistant, run:

```bash
python voice_assistant.py
```

### 2. Interact with the Assistant

Follow the voice prompts to interact with the assistant. You can issue commands like:

- "Search Wikipedia for [topic]."
- "Open Notepad."
- "Send email to [email address]."

## Configuration

### Update Email Credentials

To enable email functionality, you need to update your email credentials in `voice_assistant.py`:

```python
sender_email = 'your-email@gmail.com'
app_password = 'your-app-password'
```

**Note:** If two-factor authentication is enabled on your Gmail account, you must use an App Password. You can generate one from your Google Account settings.

### Specify Recipient Email

When using the email feature, ensure that you specify the recipient's email address:

```python
to_email = 'recipient@example.com'
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

