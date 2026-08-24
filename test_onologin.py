# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import re
from playwright.sync_api import Playwright, sync_playwright, expect

def test_onologin(playwright: Playwright):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://dev-mos.onoark.com/languageSelection")
    page.get_by_role("heading",name="En").click()
    page.get_by_role("textbox").fill("1000000000 ")
    page.get_by_role("button", name="LOGIN").click()
    page.get_by_role("textbox").fill("123456")
    page.get_by_role("button", name="CONTINUE").click()
    page.screenshot(path="success_screenshot.png")
    # ---------------------
    context.close()
    browser.close()



# Press the green button in the gutter to run the script.
with sync_playwright() as playwright:
    test_onologin(playwright)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
