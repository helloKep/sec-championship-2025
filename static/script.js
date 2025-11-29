// Team results state
const teamResults = {
    tamu: 'win',
    bama: 'win',
    uga: 'win',
    miss: 'win'
};

// Initialize toggle buttons
document.addEventListener('DOMContentLoaded', () => {
    initializeToggles();
    setupEventListeners();
});

function initializeToggles() {
    const teamRows = document.querySelectorAll('.team-row');
    
    teamRows.forEach(row => {
        const team = row.dataset.team;
        const toggleButtons = row.querySelectorAll('.toggle-btn');
        
        toggleButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                const result = btn.dataset.result;
                
                // Update active state
                toggleButtons.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                
                // Update state
                teamResults[team] = result;
            });
        });
    });
}

function setupEventListeners() {
    // Go button
    document.getElementById('go-btn').addEventListener('click', runSimulation);
    
    // Randomize button
    document.getElementById('randomize-btn').addEventListener('click', randomizeResults);
}

async function randomizeResults() {
    try {
        const response = await fetch('/randomize');
        const data = await response.json();
        
        // Update UI and state based on randomized results
        Object.keys(data).forEach(team => {
            const result = data[team];
            teamResults[team] = result;
            
            // Update button states
            const teamRow = document.querySelector(`.team-row[data-team="${team}"]`);
            const buttons = teamRow.querySelectorAll('.toggle-btn');
            
            buttons.forEach(btn => {
                if (btn.dataset.result === result) {
                    btn.classList.add('active');
                } else {
                    btn.classList.remove('active');
                }
            });
        });
        
        // Hide any previous results
        hideResults();
        hideError();
        
    } catch (error) {
        showError('Failed to randomize results. Please try again.');
    }
}

async function runSimulation() {
    hideResults();
    hideError();
    
    try {
        const response = await fetch('/simulate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ teams: teamResults })
        });
        
        const data = await response.json();
        
        if (data.success) {
            showResults(data.teams);
        } else {
            showError(data.error || 'Simulation failed. Please try again.');
        }
        
    } catch (error) {
        showError('Network error. Please check your connection and try again.');
    }
}

function showResults(teams) {
    const resultsSection = document.getElementById('results-section');
    const resultsContent = document.getElementById('results-content');

    console.log(teams)
    console.log(teams[0].replace(/[^A-Z0-9]/ig, "_"))
    
    if (teams.length === 2) {
        resultsContent.innerHTML = `
            <div class="championship-${teams[0].replace(/[^A-Z0-9]/ig, "_")}">${teams[0]}</div>
            <div class="vs-text">vs</div>
            <div class="championship-${teams[1].replace(/[^A-Z0-9]/ig, "_")}">${teams[1]}</div>
        `;
    } else if (teams.length === 1) {
        resultsContent.innerHTML = `
            <div class="championship-team">${teams[0]}</div>
            <p style="margin-top: 15px; color: #666;">Only one team qualifies under these conditions.</p>
        `;
    } else if (teams.length === 0) {
        resultsContent.innerHTML = `
            <p style="color: #666;">No teams qualify for the championship under these conditions.</p>
        `;
    } else {
        // More than 2 teams
        const teamsHTML = teams.map(team => `
            <div class="championship-team">${team}</div>
        `).join('');
        resultsContent.innerHTML = `
            ${teamsHTML}
            <p style="margin-top: 15px; color: #666;">Multiple scenarios possible.</p>
        `;
    }
    
    resultsSection.classList.remove('hidden');
}

function hideResults() {
    const resultsSection = document.getElementById('results-section');
    resultsSection.classList.add('hidden');
}

function showError(message) {
    const errorSection = document.getElementById('error-section');
    const errorMessage = document.getElementById('error-message');
    
    errorMessage.textContent = message;
    errorSection.classList.remove('hidden');
}

function hideError() {
    const errorSection = document.getElementById('error-section');
    errorSection.classList.add('hidden');
}
