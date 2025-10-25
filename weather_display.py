"""Display module for formatting and showing weather information."""

from typing import Dict, Any, Optional
from datetime import datetime


class WeatherDisplay:
    """Class for formatting and displaying weather information."""
    
    @staticmethod
    def format_current_weather(data: Dict[str, Any]) -> str:
        """
        Format current weather data for display.
        
        Args:
            data: Weather data dictionary from API
            
        Returns:
            Formatted string with weather information
        """
        if not data:
            return "No weather data available"
        
        city = data.get('name', 'Unknown')
        country = data.get('sys', {}).get('country', '')
        temp = data.get('main', {}).get('temp', 0)
        feels_like = data.get('main', {}).get('feels_like', 0)
        humidity = data.get('main', {}).get('humidity', 0)
        description = data.get('weather', [{}])[0].get('description', 'N/A')
        wind_speed = data.get('wind', {}).get('speed', 0)
        
        output = [
            "=" * 50,
            f"Current Weather in {city}, {country}",
            "=" * 50,
            f"Temperature: {temp}°C (Feels like: {feels_like}°C)",
            f"Condition: {description.capitalize()}",
            f"Humidity: {humidity}%",
            f"Wind Speed: {wind_speed} m/s",
            "=" * 50
        ]
        
        return "\n".join(output)
    
    @staticmethod
    def format_forecast(data: Dict[str, Any]) -> str:
        """
        Format forecast data for display.
        
        Args:
            data: Forecast data dictionary from API
            
        Returns:
            Formatted string with forecast information
        """
        if not data or 'list' not in data:
            return "No forecast data available"
        
        city = data.get('city', {}).get('name', 'Unknown')
        country = data.get('city', {}).get('country', '')
        
        output = [
            "=" * 50,
            f"5-Day Forecast for {city}, {country}",
            "=" * 50,
            ""
        ]
        
        # Group forecasts by day
        current_date = None
        for item in data['list']:
            dt = datetime.fromtimestamp(item['dt'])
            date_str = dt.strftime('%Y-%m-%d')
            
            # Print date header for new day
            if date_str != current_date:
                current_date = date_str
                output.append(f"\n{dt.strftime('%A, %B %d, %Y')}")
                output.append("-" * 40)
            
            time_str = dt.strftime('%H:%M')
            temp = item['main']['temp']
            description = item['weather'][0]['description']
            
            output.append(f"  {time_str}: {temp}°C - {description.capitalize()}")
        
        output.append("=" * 50)
        return "\n".join(output)
    
    @staticmethod
    def display_error(message: str):
        """
        Display an error message.
        
        Args:
            message: Error message to display
        """
        print(f"\n❌ Error: {message}\n")
    
    @staticmethod
    def display_info(message: str):
        """
        Display an informational message.
        
        Args:
            message: Info message to display
        """
        print(f"\nℹ️  {message}\n")
