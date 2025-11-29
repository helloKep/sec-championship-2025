from flask import Flask, render_template, request, jsonify
import clingo
import random

app = Flask(__name__)

def solve_sec_championship(team_results):
    """
    Solve the SEC championship using Clingo.
    
    Args:
        team_results: dict with keys 'tamu', 'bama', 'uga', 'miss' 
                     and values 'win' or 'loss'
    
    Returns:
        list of teams that reach the SEC championship
    """
    # Create a Clingo control object
    ctl = clingo.Control()
    
    # Option 1: Load from external file (uncomment to use)
    import os
    encoding_path = os.path.join(os.path.dirname(__file__), 'encoding.lp')
    if os.path.exists(encoding_path):
        ctl.load(encoding_path)
    else:
        pass
        # Fallback to inline encoding
    
    # ctl.add("base", [], encoding)
    
    # Add the facts based on team results
    facts = []
    team_map = {
        'tamu': 'tamu',
        'bama': 'bama', 
        'uga': 'uga',
        'miss': 'miss'
    }
    
    for team_key, result in team_results.items():
        team = team_map[team_key]
        if result == 'win':
            facts.append(f"{team}_win.")
            ctl.add("base", [], f"{team}_win.")
        else:
            facts.append(f"{team}_loss.")
            ctl.add("base", [], f"{team}_loss.")
    
    # Ground the program
    ctl.ground([("base", [])])
    
    # Solve and collect results
    championship_teams = []
    
    def on_model(model):
        nonlocal championship_teams
        championship_teams = []
        for atom in model.symbols(shown=True):
            if atom.name == "sec" and len(atom.arguments) == 1:
                team = str(atom.arguments[0])
                championship_teams.append(team)
    
    ctl.solve(on_model=on_model)
    
    return championship_teams

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    team_results = data.get('teams', {})
    
    try:
        championship_teams = solve_sec_championship(team_results)
        
        # Map team codes to full names
        team_names = {
            'tamu': 'Texas A&M',
            'bama': 'Alabama',
            'uga': 'Georgia',
            'miss': 'Ole Miss'
        }
        
        result_names = [team_names.get(team, team) for team in championship_teams]
        
        return jsonify({
            'success': True,
            'teams': result_names,
            'raw_teams': championship_teams
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/randomize', methods=['GET'])
def randomize():
    teams = ['tamu', 'bama', 'uga', 'miss']
    results = {}
    for team in teams:
        results[team] = random.choice(['win', 'loss'])
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
