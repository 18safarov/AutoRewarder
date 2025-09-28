import os
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, WebDriverException

# ---------------- CONFIG ---------------- #
# Chrome profile path
CHROME_PROFILE_PATH = os.path.join(
    os.environ['USERPROFILE'],
    'AppData', 
    'Local', 
    'SeleniumProfile'
)

# chromedriver path
CHROMEDRIVER_PATH = os.path.join(
    os.environ['USERPROFILE'],
    'desktop', 
    'python',
    'AutoRewarder',
    'chromedriver-win64',
    'chromedriver.exe'
)

# ---------------- PHRASES ---------------- #
templates = [
    "How to {action} {topic} effectively?",
    "Tips to {action} a {adj} {topic}",
    "Best ways to {action} {topic} quickly",
    "Can you {action} {adj} {topic}?",
    "Why {topic} is considered {adj} when you {action} it",
    "Learn how to {action} your {adj} {topic}",
    "The secret to {action} {topic} like a pro",
    "Top 10 methods to {action} {adj} {topic}",
    "Why people {action} {topic} in a {adj} way",
    "How {adj} {topic} can be {action}ed easily"
]

topics = [
    "Python programming", "machine learning", "data science", "web development", "cybersecurity",
    "cloud computing", "mobile apps", "artificial intelligence", "blockchain technology", "game development",
    "networking basics", "database management", "robotics", "quantum computing", "virtual reality",
    "augmented reality", "software testing", "UI/UX design", "digital marketing", "big data analytics",
    "cryptocurrency", "deep learning", "computer vision", "natural language processing", "software architecture",
    "devops practices", "microservices", "internet of things", "ethical hacking", "computer graphics"
]

actions = [
    "improve", "optimize", "learn", "master", "debug",
    "build", "deploy", "test", "design", "implement",
    "secure", "configure", "upgrade", "monitor", "maintain",
    "scale", "automate", "analyze", "visualize", "code",
    "refactor", "document", "integrate", "manage", "debug",
    "train", "simulate", "calculate", "explore", "develop"
]

adjectives = [
    "efficient", "scalable", "secure", "fast", "robust",
    "modern", "user-friendly", "advanced", "innovative", "flexible",
    "dynamic", "interactive", "reliable", "optimized", "custom",
    "smart", "powerful", "intuitive", "clean", "responsive",
    "lightweight", "modular", "agile", "versatile", "stable",
    "professional", "cutting-edge", "automated", "effective", "streamlined"
]

# track used phrases to avoid duplicates
used_phrases = set()

def generate_unique_phrase():
    # generate unique search phrases using templates, topics, actions, and adjectives
    while True:
        template = random.choice(templates)
        topic = random.choice(topics)
        action = random.choice(actions)
        adj = random.choice(adjectives)
        phrase = template.format(topic=topic, action=action, adj=adj)
        if phrase not in used_phrases:
            used_phrases.add(phrase)
            return phrase

def human_typing(element, text):
    # simulate human-like typing
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.18))  # delay between key presses

def setup_driver():
    # selinium moment :)
    options = Options()
    options.add_argument(f"--user-data-dir={CHROME_PROFILE_PATH}")
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def perform_searches(driver, num_searches=30):
    # the main loop to perform searches(loop 30 times - 90 points)
    for i in range(num_searches):
        try:
            driver.get("https://www.bing.com")
            time.sleep(random.uniform(3, 6))

            search_box = driver.find_element("name", "q")
            search_box.clear()

            query = generate_unique_phrase()
            print(f"Search #{i + 1}: {query}")

            human_typing(search_box, query)
            search_box.send_keys(Keys.RETURN)

            time.sleep(random.uniform(5, 10))
        except NoSuchElementException:
            print(f"[ERROR] Search box not found on attempt #{i+1}")
        except WebDriverException as e:
            print(f"[ERROR] WebDriver exception on attempt #{i+1}: {e}")
        except Exception as e:
            print(f"[ERROR] Unexpected exception on attempt #{i+1}: {e}")

def close_running_chrome():
    # close any chrome and chromedriver processes
    os.system("taskkill /f /im chrome.exe >nul 2>&1")
    os.system("taskkill /f /im chromedriver.exe >nul 2>&1")
    time.sleep(3)

def main():
    # main function to run the script
    print("Starting AutoRewarder...")
    close_running_chrome()
    driver = setup_driver()
    try:
        perform_searches(driver, num_searches=30)
    finally:
        driver.quit()

# standard entry point for the script
if __name__ == "__main__":

    main()
