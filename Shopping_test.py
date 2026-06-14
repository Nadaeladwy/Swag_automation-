from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        print("Opened")
        time.sleep(3)


        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")

        page.click("#login-button")
    
        print ("Loged in")
        time.sleep(3)
#Add item in cartحغ
        page.click("#add-to-cart-sauce-labs-backpack")
        print("Added Item")
        time.sleep(2)
        page.click("#add-to-cart-sauce-labs-bike-light")
        print("Added Item")
        time.sleep(2)
        page.click("#add-to-cart-sauce-labs-bolt-t-shirt")
        print("Added Item")
        time.sleep(2)
#validate the itme in cart 
        page.click(".shopping_cart_link")
        print(" Cart Opned!")
        time.sleep(2)
        item =page.query_selector_all(".inventory_item_name")
        print(f"All times in cart: {len(item)}")
        time.sleep(2)
    # Checout 
        page.click ("#checkout")
        page.fill ("#first-name","Nada")
        page.fill ("#last-name", "Saleh")
        page.fill ("#postal-code","123456")
        time.sleep(1)
        page.click("#continue")
        #Check the peymnet information 
        payment=page.text_content(".summary_info_label")
        print(f"Checked payemnt are done:{payment}")
        page.click("#finish")
        print ("Thank you")
        time.sleep(1)

        browser.close()

