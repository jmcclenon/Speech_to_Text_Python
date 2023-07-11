# Speech Recognition Script

This Python script uses the `speech_recognition` library to convert spoken language into written text. It continually listens for audio input until a predefined exit phrase is spoken and writes the recognized speech to a file. It also logs various events to a log file for future analysis.

## Features

- Continuous speech recognition until an exit phrase is spoken.
- Recognized speech is written to a file with timestamps.
- Detailed logging of events to a log file.
- Adjustable settings through a configuration file.

## Installation

1. Clone this repository:

git clone https://github.com/jmcclenon/speech_recognition.git

2. Navigate to the project directory:

cd speech_recognition

3. Install the required Python packages:

pip install -r requirements.txt

4. If you're on Windows, you might need to install PyAudio separately:

pip install pyaudio

If you encounter issues installing PyAudio, you may need to install some additional dependencies. Refer to the [PyAudio documentation](http://people.csail.mit.edu/hubert/pyaudio/) for more information.

## Usage

1. Modify the `config.json` file as needed. You can specify the output file name and the phrases that should cause the script to exit.
2. Run the script:

python main.py

3. Speak into your microphone. The script will transcribe your speech and write it to the output file. To stop the script, speak one of the exit phrases specified in the `config.json` file.

## License

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.
