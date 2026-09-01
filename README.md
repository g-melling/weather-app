# Weather App 🌤️

A simple Python desktop application built with **Tkinter** that displays the current **Air Quality Index (AQI)** for a given ZIP code using the AirNow API.

## Features

* Search air quality data by ZIP code
* Displays:

  * City name
  * Air Quality Index (AQI)
  * Air quality category
* Color-coded background based on air quality level
* Simple and lightweight Tkinter GUI

## Technologies Used

* Python 3
* Tkinter (GUI)
* Requests (API calls)
* JSON
* AirNow API

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
```

### 2. Install dependencies

```bash
pip install requests
```

### 3. Run the application

```bash
python weather.py
```

## How It Works

1. Enter a ZIP code in the input field.
2. Click **Enter Zipcode**.
3. The application sends a request to the AirNow API.
4. Current air quality information is retrieved and displayed.
5. The window background changes color based on the AQI category.

## Air Quality Categories

| Category                       | Color  |
| ------------------------------ | ------ |
| Good                           | Green  |
| Moderate                       | Yellow |
| Unhealthy for Sensitive Groups | Orange |
| Unhealthy                      | Red    |
| Very Unhealthy                 | Purple |
| Hazardous                      | Maroon |

## Project Structure

```text
weather-app/
│
├── weather.py
├── README.md
└── screenshot.png
```

## API

This project uses the AirNow API:

https://www.airnow.gov/

Example endpoint:

```text
https://www.airnowapi.org/aq/observation/zipCode/current/
```

## Important Note

The API key is currently hardcoded in the source code. For production use, it is recommended to store API keys in environment variables or a configuration file rather than committing them to source control.

Example:

```python
import os

API_KEY = os.getenv("AIRNOW_API_KEY")
```
