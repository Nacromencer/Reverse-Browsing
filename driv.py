from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
website = input()
driver.get("http://www." + website)

xpath = input()
def click(elem):
	elem.click()
	time.sleep(5)
	with open('page.html', 'w') as f:
	    f.write(driver.page_source)
def action(elem,keys):
	elem.clear()
	elem.send_keys(keys)
	elem.submit()



def f(xpath):
	try:
		func, path, keys = xpath.split(" ")
		elem = driver.find_element_by_xpath(path)
		# elem = driver.find_element_by_class_name()
		if func == 'click':
			click(elem)
		elif func == 'action':
			action(elem, keys)
	except:
		pass
	xpath = input()
	f(xpath)
f(xpath)
assert "No results found." not in driver.page_source
# driver.close()
# action //*[@id="lst-ib"] whatismyip