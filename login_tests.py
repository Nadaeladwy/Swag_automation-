from playwright.sync_api import sync_playwright
import time

def run_test(test_name, username, password, expected):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.fill("#user-name", username)
        page.fill("#password", password)
        page.click("#login-button")
        time.sleep(3)
        print(f"Test: {test_name} - {expected}")
        browser.close()

# Test 1: Valid user name and Pass
run_test("Happy Path", "standard_user", "secret_sauce", "  login successfully ")

# Test 2: Invalid user name 
run_test("Wrong Username", "wrong_user", "secret_sauce", "Fail login")

# Test 3: Invalid pass
run_test("Wrong Password", "standard_user", "wrong_pass", "Fail login")

# Test 4: Empty fileds 
run_test("Empty Fields", "", "", "Fail login")

# Test 5: Locked user
run_test("Locked User", "locked_out_user", "secret_sauce", "Fail login")
