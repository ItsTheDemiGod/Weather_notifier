import requests
import pywhatkit
import schedule
import time
from datetime import datetime

# Function to fetch weather data
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if data["cod"] != 200:
            return f"Error: City not found or API issue."
        
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return f"Weather in {city}: {temp}°C, {description}"
    except Exception as e:
        return f"Error fetching weather: {str(e)}"

# Function to send WhatsApp message
def send_whatsapp_message(phone_number, city, api_key):
    weather_message = get_weather(city, api_key)
    now = datetime.now()
    hour = now.hour
    minute = now.minute + 2  # pywhatkit requires at least 2 minutes ahead
    if minute >= 60:
        hour += 1
        minute -= 60
    try:
        pywhatkit.sendwhatmsg(phone_number, weather_message, hour, minute, wait_time=20, tab_close=True)
        print(f"Message scheduled to {phone_number} at {hour:02d}:{minute:02d}")
    except Exception as e:
        print(f"Failed to send WhatsApp message: {str(e)}")

# Main function
def main():
    city = input("Enter your city: ")
    phone_number = input("Enter WhatsApp phone number (with country code, e.g., +1234567890): ")
    desired_time = input("Enter desired notification time (HH:MM in 24-hour format): ")
    
    # Validate phone number
    if not phone_number.startswith('+') or not phone_number[1:].isdigit():
        print("Invalid phone number format. Use + followed by country code and number.")
        return

    # Parse time
    try:
        hour, minute = map(int, desired_time.split(':'))
        if not (0 <= hour <= 23 and 0 <= minute <= 59):
            raise ValueError
        now = datetime.now()
        scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        if scheduled_time <= now:
            print("Scheduled time must be in the future.")
            return
    except ValueError:
        print("Invalid time format. Use HH:MM (e.g., 14:30).")
        return

    api_key = 'e38e45dde86da941b73a8875dd87308c'  # Replace with your OpenWeatherMap API key

    # Schedule the message
    def job():
        send_whatsapp_message(phone_number, city, api_key)

    schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(job)

    print(f"Notification scheduled for {desired_time}. Keep this script running and logged in to WhatsApp Web.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
