# How to use the sample codes

## Prerequisite
* Install Python 3.x
* Download the chrome/ie drive which can work with your current browser.

## Deploy ENV

* Please use the following command to install the necessary modules:
  
  ```cmd
  $ pip install -r requirements.txt
  ```

## Configuration

* Config the following parameter by yourself
  
  ```json
  {
    "attempts": 3, 
    "visit_result": 3,
  }
  ```

## Usage

* Entrance 1:  
  main.py: Test for searching a text on the website *https://www.baidu.com/*

  ```cmd
  $ python main.py
  ```

* Entrance 2:  
  img_main.py: Test for predicting an image on the website *https://image.baidu.com/*

  ```
  $ python img_main.py
  ```