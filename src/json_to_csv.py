from os.path import isfile, join, abspath
from datetime import datetime
from pprint import pprint
from json_byteified import json_load_byteified
from os import listdir    
import json
import csv


ts = int("1284101485")

# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))



def get_comments(comments):
  comment_list = []
  for comment in comments:
    dt = datetime.utcfromtimestamp(
      int(comment['node']['created_at'])).strftime('%Y-%m-%d %H:%M:%S')
    
    print dt
  return



def main():
  json_dir = abspath('./json/')
  csv_dir  = abspath('./csv/')
  json_filenames = [f for f in listdir(json_dir) if isfile((join(json_dir, f)))]
  
  for json_filename in json_filenames:
    json_filepath = json_dir + "/" + json_filename
    csv_filepath  = csv_dir + "/" + json_filename[:-4] + "csv"

    with file(json_filepath) as json_file:
      json_data = json_load_byteified(json_file)
      caption             = json_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_media_to_caption']['edges'][0]['node']["text"]
      comment_count       = json_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_media_to_comment']['count']
      comments_json       = json_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_media_to_comment']['edges']
      tagged_user_json    = json_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_media_to_tagged_user']['edges'][0]['node']['user']

      get_comments(comments_json)
      # pprint(caption)
      break

main()
