# Quick Start Guide

Get the weather forecast app running in 5 minutes!

## Option 1: Demo Mode (No API Key Required)

Run the demo to see sample output immediately:

```bash
python demo.py
```

This will show you what the app looks like without requiring any setup.

## Option 2: Live Weather Data

### Step 1: Get API Key (2 minutes)

1. Go to https://openweathermap.org/api
2. Click "Sign Up" (free tier available)
3. Verify your email
4. Go to API Keys section and copy your key

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set API Key

**On Linux/Mac:**
```bash
export OPENWEATHER_API_KEY="your_api_key_here"
```

**On Windows (PowerShell):**
```powershell
$env:OPENWEATHER_API_KEY="your_api_key_here"
```

**On Windows (Command Prompt):**
```cmd
set OPENWEATHER_API_KEY=your_api_key_here
```

### Step 4: Run the App

```bash
# Default city (London)
python main.py

# Specific city
python main.py Paris
python main.py "New York"
python main.py Tokyo
```

## Trying the AI Agent Context Feature

### With GitHub Copilot:

1. Open this project in VS Code with GitHub Copilot enabled
2. Open `example_extensions.py`
3. Try implementing the incomplete methods
4. Notice how Copilot suggests code that matches the project style

### Without GitHub Copilot:

Read `COPILOT_CONTEXT_GUIDE.md` to understand how AI agent context works and how this project is structured to demonstrate it.

## Common Issues

### "API key not found"
- Make sure you've set the `OPENWEATHER_API_KEY` environment variable
- Check that there are no extra spaces in your API key
- Verify the API key is active on OpenWeatherMap

### "Could not fetch weather"
- Check your internet connection
- Verify the city name is spelled correctly
- Make sure your API key is activated (may take a few minutes after signup)

### "No module named 'requests'"
- Run: `pip install -r requirements.txt`

## Next Steps

- Read `README.md` for full documentation
- Check out `COPILOT_CONTEXT_GUIDE.md` to learn about AI agent context
- Try extending the app with new features in `example_extensions.py`
- Experiment with different cities and observe the output

## Quick Reference

```bash
# Demo mode
python demo.py

# Real weather for London (default)
python main.py

# Real weather for specific city
python main.py "San Francisco"

# Install dependencies
pip install -r requirements.txt

# Check Python version (need 3.8+)
python --version
```

## Support

If you encounter issues:
1. Check this Quick Start guide
2. Review the main README.md
3. Verify your Python version is 3.8 or higher
4. Ensure all dependencies are installed

Happy weather forecasting! 🌤️
