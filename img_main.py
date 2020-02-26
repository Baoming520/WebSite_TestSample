#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import json
import os
import time
import uuid

def validate(v_elem, expectation):
  exp_texts = expectation.split()
  flag = False
  for exp_text in exp_texts:
    if exp_text in v_elem.text:
      flag = True
      break
  return flag

def main(argv=None):
  # Read config file
  with open('./config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
  print(config)

  # Load Chrome drive
  wd = webdriver.Chrome(config['web_drive_path'])

  # Access the baidu.com
  wd.get('http://image.baidu.com')

  imgs = config['images']
  for img in imgs:
    # Upload an image and use it to search
    img_f = img['image_path']
    img_c = img['category']
    img_l = img['label']
    res_out = img['output_file']
    wd.find_element_by_id('stfile').send_keys(img_f)

    # Sleep 3 secends to wait for loading html elements
    time.sleep(3)

    v_elem = wd.find_element_by_xpath('//div[@class="graph-guess-word"]')
    v_res = validate(v_elem, img_l)
    if v_res:
      print('{} - [Passed: {}]'.format(img_f, img_l))
    else:
      print('{} - [Failed: exp_val={}, act_val={}]'.format(img_f, img_l, v_elem.text))
    
    # Save the predicted result
    fsaved = wd.get_screenshot_as_file(res_out)
    if fsaved:
      print('The predicted result has been saved!')
    else:
      print('Failed to save the predicted result!')
    
    time.sleep(3)
    wd.back()
    time.sleep(3)
    
  print('Done!')
  wd.execute_script('window.alert("Enjoy with Selenium testing!")')

# Entrance
if __name__ == '__main__':
  main()
  