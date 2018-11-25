from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

opts = Options()
opts.set_headless()

def main(url, filepath):
  driver = webdriver.Chrome('../chromedriver_linux64/chromedriver')
  driver.get(url)
  time.sleep(5)
  
  comments_button = driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/li[2]/button'
  )
  time.sleep(2)
  comments_button.click()

  html = driver.page_source
  with file(filepath, 'w+') as HTMLFile:
    HTMLFile.write(html.encode('utf-8'))

main(
  'https://www.instagram.com/p/BqfFwtdAexn/?hl=en',   # link to grab data
  '../html/artidote_singapore.html'                   # path where html should be saved
)
