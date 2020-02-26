#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import json
import os
import time
import uuid

# Entrance
if __name__ == '__main__':
  # Read config file
  with open('./config.json', 'r') as f:
    config = json.load(f)
  print(config)

  # Load Chrome drive
  wd = webdriver.Chrome(config['web_drive_path'])

  # Access the baidu.com
  wd.get('http://image.baidu.com')

  # Upload an image and use it to search
  img_f = os.path.join(config['image_data_dir'], 'lions.png')
  img_f = r'C:\Users\dxl\Desktop\Web_TestSuite\data\lions.png'
  wd.find_element_by_id('stfile').send_keys(img_f)
  wd.find_element_by_id('uploadImg').click()

  wd.execute_script('window.alert("Enjoy with Selenium testing!")')