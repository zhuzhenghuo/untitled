import time

from selenium import webdriver


browser=webdriver.Firefox()

browser.get("https://cn.bing.com/")

print(browser.title)
browser.find_element_by_id("sb_form_q").send_keys("鲁迅")
browser.find_element_by_id("sb_form_go").click()
time.sleep(10)
print(browser.current_url)
assert "登录" in browser.page_source
assert "bing" in browser.current_url
browser.quit()