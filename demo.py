"""
Demo script showing the weather app output without requiring an API key.

This script demonstrates what the application output looks like by using
sample data instead of making real API calls.
"""

from weather_display import WeatherDisplay


def demo_current_weather():
    """Display sample current weather data."""
    # Sample data structure matching OpenWeatherMap API response
    sample_current = {
        'name': 'London',
        'sys': {'country': 'GB'},
        'main': {
            'temp': 15.5,
            'feels_like': 14.2,
            'humidity': 72
        },
        'weather': [
            {'description': 'partly cloudy'}
        ],
        'wind': {
            'speed': 3.5
        }
    }
    
    print("🌤️  Current Weather Demo\n")
    print(WeatherDisplay.format_current_weather(sample_current))


def demo_forecast():
    """Display sample forecast data."""
    # Sample forecast data
    sample_forecast = {
        'city': {
            'name': 'London',
            'country': 'GB'
        },
        'list': [
            {
                'dt': 1729850400,  # Monday 12:00
                'main': {'temp': 16.0},
                'weather': [{'description': 'partly cloudy'}]
            },
            {
                'dt': 1729861200,  # Monday 15:00
                'main': {'temp': 17.5},
                'weather': [{'description': 'clear sky'}]
            },
            {
                'dt': 1729872000,  # Monday 18:00
                'main': {'temp': 15.0},
                'weather': [{'description': 'few clouds'}]
            },
            {
                'dt': 1729936800,  # Tuesday 12:00
                'main': {'temp': 14.5},
                'weather': [{'description': 'light rain'}]
            },
            {
                'dt': 1729947600,  # Tuesday 15:00
                'main': {'temp': 15.0},
                'weather': [{'description': 'overcast clouds'}]
            }
        ]
    }
    
    print("\n📅 Forecast Demo\n")
    print(WeatherDisplay.format_forecast(sample_forecast))


def main():
    """Run the demo."""
    print("=" * 60)
    print("Weather Forecast App - Demo Mode")
    print("=" * 60)
    print("\nThis demo shows what the app output looks like.")
    print("To use real weather data, set OPENWEATHER_API_KEY and run main.py\n")
    
    demo_current_weather()
    demo_forecast()
    
    print("\n" + "=" * 60)
    print("Demo Complete!")
    print("=" * 60)
    print("\n💡 Tips:")
    print("  1. Get a free API key at: https://openweathermap.org/api")
    print("  2. Set OPENWEATHER_API_KEY environment variable")
    print("  3. Run: python main.py <city_name>")
    print()


if __name__ == "__main__":
    main()
