from flask import Flask, request, render_template_string
import requests
import json

app = Flask(__name__)

template = """
<html>
  <body>
    <h1>Weather Forecast</h1>
    <form action="/" method="post">
      <label for="location">Enter the name of a city or a zip code:</label>
      <input type="text" id="location" name="location"><br><br>
      <input type="submit" value="Get Weather">
    </form>
    {% if temperature %}
      <p>Temperature: {{ temperature }}°C</p>
      <p>Humidity: {{ humidity }}%</p>
      <p>Wind Speed: {{ wind_speed }} m/s</p>
      <p>Weater Conditions: {{ description }}</p>
    {% endif %}
  </body>
</html>
"""

def get_weather(api_key, location):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    weather_data = response.json()
    return weather_data

def parse_weather(weather_data):
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]
    description = weather_data["weather"][0]["description"]
    return temperature, humidity, wind_speed, description

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        api_key = " Enter Your OPENWEATHERMAP API KEY"
        location = request.form["location"]
        weather_data = get_weather(api_key, location)
        if weather_data["cod"] != "404":
            temperature, humidity, wind_speed, description = parse_weather(weather_data)
            return render_template_string(template, temperature=temperature, humidity=humidity, wind_speed=wind_speed, description=description)
        else:
            return render_template_string(template, temperature=None, humidity=None, wind_speed=None, description="City not found")
    return render_template_string(template)

if __name__ == "__main__":
    app.run()