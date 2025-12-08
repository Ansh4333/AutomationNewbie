# PyAutoGUI Login Automation

Automate login to a demo site using mouse/keyboard simulation, with image detection + fallback coordinates + retry logic.

##  Demo Website Used

**the‑internet.herokuapp.com** — a public demo site offering various UI/behavior examples (login page, dynamic content, alerts, forms, shifting content, etc.)

---

## When To Use This Automation Approach (PyAutoGUI / GUI Automation)

This automation style is useful when:

- Traditional automation tools (like Selenium / Playwright) are blocked or unreliable.  
- You need to simulate realistic user interactions (mouse + keyboard) rather than interacting via DOM / APIs.  
- You are working with web pages that have dynamic IDs, shifting content, or UI elements that are hard to locate with standard selectors.  
- You need fallback methods (image‑based detection, coordinate click, retry logic) to handle UI variability.  
- You want to automate desktop‑level workflows or hybrid workflows where GUI automation matters.  


---

##  Challenges & Limitations

Because this is GUI‑based, you must accept some constraints:

- **Screen visibility required** — the browser (or relevant window) must remain visible and in focus. Minimizing or covering the window may break automation.  
- **Resolution / UI scaling sensitivity** — if screen resolution, zoom, or UI layout changes compared to when screenshots were taken, image‑matching or hard‑coded coordinates may fail.  
- **Dependence on static assets (screenshots)** — you need correct, up‑to‑date screenshots of elements (buttons, fields) for detection to work reliably.  
- **Timing and loading delays** — if page loads slowly or elements render dynamically, you need waits/retries; otherwise clicks or typing may fail.  
- **Not suitable for highly dynamic or protected sites** (with CAPTCHAs, frequent layout changes, or heavy JS) — such sites may break image‑based automation.  
- **Limited portability across devices** — script may work on one display setup but fail on another, due to variations in UI scale, resolution, OS, browser theme, etc.  
## What it does

- Opens browser and navigates to login page  
- Focuses the browser window automatically  
- Finds username / password fields and Login button by screenshot (image matching)  
- Falls back to fixed coordinates if image detection fails  
- Retries detection if screen elements load slowly  
- Types login credentials, clicks Login, then saves a result screenshot & logs the attempt  

## How to run

```bash
# Install dependencies
pip install pyautogui opencv‑python

# Run script
python automation.py
