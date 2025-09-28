# AutoRewarder

AutoRewarder is a Python script for automating search queries via Selenium WebDriver. The script generates unique search phrases, opens a browser, and simulates human typing (character-by-character with delays) to perform a sequence of searches.

# Purpose
Educational and research purposes — testing, experiments with automation, and simulating user behavior.

## ⚠️ IMPORTANT DISCLAIMER

This repository contains a search automation script provided **for educational and research purposes only**. The script *can be used* to automate web searches and may therefore be misused to attempt automatic point-earning in loyalty programs (for example Microsoft Rewards). Use of automation to interact with such services typically violates their Terms of Service and can result in account suspension, loss of points, or other penalties.

**The author does NOT encourage or support using this script to bypass service rules, commit fraud, or gain an unfair advantage.** You are solely responsible for any consequences resulting from your use of this code. Use it only in controlled environments, with accounts and systems you own or have explicit permission to test.

By using the code in this repository you acknowledge that:
- You have read and understood the Terms of Service of any platform you interact with.
- You will not use the code to violate those terms, to harm others, or to engage in illegal activity.


# Functionality
Generates unique search phrases from templates, topics, actions, and adjectives.
Simulates human typing: sends characters one-by-one with random delays.
Launches a browser via Selenium WebDriver (compatible with any browser that has a WebDriver).
Handles common Selenium errors and logs performed searches.
Allows configuring the number of searches per run.

# Handling browser processes
Before starting, the script attempts to terminate conflicting browser and driver processes to avoid issues with repeated sessions. The original code used taskkill for chrome.exe/chromedriver.exe; in the README this is described more generally as “browser/driver” because the user may use a different browser and its corresponding WebDriver.

# Notes and limitations
The script is intended only for educational and research use.
Any attempts to automate actions in commercial/user-facing services (for example, mass-earning points in Microsoft Rewards) are at your own risk and are likely to violate the service’s terms.
Do not run the script with elevated privileges (administrator/root) unless absolutely necessary — it is safer to run under a normal user account.

# Contact 
If you have any questions, issues, or suggestions — please open an issue on the repository
