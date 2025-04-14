from flask import Flask, request, render_template_string
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

app = Flask(__name__)

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.json()}
    except Exception as e:
        return {"error": str(e)}

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>🌤️ Weather App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #74ebd5, #ACB6E5);
            color: #333;
            text-align: center;
            padding: 50px;
        }
        .container {
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
            max-width: 500px;
            margin: auto;
        }
        input[type="text"] {
            padding: 10px;
            width: 70%;
            border-radius: 10px;
            border: 1px solid #ccc;
            margin-bottom: 10px;
        }
        button {
            padding: 10px 20px;
            border-radius: 10px;
            border: none;
            background: #4facfe;
            color: white;
            font-weight: bold;
            cursor: pointer;
        }
        .weather {
            margin-top: 20px;
            padding: 15px;
            background: #f1f1f1;
            border-radius: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>🌦️ Weather App</h2>
        <form method="get" action="/">
            <input type="text" name="city" placeholder="Enter city name" required>
            <button type="submit">Get Weather</button>
        </form>

        {% if weather %}
            {% if weather.error %}
                <div class="weather"><strong>Error:</strong> {{ weather.error }}</div>
            {% else %}
                <div class="weather">
                    <h3>Weather in {{ weather.name }}</h3>
                    <p><strong>Temperature:</strong> {{ weather.main.temp }}°C</p>
                    <p><strong>Condition:</strong> {{ weather.weather[0].description.title() }}</p>
                    <p><strong>Humidity:</strong> {{ weather.main.humidity }}%</p>
                    <p><strong>Wind Speed:</strong> {{ weather.wind.speed }} m/s</p>
                </div>
            {% endif %}
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET'])
def home():
    city = request.args.get('city')
    weather_data = None
    if city:
        weather_data = get_weather(city)
    return render_template_string(HTML_TEMPLATE, weather=weather_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    