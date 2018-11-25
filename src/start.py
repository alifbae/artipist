from insta_scraper import run_scraper
import os.path
import csv

links_filepath = os.path.abspath("./links.csv")

with file(links_filepath) as links_csv:
  csv_file = csv.reader(links_csv, delimiter=',')
  next(csv_file, None)  # skip the headers
  
  for row in csv_file:
    city_name = row[0]
    url = row[1]
    
    run_scraper(url, city_name)
    


# run_scraper(url, html_file_output)
# # insert path to html file from which you want json
