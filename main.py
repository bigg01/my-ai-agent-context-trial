"""Main entry point for the weather forecast application."""

import sys
from config import Config
from weather_service import WeatherService
from weather_display import WeatherDisplay


def main():
    """Run the weather forecast application."""
    # Initialize configuration
    config = Config()
    
    # Validate configuration
    if not config.validate():
        WeatherDisplay.display_error(
            "API key not found. Please set OPENWEATHER_API_KEY environment variable."
        )
        WeatherDisplay.display_info(
            "Get your free API key at: https://openweathermap.org/api"
        )
        sys.exit(1)
    
    # Get city from command line argument or use default
    if len(sys.argv) > 1:
        city = " ".join(sys.argv[1:])
    else:
        city = "London"
        WeatherDisplay.display_info(f"No city specified. Using default: {city}")
    
    # Initialize weather service
    weather_service = WeatherService(config)
    
    try:
        # Fetch and display current weather
        print("\n🌤️  Fetching current weather...\n")
        current_weather = weather_service.get_current_weather(city)
        
        if current_weather:
            print(WeatherDisplay.format_current_weather(current_weather))
        else:
            WeatherDisplay.display_error(f"Could not fetch weather for '{city}'")
            sys.exit(1)
        
        # Fetch and display forecast
        print("\n📅 Fetching forecast...\n")
        forecast = weather_service.get_forecast(city)
        
        if forecast:
            print(WeatherDisplay.format_forecast(forecast))
        else:
            WeatherDisplay.display_error(f"Could not fetch forecast for '{city}'")
    
    finally:
        # Clean up
        weather_service.close()


if __name__ == "__main__":
    main()
