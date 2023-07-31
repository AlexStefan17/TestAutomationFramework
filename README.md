# TestAutomationFramework
VIDEO URL: https://www.youtube.com/watch?v=HBxAGL-4HyE&ab_channel=Alex
1. Introduction
   This is a Test Automation Framework used to test the https://www.saucedemo.com website, which is a website for test purpose.
   
   This framework uses Python as programming language, Selenium for web scrapping and Pytest for the testing part and raport generation. 

2. Installation
   In order to make this framework works you have to install following packages: pytest, selenium ,pytest-html, webdriver-manager.
   Also, you need to have Google Chrome to run the tests in the browser.
   The Selenium webdriver is automatically installed by ussing this code:
   ```
          driver = webdriver.Chrome(
            service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
            options=chrome_options)
   ```
3. Usage
   You can run individual tests by running them as a normal code file or using pytest flags line.
   When you are running test if you wanna exit headless mode of the browser comment this line of code
   ```
   chrome_options.add_argument('--headless')
   ```
   How to run a single test using pytest flag: pytest test_1
   If you write pytest in command line it will run all the tests.
   To generate XML raport you can use pytest --browser_name chrome --html=reports.html
   Another topic you can use it is to integrate this test framework with Jenkins to automate the build and see the statistics of the tests.
   This is the command line that I use for Jenkins build that generate XML raports.
   ```
   #!/bin/bash
   cd tests
   pytest --browser_name chrome --html=$WORKSPACE/reports/reports.html -v --junitxml="result.xml"
   ```
   This command is for Post-build Actions where you select Publish JUnit test result report from the dropdown menu.
   ```
   tests/*.xml
   ```
