#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import json
import os
import time
import uuid

def validate(v_elem, expectation):
  exp_texts = expectation.split()
  count = 0
  for exp_text in exp_texts:
    if exp_text in v_elem.text:
      count += 1
  return count == len(exp_texts)

if __name__ == '__main__':
  # Read config file
  with open('./config.json', 'r') as f:
    config = json.load(f)
  print(config)

  # Load Chrome drive
  wd = webdriver.Chrome(config['web_drive_path'])
  wd.get('http://www.baidu.com')


  # Send text to search box on baidu page.
  s_text = 'Python3 菜鸟教程'
  wd.find_element_by_id('kw').send_keys(s_text)

  # Click "Search" button after typing the text.
  wd.find_element_by_id('su').click()

  # Sleep 3 secends to wait for loading html elements.
  time.sleep(3)

  # Trigger when the network is poor
  loop = config['attempts']
  while loop > 0:
    elems = wd.find_elements_by_xpath('//div[@class="result c-container "]')
    if len(elems) > 0:
      break
    loop -= 1

  # Validate the specified item (This case is third one)
  v_elem = elems[config['visit_result']]
  res = validate(v_elem, s_text)
  if res:
    print('Passed')
  else:
    print('The {} record is unmatched!'.format(config['visit_result']))

  # Save the screenshot to local.
  fname = str(uuid.uuid1()) + '.png'
  fsaved = wd.get_screenshot_as_file(os.path.join(config['screenshots_dir'], fname))
  if fsaved:
    print('Done!')
  else:
    print('Failed to save the screenshot!')

  wd.execute_script('window.alert("Enjoy with Selenium testing!")')
