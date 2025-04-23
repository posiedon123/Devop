🎙️ Voice-Controlled Virtual Assistant
A Python-based virtual assistant named Jarvis that can perform tasks such as searching Wikipedia, opening websites, playing music, checking the time, and sending emails—all through voice commands.

🚀 Features
Voice Commands:

Recognizes voice input using the speech_recognition library.
Provides spoken responses using the pyttsx3 library.
Greetings Based on Time:

Wishes the user "Good Morning," "Good Afternoon," or "Good Evening" based on the current time.
Task Automation:

Wikipedia Search: Searches for a topic on Wikipedia and reads out a summary.
Open Websites: Opens commonly used websites like YouTube, Google, and StackOverflow.
Play Music: Plays songs from a specified local directory.
Check Time: Reads the current time aloud.
Open Code Editor: Opens VS Code (or any configured path).
Email Functionality:

Sends an email using smtplib.
Note: Update your email credentials in the script for this feature to work.
📋 Setup Instructions
Install Required Libraries:

Email Configuration:
Replace the placeholders youremail@gmail.com and your-password with your Gmail credentials in the sendEmail function. Enable "Allow less secure apps" in Gmail for testing purposes.

Music Directory Path:
Update the music_dir variable with the path to your local music folder.

VS Code Path:
Replace the codePath with the correct path for your VS Code or preferred editor.

🛠️ How to Run
Save the script as jarvis.py.
Run the script
Speak into your microphone when prompted with "Listening...".
🎤 Voice Commands Examples
"Open YouTube" → Opens YouTube in the browser.
"Search Wikipedia for Python" → Retrieves a summary about Python from Wikipedia.
"Play music" → Plays music from your local directory.
"What is the time" → Jarvis tells you the current time.
"Email to Harry" → Sends an email to a specified recipient.
⚠️ Important Notes
The email feature requires you to enable Less Secure Apps in Gmail. For production, use OAuth2 for email.
Ensure you have an active internet connection for web-based tasks like Wikipedia search.
