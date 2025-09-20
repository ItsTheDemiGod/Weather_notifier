Weather Notifier
A simple Python-based weather notification app that fetches current weather data using the OpenWeatherMap API and sends it as a WhatsApp message at a user-specified time.

Overview
This program prompts you for your city, a WhatsApp phone number (with country code), and a desired notification time (in HH:MM format). It then schedules and sends a WhatsApp notification with the weather details (e.g., temperature and description) using the pywhatkit library. The weather data is retrieved from the OpenWeatherMap API (requires a free API key).

Note: This is a console-based script that must remain running to handle scheduling. For production use, consider deploying it on a server or using a more robust scheduling tool.

Requirements
Python 3.x

Libraries: requests, pywhatkit, schedule (install via pip)

A free OpenWeatherMap API key (sign up at openweathermap.org)

Google Chrome installed (for pywhatkit to automate WhatsApp Web)

WhatsApp Web must be logged in on your browser before the scheduled time

Installation
Clone the repository:

text
git clone https://github.com/ItsTheDemiGod/Weather_notifier.git
(Or download the ZIP file and extract it.)

Install dependencies:

text
pip install requests pywhatkit schedule
Replace 'YOUR_API_KEY' in weather_notifier.py with your actual OpenWeatherMap API key.

Usage
Run the script in your terminal:

text
python weather_notifier.py
Follow the prompts:

Enter your city (e.g., "New York").

Enter the WhatsApp phone number (with country code, e.g., "+1234567890").

Enter the desired notification time (HH:MM in 24-hour format, e.g., "14:30").

Ensure WhatsApp Web is already logged in on your default browser (Google Chrome) before the scheduled time.

Keep the script running. At the specified time, it will automatically open WhatsApp Web, send the weather message (e.g., "Weather in New York: 22°C, clear sky"), and log the action.

Example Output:

text
Enter your city: New York
Enter WhatsApp phone number (with country code, e.g., +1234567890): +1234567890
Enter desired notification time (HH:MM in 24-hour format): 14:30
Notification scheduled for 14:30. Keep this script running.
