from os.path import isfile, join, abspath
from pprint import pprint
from os import listdir    
import json
import csv


json_dir = abspath('./json/')
csv_dir  = abspath('./csv/')
json_filenames = [f for f in listdir(json_dir) if isfile((join(json_dir, f)))]


for json_filename in json_filenames:
  json_filepath = json_dir + "/" + json_filename
  csv_filepath  = csv_dir + "/" + json_filename[:-4] + "csv"

  with file(json_filepath) as json_file:
    json_data = json.load(json_file)
    caption       = json_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_media_to_caption']['edges'][0]['node']["text"]
    comment_count = json_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_media_to_comment']['count']
    comments      = json_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_media_to_comment']['edges']
    tagged_user = json_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_media_to_tagged_user']['edges'][0]['node']['user']

    get_comments


    pprint(caption)
    break

  # csv_filepath = abspath('./csv/'+jsonfile[:-4]+.csv
