# SEC Championship Simulator 🏈

An interactive web application that simulates SEC Championship Game matchups using Answer Set Programming (ASP) with Clingo.

## Overview

This simulator allows users to set win/loss conditions for four top SEC teams and uses ASP-based reasoning to determine which two teams would compete in the SEC Championship Game based on your custom logic.

## Features

- **Interactive Interface**: Clean, modern web UI with toggle buttons for each team
- **Real-time Simulation**: Instant results using Clingo's ASP solver
- **Randomizer**: Randomly generate win/loss scenarios
- **Shareable**: Easy to deploy and share on social media

## Teams

1. Texas A&M
2. Alabama
3. Georgia
4. Ole Miss

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/sec-championship-simulator.git
cd sec-championship-simulator
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Select Win or Loss for each team using the toggle buttons

4. Click **"Go"** to run the simulation

5. Use the **"Randomize"** button to generate random scenarios

## How It Works

### ASP Logic

The simulator uses the Clingo Python API to interface with Answer Set Programming logic. When you select results for each team:

- Facts are added to the knowledge base (e.g., `tamu_win`, `bama_loss`)
- Clingo solves the ASP program with these constraints
- The solution returns which teams qualify: `sec(tamu)`, `sec(bama)`, `sec(uga)`, or `sec(miss)`

### Customizing the Logic

The ASP encoding is located in `app.py` in the `solve_sec_championship()` function. Replace the placeholder encoding with your actual SEC championship rules:

```python
encoding = """
% Your custom ASP logic here
% Define tiebreaker rules, conference standings, head-to-head records, etc.
"""
```

You can also load your encoding from an external `.lp` file:

```python
ctl.load("path/to/your/encoding.lp")
```

## Project Structure

```
sec-championship-simulator/
├── app.py                 # Flask application and Clingo interface
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── style.css         # Styling
│   └── script.js         # Frontend JavaScript
└── README.md             # This file
```

## Deployment

### Local Development
The app runs on `localhost:5000` by default. Perfect for testing and development.

### Production Deployment

For sharing on LinkedIn or deploying publicly, consider these options:

1. **Heroku**: Easy deployment with free tier
2. **PythonAnywhere**: Simple Python hosting
3. **AWS/GCP/Azure**: Cloud platforms for scalable deployment
4. **Render/Railway**: Modern deployment platforms

Example Heroku deployment:
```bash
# Add Procfile
echo "web: python app.py" > Procfile

# Initialize git and deploy
git init
heroku create your-sec-simulator
git add .
git commit -m "Initial commit"
git push heroku main
```

## Technical Details

- **Backend**: Flask (Python web framework)
- **ASP Solver**: Clingo (via Python API)
- **Frontend**: Vanilla JavaScript, HTML5, CSS3
- **Styling**: Modern gradient design with responsive layout

## Contributing

Feel free to fork this repository and customize the ASP logic for different scenarios or add additional teams/features.

## License

MIT License - feel free to use and modify for your own projects.

## Author

Built with Python, Flask, and Clingo ASP by kep, with development help from [claude.ai](https://claude.ai)

## Acknowledgments

- Powered by [Clingo](https://potassco.org/clingo/) ASP solver
- Designed for SEC football analytics

---

**Note**: This is a simulation tool. Replace the placeholder ASP logic with your actual conference championship determination rules for accurate results.
