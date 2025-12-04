🚀 Auto SpeedTester

A lightweight, automated Python script to monitor your internet connection speed at set intervals. Perfect for logging performance over time or troubleshooting intermittent network issues, all from the comfort of your terminal.

⚡ Features
Automated Monitoring: Runs indefinitely until you tell it to stop.

Custom Intervals: You choose how often the test runs (in minutes).

Detailed Metrics: Checks Download, Upload, and automatically selects the best server based on Ping.

Robust Error Handling: Automatically retries after 60 seconds if the network drops, ensuring the script doesn't crash.

Retro Aesthetics: Features a cool ASCII art banner on startup.

🛠️ Installation
1. Clone the repository

git clone https://github.com/YOUR_USERNAME/REPO_NAME.git

2. Install Dependencies
This script relies on the speedtest-cli library. Install it using pip:

pip install speedtest-cli

💻 Usage
Run the script using Python:

python main.py

How it works:
Launch: The script will display a banner and initialize the speed test client.

Input: Enter the interval (in minutes) you want to wait between tests.

Run: The script will output your current speeds and countdown to the next test.

⚠️ Data Usage Warning
Please be aware that running speed tests frequently consumes data.

Recommended Interval: For 24/7 monitoring, an interval of 60 minutes or more is usually sufficient.

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

📝 License
Distributed under the MIT License. See LICENSE for more information.
