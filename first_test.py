from playwright.sync_api import sync_playwright # type: ignore

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # الخطوة 1: افتح الموقع
    page.goto("https://www.saucedemo.com")
    print("الموقع اتفتح!")
    
    # الخطوة 2: اكتب اليوزر
    page.fill("#user-name", "standard_user")
    print("اليوزر اتكتب!")
    
    # الخطوة 3: اكتب الباسورد
    page.fill("#password", "secret_sauce")
    print("الباسورد اتكتب!")
    
    # الخطوة 4: اضغط Login
    page.click("#login-button")
    print("تم الضغط على Login!")
    
    # الخطوة 5: تأكد إن الصفحة الجديدة اتفتحت
    print("تم الدخول بنجاح!")
    
    browser.close()