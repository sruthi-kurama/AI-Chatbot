import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from google import genai
import requests

load_dotenv()

print("Gemini Key:", os.getenv("GEMINI_API_KEY"))
print("Weather Key:", os.getenv("WEATHER_API_KEY"))

app = Flask(__name__)

# Gemini API Key
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# OpenWeatherMap API Key
WEATHER_API_KEY =  os.getenv("WEATHER_API_KEY")


# =========================
# Extract City using Gemini
# =========================
def extract_city(message):

    try:

        response = client.models.generate_content(
            model=("gemini-2.5-flash"),
            contents=f"""
Extract only the city name from this sentence.

Sentence: {message}

Return ONLY the city name.
If no city is found return NONE.
"""
        )

        return response.text.strip()

    except:
        return "NONE"


# =========================
# Current Weather
# =========================
def get_weather(city):

    try:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={"38cd4551f1e85820b913c49ee1ade9a6"}&units=metric"

        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            return f"❌ Could not find weather for '{city}'."

        city_name = data["name"]
        country = data["sys"]["country"]

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        description = data["weather"][0]["description"]

        return f"""
🌍 City: {city_name}, {country}

🌡 Temperature: {temp}°C
🤗 Feels Like: {feels_like}°C
💧 Humidity: {humidity}%

☁ Condition: {description}
"""

    except Exception as e:

        return f"Weather Error: {str(e)}"


# =========================
# Forecast Weather
# =========================
def get_forecast(city):

    try:

        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={"38cd4551f1e85820b913c49ee1ade9a6"}&units=metric"

        response = requests.get(url)
        data = response.json()

        if data.get("cod") != "200":
            return f"❌ Could not find forecast for '{city}'."

        # Approx. 24 hours later
        tomorrow = data["list"][8]

        temp = tomorrow["main"]["temp"]
        humidity = tomorrow["main"]["humidity"]

        description = tomorrow["weather"][0]["description"]

        rain_expected = "rain" in description.lower()

        return f"""
📅 Tomorrow Forecast

🌍 City: {city}

🌡 Temperature: {temp}°C
💧 Humidity: {humidity}%

☁ Condition: {description}

🌧 Rain Expected: {"Yes" if rain_expected else "No"}
"""

    except Exception as e:

        return f"Forecast Error: {str(e)}"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    message = data["message"]

    try:

        msg = message.lower()

        weather_keywords = [
            "weather",
            "temperature",
            "rain",
            "raining",
            "humidity",
            "forecast",
            "hot",
            "cold",
            "wind",
            "storm",
            "umbrella",
            "climate",
            "sunny",
            "cloudy"
        ]

        # Weather detection
        if any(word in msg for word in weather_keywords):

            city = extract_city(message)

            if city == "NONE":

                return jsonify({
                    "reply": "❌ Please mention a city name."
                })

            # Forecast questions
            if (
                "tomorrow" in msg
                or "forecast" in msg
                or "next day" in msg
            ):

                reply = get_forecast(city)

            else:

                reply = get_weather(city)

            return jsonify({
                "reply": reply
            })

        # Normal Gemini Chat
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=message
        )

        reply = response.text

    except Exception as e:

        if "429" in str(e):

            reply = "⚠️ API usage limit reached."

        elif "503" in str(e):

            reply = "⚠️ AI service is currently busy."

        else:

            reply = f"Error: {str(e)}"

    return jsonify({
        "reply": reply
    })


if __name__ == "__main__":
    app.run(debug=True)