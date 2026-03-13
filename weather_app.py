import tkinter as tk
from tkinter import messagebox
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    print("ERROR: OPENWEATHER_API_KEY not found in environment variables.")
    print("Please create a .env file with your API key. See .env.example for details.")
    exit(1)


def get_weather():
    """Fetch weather data for the entered city and display it."""
    city = city_entry.get().strip()

    if city == "":
        result_label.config(text="Please enter a city name", fg="#ff6e40")
        return

    result_label.config(text="Loading...", fg="#ffffff")
    root.update()

    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=5)
        data = response.json()

        if data.get("cod") != 200:
            result_label.config(
                text=f"❌ City not found: '{city}'", fg="#ff6e40"
            )
            return

        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        feels_like = data["main"]["feels_like"]
        wind_speed = data["wind"]["speed"]

        result = f"""
🌍 {city.upper()}

🌡️  Temperature: {temp}°C
🤔 Feels Like: {feels_like}°C
☁️  Weather: {weather}
💧 Humidity: {humidity}%
💨 Wind Speed: {wind_speed} m/s
"""
        result_label.config(text=result, fg="#ffffff")

    except requests.exceptions.Timeout:
        result_label.config(text="❌ Request timeout. Please try again.", fg="#ff6e40")
    except requests.exceptions.ConnectionError:
        result_label.config(
            text="❌ Connection error. Check your internet.", fg="#ff6e40"
        )
    except Exception as e:
        result_label.config(text=f"❌ Error: {str(e)}", fg="#ff6e40")


def on_enter_key(event):
    """Allow pressing Enter to search for weather."""
    get_weather()


# GUI Setup
root = tk.Tk()
root.title("🌦️ Real-Time Weather App")
root.geometry("450x500")
root.configure(bg="#1e3d59")
root.resizable(False, False)

# Title
title = tk.Label(
    root,
    text="🌦️ Weather App",
    font=("Helvetica", 28, "bold"),
    bg="#1e3d59",
    fg="#ffffff",
)
title.pack(pady=20)

# City entry
city_entry = tk.Entry(
    root, font=("Arial", 14), justify="center", width=30, bg="#2d5a7b", fg="white"
)
city_entry.pack(pady=15)
city_entry.bind("<Return>", on_enter_key)

# Search button
search_btn = tk.Button(
    root,
    text="🔍 Get Weather",
    command=get_weather,
    bg="#ff6e40",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=20,
    pady=10,
)
search_btn.pack(pady=10)

# Result display
result_label = tk.Label(
    root,
    text="Enter a city name and click 'Get Weather'",
    font=("Arial", 13),
    bg="#1e3d59",
    fg="#ffffff",
    justify="center",
    wraplength=400,
)
result_label.pack(pady=30)

# Footer
footer = tk.Label(
    root,
    text="Powered by OpenWeatherMap API",
    font=("Arial", 9),
    bg="#1e3d59",
    fg="#999999",
)
footer.pack(side="bottom", pady=10)

root.mainloop()
