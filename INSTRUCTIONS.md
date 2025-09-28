# AutoRewarder — Installation & Usage Instructions

## 1. Requirements

Before running the script, make sure you have:

* Python **3.8** or higher installed.
* `pip` (Python package manager) available.
* A browser with a corresponding Selenium WebDriver installed (Chrome, Firefox, Edge, etc.).
* Basic knowledge of terminal/command line usage.

---

## 2. Installing Dependencies

Open a terminal/command prompt and run:

```bash
pip install selenium
```

This will install the required Selenium library for Python.

---

## 3. Setting Up WebDriver

The script works with any browser that supports Selenium WebDriver. Examples:

* **Google Chrome** → `ChromeDriver`
* **Mozilla Firefox** → `GeckoDriver`
* **Microsoft Edge** → `EdgeDriver`
* **Opera** → `OperaDriver`
* **Brave** → `ChromeDriver` (compatible with Chrome)

**Steps:**

1. Download the WebDriver for your browser and OS.

2. Place the driver in a folder you can access, for example:

   * **Windows:** `C:\WebDriver\chromedriver.exe`
   * **Linux/macOS:** `/usr/local/bin/chromedriver`

3. Make a note of the path — you will need it for the script configuration.

---

## 4. Configuring AutoRewarder

Open `auto_rewarder.py` in a text editor and update configuration variables as needed.

**Example configuration:**

```python
# Set the path to your browser profile (optional, for persistent sessions)
CHROME_PROFILE_PATH = r"C:\Users\YourUser\AppData\Local\SeleniumProfile"

# Set the path to your WebDriver
CHROMEDRIVER_PATH = r"C:\WebDriver\chromedriver.exe"
```

If you use a different browser, adjust variable names and paths accordingly.

---

## 5. Running the Script

Open a terminal in the folder where `auto_rewarder.py` is located and run:

```bash
python auto_rewarder.py
```

The script will open your browser and generate search queries, typing them automatically.

> The number of searches can be configured inside the script (default: `num_searches = 30`).

---

If something doesn't work, don't hesitate to write — I will respond.  
