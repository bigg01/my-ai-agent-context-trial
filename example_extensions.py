"""
Example: How to extend this application with new features

This file demonstrates how GitHub Copilot's AI agent context helps when adding
new features to the weather application.

When you open this file in VS Code with Copilot enabled, try typing the code
below and observe how Copilot suggests code that matches the project patterns.
"""

from typing import Dict, Any, Optional
from weather_service import WeatherService
from config import Config


class WeatherCache:
    """
    Cache weather data to reduce API calls.
    
    This class demonstrates how Copilot would suggest implementation details
    based on the project's context and existing patterns.
    """
    
    def __init__(self, ttl_seconds: int = 300):
        """
        Initialize the weather cache.
        
        Args:
            ttl_seconds: Time-to-live for cached data in seconds (default: 300)
        """
        self._cache: Dict[str, Dict[str, Any]] = {}
        self.ttl_seconds = ttl_seconds
    
    def get(self, key: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve cached weather data.
        
        Args:
            key: Cache key (typically the city name)
            
        Returns:
            Cached data if available and not expired, None otherwise
        """
        # Try typing this method and see how Copilot suggests implementation
        # that follows the project's error handling and return type patterns
        pass
    
    def set(self, key: str, data: Dict[str, Any]):
        """
        Store weather data in cache.
        
        Args:
            key: Cache key (typically the city name)
            data: Weather data to cache
        """
        # Copilot will suggest cache storage logic matching the project style
        pass
    
    def clear(self):
        """Clear all cached data."""
        # Simple implementation suggestion from Copilot
        pass


class WeatherAlerts:
    """
    Handle weather alerts and notifications.
    
    Another example class where Copilot would provide contextual suggestions.
    """
    
    def __init__(self, service: WeatherService):
        """
        Initialize weather alerts service.
        
        Args:
            service: WeatherService instance for fetching data
        """
        self.service = service
    
    def check_temperature_alert(
        self,
        city: str,
        min_temp: float,
        max_temp: float
    ) -> Optional[str]:
        """
        Check if current temperature is outside the specified range.
        
        Args:
            city: City to check temperature for
            min_temp: Minimum acceptable temperature
            max_temp: Maximum acceptable temperature
            
        Returns:
            Alert message if temperature is out of range, None otherwise
        """
        # When you start implementing this, Copilot will suggest:
        # 1. Calling self.service.get_current_weather(city)
        # 2. Proper error handling with try-except
        # 3. Extracting temperature from the response
        # 4. Comparing with thresholds
        # 5. Returning formatted alert message
        pass


# Try creating your own classes here and see how Copilot helps!
# For example, try typing:
# class WeatherComparison:
#     """Compare weather between two cities."""
#
# And watch Copilot suggest methods and implementation based on the project context.
