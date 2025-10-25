# Weather Forecast App - AI Agent Context Example

This project demonstrates how to use **GitHub Copilot's AI agent context** to improve code completion and suggestions in a real-world application.

## 🎯 What is AI Agent Context?

AI agent context refers to the additional information and instructions you provide to GitHub Copilot to help it better understand your project and generate more relevant code suggestions. This is achieved through:

1. **`.github/copilot-instructions.md`** - Project-specific instructions that guide Copilot
2. **Well-structured code** - Clear module organization and naming conventions
3. **Type hints and docstrings** - Explicit type information and documentation
4. **Consistent coding patterns** - Following established patterns throughout the codebase

## 📁 Project Structure

```
.
├── .github/
│   └── copilot-instructions.md  # AI agent context instructions
├── config.py                     # Configuration management
├── weather_service.py            # API integration layer
├── weather_display.py            # Display formatting
├── main.py                       # Application entry point
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🚀 Features

- **Current Weather**: Get real-time weather conditions for any city
- **5-Day Forecast**: View detailed weather predictions
- **Clean Architecture**: Separated concerns with distinct modules
- **Error Handling**: Graceful handling of API failures
- **Type Safety**: Full type hints for better code completion

## 📋 Prerequisites

- Python 3.8 or higher
- OpenWeatherMap API key (free tier available)

## 🔧 Installation

1. Clone this repository:
```bash
git clone https://github.com/bigg01/my-ai-agent-context-trial.git
cd my-ai-agent-context-trial
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Get your free API key from [OpenWeatherMap](https://openweathermap.org/api)

4. Set your API key as an environment variable:
```bash
# On Linux/Mac:
export OPENWEATHER_API_KEY="your_api_key_here"

# On Windows (Command Prompt):
set OPENWEATHER_API_KEY=your_api_key_here

# On Windows (PowerShell):
$env:OPENWEATHER_API_KEY="your_api_key_here"
```

## 💻 Usage

Run the application with a city name:

```bash
python main.py London
```

Or run without arguments to use the default city (London):

```bash
python main.py
```

### Example Output

```
ℹ️  Fetching current weather...

==================================================
Current Weather in London, GB
==================================================
Temperature: 15°C (Feels like: 14°C)
Condition: Partly cloudy
Humidity: 72%
Wind Speed: 3.5 m/s
==================================================

📅 Fetching forecast...

==================================================
5-Day Forecast for London, GB
==================================================

Monday, October 25, 2025
----------------------------------------
  12:00: 16°C - Partly cloudy
  15:00: 17°C - Clear sky
  18:00: 15°C - Few clouds
...
```

## 🤖 How GitHub Copilot Uses This Context

When you open this project in VS Code with GitHub Copilot enabled, it will:

1. **Read `.github/copilot-instructions.md`** to understand:
   - Project architecture and module responsibilities
   - Coding style preferences (PEP 8, type hints, docstrings)
   - Common patterns to follow
   - Testing expectations

2. **Analyze the code structure** to learn:
   - How modules interact with each other
   - Naming conventions used
   - Error handling patterns
   - API integration approaches

3. **Provide better suggestions** when you:
   - Create new functions (suggests proper type hints and docstrings)
   - Add error handling (follows existing patterns)
   - Implement new features (adheres to architecture guidelines)
   - Write tests (matches testing conventions)

## 🧪 Try It Yourself

To see AI agent context in action:

1. Open this project in VS Code with GitHub Copilot enabled
2. Create a new file, e.g., `weather_cache.py`
3. Start typing a class definition:
   ```python
   class WeatherCache:
   ```
4. Watch how Copilot suggests:
   - Proper docstrings matching the project style
   - Type hints for methods
   - Error handling patterns similar to existing code
   - Methods that fit the project architecture

## 📚 Learning Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [OpenWeatherMap API Documentation](https://openweathermap.org/api)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [PEP 8 Style Guide](https://pep8.org/)

## 🤝 Contributing

This is an example project for learning purposes. Feel free to fork and experiment with:
- Adding more weather features
- Implementing caching
- Creating a GUI
- Adding unit tests
- Improving error handling

## 📄 License

This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.