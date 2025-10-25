"""Weather service for fetching data from OpenWeatherMap API."""

import requests
from typing import Dict, Any, Optional
from config import Config


class WeatherService:
    """Service class for interacting with OpenWeatherMap API."""
    
    def __init__(self, config: Config):
        """
        Initialize the weather service.
        
        Args:
            config: Configuration object containing API settings
        """
        self.config = config
        self.session = requests.Session()
    
    def get_current_weather(self, city: str) -> Optional[Dict[str, Any]]:
        """
        Fetch current weather data for a given city.
        
        Args:
            city: Name of the city to fetch weather for
            
        Returns:
            Dictionary containing weather data, or None if request fails
        """
        try:
            url = f"{self.config.base_url}/weather"
            params = {
                'q': city,
                'appid': self.config.api_key,
                'units': self.config.units
            }
            
            response = self.session.get(
                url,
                params=params,
                timeout=self.config.timeout
            )
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None
    
    def get_forecast(self, city: str, days: int = 5) -> Optional[Dict[str, Any]]:
        """
        Fetch weather forecast for a given city.
        
        Args:
            city: Name of the city to fetch forecast for
            days: Number of days to forecast (default: 5)
            
        Returns:
            Dictionary containing forecast data, or None if request fails
        """
        try:
            url = f"{self.config.base_url}/forecast"
            params = {
                'q': city,
                'appid': self.config.api_key,
                'units': self.config.units,
                'cnt': days * 8  # API returns data in 3-hour intervals
            }
            
            response = self.session.get(
                url,
                params=params,
                timeout=self.config.timeout
            )
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching forecast data: {e}")
            return None
    
    def close(self):
        """Close the HTTP session."""
        self.session.close()
