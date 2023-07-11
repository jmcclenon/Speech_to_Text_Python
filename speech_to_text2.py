import os
import json
import logging
import speech_recognition as sr
from datetime import datetime

# Setup logging
logging.basicConfig(filename='speech_to_text.log', level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s')

def load_config():
    """Load configuration from a JSON file."""
    with open("config.json") as f:
        config = json.load(f)
    return config

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone` using `recognizer`."""

    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        logging.info("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)
        logging.info("Listening...")
        audio = recognizer.listen(source)

    try:
        response = recognizer.recognize_google(audio).lower()
    except sr.RequestError:
        logging.error("API unavailable/unresponsive")
    except sr.UnknownValueError:
        logging.error("Unable to recognize speech")

    return response

def write_to_file(filename, text):
    """Write the given `text` to the `filename`."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as file:
        file.write(f"{timestamp}: {text}\n")

def main():
    config = load_config()

    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    while True:
        text = recognize_speech_from_mic(recognizer, mic)

        if text in config['exit_phrases']:
            logging.info("Exit phrase detected, stopping the program.")
            break

        write_to_file(config['output_file'], text)
        logging.info("Text written to file.")

if __name__ == "__main__":
    main()
