# AutoRewarder

AutoRewarder is a Python script for automating search queries via Selenium WebDriver. The script generates unique search phrases, opens a browser, and simulates human typing (character-by-character with delays) to perform a sequence of searches.

# Purpose
Educational and research purposes — testing, experiments with automation, and simulating user behavior.

# ⚠️ IMPORTANT : 
the script can be used to attempt automatic point-earning in programs like Microsoft Rewards or other loyalty/reward programs that grant points for searches. Such use typically violates the terms of service of those platforms and may result in account suspension, loss of accumulated points, or other penalties.
The author does not encourage or support using the script to bypass rules, commit fraud, or gain unfair advantage. The script is provided only for educational and research purposes.

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
