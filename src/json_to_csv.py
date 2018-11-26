from os.path import isfile, join, abspath
from datetime import datetime
from pprint import pprint
from json_byteified import json_load_byteified
from os import listdir    
import json
import csv

# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
# ts = int("1284101485")
# print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))


def get_comments(json_data):
  comments = json_data['entry_data']['PostPage'][0]['graphql'][
    'shortcode_media']['edge_media_to_comment']['edges']
  
  comments_list = []
  for comment in comments:
    dt = lambda created_at : datetime.utcfromtimestamp(
      int(created_at)).strftime('%Y-%m-%d %H:%M:%S')
    
    comment_hash = dict(
      comment_text = comment['node']['text'],
      username     = comment['node']['owner']['username'], 
      created_at   = dt(comment['node']['created_at'])
    )
    comments_list.append(comment_hash)
  return comments_list

def get_caption(json_data):
  caption = json_data['entry_data']['PostPage'][0]['graphql'][
    'shortcode_media']['edge_media_to_caption']['edges'][0]['node']["text"]
  return caption

def get_tagged_user(json_data):
  try:
    tagged_user = json_data['entry_data']['PostPage'][0]['graphql'][
        'shortcode_media']['edge_media_to_tagged_user']['edges'][0]['node']['user']
    return tagged_user
  except IndexError:
    return

def main():
  json_dir = './json/'
  csv_dir  = './csv/'
  json_filenames = [f for f in listdir(json_dir) if isfile((join(json_dir, f)))]
  
  for json_filename in json_filenames:
    json_filepath = json_dir + "/" + json_filename
    csv_filepath  = csv_dir + "/" + json_filename[:-4] + "csv"

    # make hash from json
    with file(json_filepath) as json_file:
      json_data   = json_load_byteified(json_file)
      caption     = get_caption(json_data)
      comments    = get_comments(json_data)
      # tagged_user = get_tagged_user(json_data) 

      # make csv
      with file(csv_filepath, 'w+') as csv_file:
        print "...writing " + json_filename[:-4] + "csv"
        headings = ['username', 'created_at', 'comment_text']
        writer = csv.DictWriter(
            csv_file, fieldnames=headings, delimiter=',', quotechar='"', 
            quoting=csv.QUOTE_ALL, skipinitialspace=True)
        writer.writeheader()
        for comment in comments:
          writer.writerow(comment)

main()
