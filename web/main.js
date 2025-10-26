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

        //await to decode collected response as JSON
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
        //kills
        bugKillsElement.textContent = String(`Terminids: ${bugKills.toLocaleString()}`);
        botKillsElement.textContent = String(`Automatons: ${botKills.toLocaleString()}`);
        squidKillsElement.textContent = String(`Illuminate: ${squidKills.toLocaleString()}`);
        overallKillsElement.textContent = String(`Overall Kills: ${overallKills.toLocaleString()}`);
        //missions
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

async function fetchMajorOrderData() {
    const contentArea = document.querySelector('.content-area');

    contentArea.innerHTML = '<h2>Loading Major Orders...</h2>'
    try {
        console.log('Fetching stats from /api/major_orders...');
        const response = await fetch('http://127.0.0.1:8000/api/major_orders');

        //check if network request was successful
        if (!response.ok) {
            throw new Error(`Network error: ${response.status}`);
            //sends error to catch block
        }

        //mo list
        const data = await response.json();

        if (data.length === 0) {
            contentArea.innerHTML = '<h2>No Active Major Orders</h2>';
            return;
        }

        let ordersHtml = '<h2>Active Major Orders</h2>';

        //mo list loop
        for (const order of data) {
            //adds expression to original value
            //build an MO card based on # of MOs
            ordersHtml += `
                <div class="mo-card">
                <h3>${order.order_title}</h3>
                <p>${order.order_briefing}</p>
                <p><strong>Expires:</strong> ${order.order_expires}</p>
                <p><strong>Reward:</strong> ${order.rewards_amount} Medals</p>

                <h4>Objectives</h4>
            `;

            //need to loop through # of tasks
            for (const task of order.tasks) {
                const percentage = ((task.progress / task.goal) * 100).toFixed(2); //2 decimal places toFixed(2)
                ordersHtml += `
                    <div class="task">
                        <p>${task.target_name}</p>
                        <p>${task.progress.toLocaleString()} / ${task.goal.toLocaleString()}</p>
                        <p><strong>Completion: ${percentage}%</strong></p>
                    </div>
                `;
            }

            ordersHtml += '</div>'; // close mo card
        }

        contentArea.innerHTML = ordersHtml; //loads final HTML (ordersHtml) into page


    } 
    catch (error) {
        console.error('Failed to fetch major orders:', error);
        contentArea.innerHTML = '<p style="color:red;">Error loading Major Orders.</p>';
    }
}

function siteNavigation() {
    //collect all links in sidebar
    const navLinks = document.querySelectorAll('.sidebar-nav a');

    navLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault();//stops browser's default behaviour
            
            const navTarget = link.getAttribute('href');

            if (navTarget === '#home') {
                fetchGalaxyStats();
            } else if (navTarget === '#planets') {
                fetchAllPlanets();
            } else if (navTarget === '#major_orders') {
                fetchMajorOrderData();
            } else if (navTarget === '#galaxy_stats') {
                fetchGalaxyStats();
            }
        })
    });
}