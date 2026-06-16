from playwright.sync_api import sync_playwright # type: ignore
import time


def login(test_name,username,password,expected,url):
    # with sync_playwright() as p:
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url, wait_until="domcontentloaded",timeout=60000)
    page.fill("#user-name",username)
    page.fill("#password",password)
    page.click("#login-button")
    time.sleep(1)
    print(f"Test: {test_name}-{expected}")
    return page

 # Test 1: Valid user name and Pass
##login("Happy Path", "standard_user", "secret_sauce", "  login successfully " , "https://www.saucedemo.com/")

# # Test 2: Invalid user name 
# login("Wrong Username", "wrong_user", "secret_sauce", "Fail login")

# # Test 3: Invalid pass
# login("Wrong Password", "standard_user", "wrong_pass", "Fail login")

# # Test 4: Empty fileds 
# login("Empty Fields", "", "", "Fail login")

# # Test 5: Locked user
# login("Locked User", "locked_out_user", "secret_sauce", "Fail login")
