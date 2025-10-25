"""Configuration management for the weather forecast application."""

import os
from typing import Optional


class Config:
    """Configuration class for weather application settings."""
    
    def __init__(self):
        """Initialize configuration with environment variables."""
        self.api_key: Optional[str] = os.getenv('OPENWEATHER_API_KEY')
        self.base_url: str = 'https://api.openweathermap.org/data/2.5'
        self.units: str = 'metric'  # Use metric units by default
        self.timeout: int = 10  # API request timeout in seconds
    
    def validate(self) -> bool:
        """
        Validate that all required configuration is present.
        
        Returns:
            bool: True if configuration is valid, False otherwise
        """
        return self.api_key is not None and len(self.api_key) > 0
