from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from html_parser import parse_file
import time
import os.path


opts = Options()
opts.set_headless()

def get_source_with_comments(url):
  driver = webdriver.Chrome('/home/alif/Code/projects/artipist/chromedriver_linux64/chromedriver')
  driver.get(url)

  try:
    time.sleep(3)
    comments_button = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/li[2]/button'
    )
    time.sleep(2)
    while comments_button:
      comments_button.click()
      comments_button = driver.find_element_by_xpath(
          '//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/li[2]/button'
      )
      time.sleep(1)
  except (NoSuchElementException, StaleElementReferenceException), e:
    page_source = driver.page_source
    driver.close()
    return page_source

def write_to_html_file(page_source, filepath):
  with file(filepath, 'w+') as html_file:
    html_file.write(page_source.encode('utf-8'))


def run_scraper(url, city_name):
  source = get_source_with_comments(url)
  html_output_filepath = os.path.abspath('./html/artidote_'+city_name+'.html')
  write_to_html_file(source, html_output_filepath)
  parse_file(html_output_filepath, city_name)

  


