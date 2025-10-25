document.addEventListener('DOMContentLoaded', main)

function main() {
    console.log('The page is loaded. Running main.js...')
    fetchGalaxyStats();
}

// 
async function fetchGalaxyStats() {
    //'try' and 'catch' are similar to 'try' and 'except'
    try {
        console.log('Fetching stats from /api/galaxy_stats...');
        const response = await fetch('http://127.0.0.1:8000/api/galaxy_stats');

        //check if network request was successful
        if (!response.ok) {
            throw new Error(`Network error: ${response.status}`);
            //sends error to catch block
        }

        //await decode collected response as JSON
        const data = await response.json();
        console.log('Sucessfully fetched data:', data);

        //find HTML elements by name
        const bugKillsElement = document.getElementById('stats-bug-kills');
        const botKillsElement = document.getElementById('stats-bot-kills');
        const squidKillsElement = document.getElementById('stats-squid-kills');
        const overallKillsElement = document.getElementById('stats-overall-kills');
        const missionsWonElement = document.getElementById('stats-total-missions-won');
        const missionsLostElement = document.getElementById('stats-total-missions-lost');
        const missionsWinPercentElement = document.getElementById('stats-missions-wl-ratio');

        //KILLS DATA
        const bugKills = data.bugKills || 0; // || defaults to 0 if no stats can be found.
        const botKills = data.automatonKills || 0;
        const squidKills = data.illuminateKills || 0;
        const overallKills = bugKills+botKills+squidKills;
        bugKillsElement.classList.add('terminid-color');
        botKillsElement.classList.add('automaton-color');
        squidKillsElement.classList.add('illuminate-color');

        const missionsWon = data.missionsWon || 0;
        const missionsLost = data.missionsLost || 0;
        const missionsTotal = missionsWon + missionsLost;
        const missionsWinPercent = (missionsWon / missionsTotal) * 100;


        //update element text
        bugKillsElement.textContent = String(`Terminids: ${bugKills.toLocaleString()}`);
        botKillsElement.textContent = String(`Automatons: ${botKills.toLocaleString()}`);
        squidKillsElement.textContent = String(`Illuminate: ${squidKills.toLocaleString()}`);
        overallKillsElement.textContent = String(`Overall Kills: ${overallKills.toLocaleString()}`);
        missionsWonElement.textContent = String(`Missions Won: ${missionsWon.toLocaleString()}`);
        missionsLostElement.textContent = String(`Missions Lost: ${missionsLost.toLocaleString()}`);
        missionsWinPercentElement.textContent = String(`Win Percentage: ${missionsWinPercent.toLocaleString()}%`)
    }

    catch (error) {
        //if try block fails, execute catch block
        console.error('Failed to fetch stats:', error);

        //updating page to show an error
        const statsLayout = document.querySelector('.stats-layout')
        statsLayout.innerHTML = '<p style="color: red;">Error: Could not load Galactic War stats. Is the API running?</p>';
    }
}