// Intelligent Online Exam Proctoring System - Web Demo
// Interactive JavaScript for the live demo

let isMonitoring = false;
let sessionStartTime = null;
let timerInterval = null;
let currentScenario = 'normal';

// Demo scenarios with different monitoring states
const scenarios = {
    normal: {
        face: { status: 'Normal', class: 'status-normal' },
        eye: { status: 'Focused', class: 'status-normal' },
        head: { status: 'Proper Position', class: 'status-normal' },
        object: { status: 'Clear', class: 'status-normal' },
        audio: { status: 'Quiet', class: 'status-normal' },
        demoText: '✅ Student properly positioned and focused',
        alert: false
    },
    no_face: {
        face: { status: 'No Face Detected!', class: 'status-alert' },
        eye: { status: 'Not Detected', class: 'status-alert' },
        head: { status: 'Not Detected', class: 'status-alert' },
        object: { status: 'Clear', class: 'status-normal' },
        audio: { status: 'Quiet', class: 'status-normal' },
        demoText: '❌ No student face detected in frame',
        alert: true
    },
    multiple_faces: {
        face: { status: 'Multiple Faces!', class: 'status-alert' },
        eye: { status: 'Multiple Sources', class: 'status-alert' },
        head: { status: 'Multiple Positions', class: 'status-alert' },
        object: { status: 'Clear', class: 'status-normal' },
        audio: { status: 'Voices Detected', class: 'status-alert' },
        demoText: '⚠️ Multiple people detected in exam area',
        alert: true
    },
    suspicious: {
        face: { status: 'Looking Away', class: 'status-alert' },
        eye: { status: 'Not Focused', class: 'status-alert' },
        head: { status: 'Turned Away', class: 'status-alert' },
        object: { status: 'Phone Detected!', class: 'status-alert' },
        audio: { status: 'Suspicious Sounds', class: 'status-alert' },
        demoText: '🚨 Suspicious activity: Phone detected, student looking away',
        alert: true
    }
};

function startDemo() {
    if (!isMonitoring) {
        isMonitoring = true;
        sessionStartTime = new Date();
        startTimer();
        
        // Initialize with normal scenario
        simulateScenario('normal');
        
        // Update button text
        const startBtn = document.querySelector('.btn-primary');
        startBtn.textContent = 'Stop Proctoring';
        startBtn.onclick = stopDemo;
        
        console.log('Proctoring demo started');
    }
}

function stopDemo() {
    isMonitoring = false;
    clearInterval(timerInterval);
    
    // Reset all statuses
    resetStatuses();
    
    // Update button text
    const startBtn = document.querySelector('.btn-primary');
    startBtn.textContent = 'Start Proctoring';
    startBtn.onclick = startDemo;
    
    // Hide alert
    document.getElementById('alertBox').classList.remove('show');
    
    console.log('Proctoring demo stopped');
}

function simulateScenario(scenarioName) {
    if (!isMonitoring && scenarioName !== 'normal') {
        alert('Please start the proctoring demo first!');
        return;
    }
    
    currentScenario = scenarioName;
    const scenario = scenarios[scenarioName];
    
    // Update status displays
    updateStatus('faceStatus', scenario.face);
    updateStatus('eyeStatus', scenario.eye);
    updateStatus('headStatus', scenario.head);
    updateStatus('objectStatus', scenario.object);
    updateStatus('audioStatus', scenario.audio);
    
    // Update demo text
    document.getElementById('demoText').textContent = scenario.demoText;
    
    // Show/hide alert
    const alertBox = document.getElementById('alertBox');
    if (scenario.alert) {
        alertBox.classList.add('show');
        // Add some dynamic alert messages
        const alertMessages = [
            '🚨 ALERT: Suspicious activity detected!',
            '⚠️ WARNING: Exam integrity violation!',
            '🔴 ATTENTION: Unauthorized behavior detected!',
            '📢 NOTICE: Please return to proper exam position!'
        ];
        alertBox.textContent = alertMessages[Math.floor(Math.random() * alertMessages.length)];
    } else {
        alertBox.classList.remove('show');
    }
    
    console.log(`Scenario changed to: ${scenarioName}`);
}

function updateStatus(elementId, statusObj) {
    const element = document.getElementById(elementId);
    element.textContent = statusObj.status;
    element.className = statusObj.class;
}

function resetStatuses() {
    const statusElements = ['faceStatus', 'eyeStatus', 'headStatus', 'objectStatus', 'audioStatus'];
    statusElements.forEach(id => {
        const element = document.getElementById(id);
        element.textContent = 'Ready';
        element.className = 'status-normal';
    });
    
    document.getElementById('timeStatus').textContent = '00:00:00';
    document.getElementById('demoText').textContent = 'Click "Start Proctoring" to begin the demo';
}

function startTimer() {
    timerInterval = setInterval(() => {
        if (sessionStartTime) {
            const now = new Date();
            const elapsed = Math.floor((now - sessionStartTime) / 1000);
            const hours = Math.floor(elapsed / 3600).toString().padStart(2, '0');
            const minutes = Math.floor((elapsed % 3600) / 60).toString().padStart(2, '0');
            const seconds = (elapsed % 60).toString().padStart(2, '0');
            
            document.getElementById('timeStatus').textContent = `${hours}:${minutes}:${seconds}`;
        }
    }, 1000);
}

// Add some interactive effects
document.addEventListener('DOMContentLoaded', function() {
    // Add hover effects to feature cards
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
    
    // Add click effects to buttons
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = '';
            }, 150);
        });
    });
    
    console.log('Intelligent Online Exam Proctoring System - Web Demo Loaded');
    console.log('Created by: Amar Avenkatesh');
    console.log('GitHub: https://github.com/amaravenkatesh45/Intelligent-Exam-Proctoring-System');
});

// Auto-demo mode (optional - cycles through scenarios)
function startAutoDemo() {
    if (!isMonitoring) return;
    
    const scenarioKeys = Object.keys(scenarios);
    let currentIndex = 0;
    
    setInterval(() => {
        if (isMonitoring) {
            simulateScenario(scenarioKeys[currentIndex]);
            currentIndex = (currentIndex + 1) % scenarioKeys.length;
        }
    }, 5000); // Change scenario every 5 seconds
}

// Keyboard shortcuts
document.addEventListener('keydown', function(event) {
    if (event.ctrlKey) {
        switch(event.key) {
            case '1':
                event.preventDefault();
                simulateScenario('normal');
                break;
            case '2':
                event.preventDefault();
                simulateScenario('no_face');
                break;
            case '3':
                event.preventDefault();
                simulateScenario('multiple_faces');
                break;
            case '4':
                event.preventDefault();
                simulateScenario('suspicious');
                break;
        }
    }
});
