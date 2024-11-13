# LinkedIn Connection Automation Script

This script automates the sending of personalized LinkedIn connection requests. It searches for recruiters at specified companies and sends a connection request with a custom message.

## Prerequisites

1. **Google Chrome**: Make sure Google Chrome is installed on your computer.

2. **ChromeDriver**: Download ChromeDriver compatible with your version of Chrome:
   - Visit the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/).
   - Download the version that matches your Chrome version.
   - Extract the file and note its path; you’ll need it later.

3. **Python**: Ensure Python is installed. You can download it from [python.org](https://www.python.org/downloads/).

4. **Selenium Library**: Install Selenium via pip:
   ```bash
   pip install selenium
## Setup

1. **Clone or Download the Repository**:
   - Clone this GitHub repository or download the code to your local machine.

2. **Specify the Path to ChromeDriver**:
   - Update the `chrome_service` path in the code to the location where you saved `chromedriver.exe`:
     ```python
     chrome_service = Service('D:/software/chromedriver-win64/chromedriver.exe')
     ```

3. **Specify the Path to Chrome**:
   - Set the path to your Chrome browser in `chrome_options.binary_location`:
     ```python
     chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
     ```

4. **Specify Your Chrome Profile Path**:
   - Use your Chrome user profile path to stay logged into LinkedIn. Replace `"user-data-dir=C:/Users/yourname/AppData/Local/Google/Chrome/User Data"` with your own profile folder path.

## How It Works

1. The script opens Chrome with your user profile, logging into LinkedIn.
2. It searches for LinkedIn recruiters at each specified company.
3. For each recruiter, it:
   - Clicks the "Connect" button.
   - Adds a personalized message.
   - Sends the connection request.

4. **Error Handling**:
   - The script skips recruiters if an error occurs and logs an error message.

5. Once all connection requests are sent, the script automatically closes the browser.

## Troubleshooting

- **ChromeDriver Version Compatibility**: Ensure your ChromeDriver version matches your Chrome browser version.
- **LinkedIn Captchas**: Excessive use of this script may trigger captchas. Use responsibly to avoid account restrictions.
