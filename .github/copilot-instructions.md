# GitHub Copilot Instructions

This project is a weather forecast application that demonstrates the use of AI agent context with GitHub Copilot.

## Project Overview

This is a Python-based weather forecast application that:
- Fetches weather data from OpenWeatherMap API
- Displays current weather conditions
- Shows a 5-day forecast
- Uses object-oriented design patterns

## Code Style Guidelines

- Use Python 3.8+ features
- Follow PEP 8 style guidelines
- Use type hints for function parameters and return values
- Add docstrings to all classes and functions
- Keep functions small and focused (max 20 lines)
- Use descriptive variable names

## Architecture

- `weather_service.py`: Handles API communication with weather service
- `weather_display.py`: Formats and displays weather information
- `main.py`: Entry point for the application
- `config.py`: Configuration management

## API Integration

When working with the OpenWeatherMap API:
- Use environment variables for API keys (never hardcode)
- Handle API errors gracefully with try-except blocks
- Implement retry logic for transient failures
- Cache responses when appropriate

## Testing

- Write unit tests for all service classes
- Mock external API calls in tests
- Aim for >80% code coverage

## Common Patterns

When adding new features:
1. Create a new class or function in the appropriate module
2. Add type hints and docstrings
3. Handle errors appropriately
4. Add corresponding tests
