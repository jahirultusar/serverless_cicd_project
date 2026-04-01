import json

WEATHER = {
    "london": {
        "city": "London",
        "condition": "Cloudy with light rain",
        "temperature": "12°C",
        "humidity": "78%",
        "wind": "15 mph SW"
    },
    "new york": {
        "city": "New York",
        "condition": "Partly cloudy",
        "temperature": "18°C",
        "humidity": "62%",
        "wind": "10 mph NW"
    },
    "tokyo": {
        "city": "Tokyo",
        "condition": "Clear skies",
        "temperature": "22°C",
        "humidity": "55%",
        "wind": "8 mph E"
    },
    "sydney": {
        "city": "Sydney",
        "condition": "Sunny",
        "temperature": "26°C",
        "humidity": "48%",
        "wind": "12 mph NE"
    },
    "paris": {
        "city": "Paris",
        "condition": "Overcast",
        "temperature": "14°C",
        "humidity": "71%",
        "wind": "9 mph W"
    }
}

def lambda_handler(event, context):
    params = event.get("queryStringParameters") or {}
    city = params.get("city", "london").strip().lower()

    weather = WEATHER.get(city)

    if not weather:
        available = ", ".join(WEATHER.keys())
        return {
            "statusCode": 400,
            "headers": {"Access-Control-Allow-Origin": "*",
                        "Content-Type": "application/json"},
            "body": json.dumps({
                "skill": "tell_weather",
                "message": f"Sorry, I don't have weather data for {city}. Try one of these: {available}."
            })
        }

    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps({
            "skill": "tell_weather",
            "message": (
                f"The weather in {weather['city']} is currently {weather['condition']}. "
                f"Temperature: {weather['temperature']}, "
                f"Humidity: {weather['humidity']}, "
                f"Wind: {weather['wind']}."
            )
        })
    }