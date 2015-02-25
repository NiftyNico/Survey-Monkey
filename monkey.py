import sys
import random
import math
from selenium import webdriver

if len(sys.argv) < 2:
  print('Please provide a url to open')
  quit(1)

numTimesToFill = 10
if len(sys.argv) >= 3:
  numTimesToFill = int(sys.argv[2])

url = sys.argv[1]; 

def getBrowser():
  browser = webdriver.Firefox()
  browser.get(url)
  #browser.maximize_window()

  return browser

def selectRandomOption (options):
  numOptions = len(options)
  toSelect = int(math.floor(random.random() * numOptions))
  options[toSelect].click()

def getRadioOptions (block):
  return block.find_elements_by_xpath(".//input[@type='radio']")

def selectOneRadioOptionPerQuestion (questions):
  for question in questions:
    radioOptions = getRadioOptions(question)
    selectRandomOption(radioOptions)

def clickSubmitButton (browser):
  browser.find_element_by_xpath("//*[@type='submit']").click()

def fillGoogleForm (url):
  browser = getBrowser()

  radioQuestions = browser.find_elements_by_xpath("//*[@role='radiogroup']")
  selectOneRadioOptionPerQuestion(radioQuestions)

  clickSubmitButton(browser)

  browser.quit()

def fillSurveyMonkey (url):
  browser = getBrowser()

  questions = browser.find_elements_by_css_selector(".question")
  selectOneRadioOptionPerQuestion(questions)

  clickSubmitButton(browser)

  browser.quit()

def fillStrawPoll (url):
  browser = getBrowser()
  
  options = browser.find_elements_by_css_selector(".optionNumber")
  selectRandomOption(options)

  clickSubmitButton(browser)

  browser.quit()

def fillSurvey (url):
  if 'strawpoll' in url:
    fillStrawPoll(url)
  if 'google' in url:
    fillGoogleForm(url)
  else:
    fillSurveyMonkey(url)

surveyNum = 0
while surveyNum < numTimesToFill:
  fillSurvey(url)
  surveyNum += 1
  print('Filled survey num %d' % surveyNum)
