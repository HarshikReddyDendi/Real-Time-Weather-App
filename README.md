🌦️ Real-Time Weather App
A simple, user-friendly weather application built with Python and Tkinter that fetches real-time weather data using the OpenWeatherMap API.
Features

🌍 Search weather for any city in the world
🌡️ Display temperature, feels-like temperature, and weather conditions
💧 Show humidity and wind speed
🎨 Beautiful, intuitive GUI with Tkinter
⚡ Fast and responsive
🔒 Secure API key handling using environment variables

Screenshots
The app displays:

Current temperature (in Celsius)
"Feels like" temperature
Weather description
Humidity percentage
Wind speed

Prerequisites

Python 3.7 or higher
pip (Python package manager)

Installation
1. Clone the repository
bashgit clone https://github.com/yourusername/weather-app.git
cd weather-app
2. Create a virtual environment (recommended)
bash# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
bashpip install -r requirements.txt
4. Get an API Key

Go to OpenWeatherMap API
Sign up for a free account
Copy your API key

5. Set up environment variables

Create a .env file in the project root:

bashcp .env.example .env

Edit .env and add your API key:

OPENWEATHER_API_KEY=your_api_key_here

⚠️ Never commit the .env file to GitHub! It's in .gitignore for your protection.

Usage
Run the application:
bashpython weather_app.py

Enter a city name in the text field
Click "🔍 Get Weather" or press Enter
View the weather information displayed

Project Structure
weather-app/
├── weather_app.py          # Main application script
├── requirements.txt        # Python dependencies
├── .env.example           # Example environment variables
├── .gitignore             # Git ignore rules
└── README.md              # This file
Security

API Key Protection: The API key is stored in a .env file and loaded as an environment variable
Never hardcoded: The key is not committed to the repository
Safe for public repos: The .gitignore file ensures .env won't be accidentally pushed

Improvements Made
✅ Removed hardcoded API key
✅ Added environment variable support
✅ Improved error handling with specific exceptions
✅ Better user interface with emoji icons
✅ Enter key support for faster searching
✅ Added wind speed and "feels like" temperature
✅ Timeout handling for network requests
✅ Removed infinite refresh loop
Troubleshooting
"OPENWEATHER_API_KEY not found in environment variables"

Make sure you created a .env file with your API key
Verify the file is in the same directory as weather_app.py
Restart the application after creating the .env file

"City not found"

Check the spelling of the city name
Try using the city's English name

"Connection error"

Check your internet connection
Verify that openweathermap.org is accessible

Dependencies

requests - For making HTTP requests to the API
python-dotenv - For loading environment variables from .env file
tkinter - Built into Python (no installation needed)

License
This project is open source and available under the MIT License.
API Attribution
Weather data provided by OpenWeatherMap

Made with ❤️ for weather enthusiasts!
