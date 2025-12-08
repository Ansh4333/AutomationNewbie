import pyautogui
import webbrowser
import time
import csv
import os
import sys
import pygetwindow as gw

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.4

FALLBACK_COORDS = {
    "username": (600, 350),
    "password": (600, 420),
    "login": (600, 500),
}

if len(sys.argv) > 1:
    SCREENSHOT_FOLDER = sys.argv[1]
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SCREENSHOT_FOLDER = os.path.join(BASE_DIR, "screenshot")

if not os.path.isdir(SCREENSHOT_FOLDER):
    print("ERROR: Screenshot folder not found:", SCREENSHOT_FOLDER)
    sys.exit(1)

def debug_image_path(img_name):
    img_path = os.path.join(SCREENSHOT_FOLDER, img_name)
    print("Looking for image:", img_path)
    if not os.path.exists(img_path):
        print("  -> File does not exist on disk.")
    else:
        print("  -> File exists. Size (bytes):", os.path.getsize(img_path))
    return img_path

def wait_for_image(img_name, timeout=15, conf=0.6, retry_interval=1):
    img_path = debug_image_path(img_name)
    start = time.time()
    while time.time() - start < timeout:
        try:
            pos = pyautogui.locateOnScreen(img_path, confidence=conf)
            if pos:
                print(f"Found image '{img_name}' on screen at {pos}")
                return pyautogui.center(pos)
        except Exception as e:
            print(f"Exception while locating {img_name}: {e}")
        time.sleep(retry_interval)
    print(f"Could not locate image on screen: {img_name} after {timeout} seconds")
    return None

def safe_click(img_name, fallback_key=None, retries=3, conf=0.6):
    """Try clicking image — retry a few times, fallback to coords if needed."""
    for attempt in range(1, retries + 1):
        print(f"Attempt {attempt}/{retries} for {img_name}")
        pos = wait_for_image(img_name, timeout=10, conf=conf)
        if pos:
            pyautogui.click(pos)
            print(f"Clicked on image {img_name} at {pos}")
            return True
        else:
            print(f"Image {img_name} not found on attempt {attempt}")
            time.sleep(1)
    # After retries, fallback to coordinates if provided
    if fallback_key and fallback_key in FALLBACK_COORDS:
        x, y = FALLBACK_COORDS[fallback_key]
        print(f"Using fallback coordinates for {fallback_key}: ({x},{y})")
        pyautogui.click(x, y)
        return True
    print(f"Failed to click {img_name} after retries and no fallback")
    return False

def safe_type(text):
    pyautogui.typewrite(text, interval=0.05)

def switch_to_browser(tab_keyword="Login"):
    try:
        titles = gw.getAllTitles()
        for title in titles:
            if tab_keyword in title:
                gw.getWindowsWithTitle(title)[0].activate()
                time.sleep(1)
                print("Switched to browser tab:", title)
                return True
        for title in titles:
            if "Chrome" in title or "Mozilla" in title or "Firefox" in title:
                gw.getWindowsWithTitle(title)[0].activate()
                time.sleep(1)
                print("Switched to browser window:", title)
                return True
    except Exception as e:
        print("Browser focus switch failed:", e)
    print("Could not switch to browser — continuing")
    return False

def write_log(status):
    with open("automation_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), status])

def main():
    url = "https://the-internet.herokuapp.com/login"
    webbrowser.open(url)
    time.sleep(5)

    switch_to_browser(tab_keyword="The Internet")

    # Username
    if safe_click("username.png", "username", retries=3, conf=0.6):
        safe_type("tomsmith")
        time.sleep(0.5)
        pyautogui.press("tab")
    else:
        print("Failed at username — aborting")
        write_log("FAILED: username not found")
        return

    time.sleep(1)

    # Password
    if safe_click("password.png", "password", retries=3, conf=0.6):
        safe_type("SuperSecretPassword!")
        time.sleep(0.5)
        pyautogui.press("tab")
    else:
        print("Failed at password — aborting")
        write_log("FAILED: password not found")
        return

    time.sleep(1)

    # Login
    if safe_click("login.png", "login", retries=3, conf=0.6):
        print("Clicked login")
    else:
        print("Failed to click login — aborting")
        write_log("FAILED: login button not found/click failed")
        return

    time.sleep(4)

    # Final screenshot and log
    pyautogui.screenshot("result.png")
    write_log("SUCCESS: Login Completed")
    print("Automation Completed Successfully")

if __name__ == "__main__":
    main()
