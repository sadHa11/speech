import speech_recognition as sr
import os

def open_application(application_name):
  """Opens the specified application.

  Args:
    application_name: The name of the application to open.
  """
  os.system(f"start {application_name}")

def main():
  """The main function."""
  # Initialize the speech recognizer.
  recognizer = sr.Recognizer()

  # Listen for the user's speech.
  with sr.Microphone() as microphone:
    print("Speak now.")
    audio = recognizer.listen(microphone)

  # Convert the audio to text.
  try:
    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")

    # Open the application.
    open_application(text)
  except:
    print("Sorry, I didn't understand what you said.")

if __name__ == "__main__":
  main()
