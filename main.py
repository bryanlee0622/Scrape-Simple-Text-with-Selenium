from selenium import webdriver
import time

def get_driver():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()  # Use Chrome browser
  #options = webdriver.EdgeOptions()    # Use Edge browser
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)    # Use Chrome browser
  #driver = webdriver.Edge(options=options)      # Use Edge browser
  driver.get("http://automated.pythonanywhere.com")
  return driver

def clean_text(text):
  """Extract only the temperature from text"""
  output = float(text.split(": ")[1])
  return output

def main():
  driver = get_driver()
  time.sleep(2)
  element1 = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
  element2 = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  return element1.text, element2.text
  #return clean_text(element.text)

text1, text2 = main()

print(text1)
print(text2)
print(clean_text(text2))
