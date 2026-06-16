from playwright.sync_api import sync_playwright # type: ignore
from login_tests import login

def add_mission( page ):    
    page.get_by_text("Attendance", exact=True).click()
    page.get_by_text("Transactions").click()
    page.get_by_role("link", name="Missions List", exact=True).click()
    page.get_by_role("button", name="Add").click()
    page.get_by_role("combobox", name="Employee Name").click()
    page.get_by_role("option", name="108 - Mohamed Essam Hassan").click()
    page.get_by_role("combobox", name="Mission Type").click()
    page.get_by_role("option", name="work from home").click()
    page.fill("#notes", "Test")


def report_




# add_mission("108","123456","yes")