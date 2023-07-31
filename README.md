# TestAutomationFramework
# VIDEO URL: https://www.youtube.com/watch?v=HBxAGL-4HyE&ab_channel=Ale
## Introduction
   1.This is a Test Automation Framework used to test the https://www.saucedemo.com website, which is a website for test purpose.
   
   2.This framework uses Python as programming language, Selenium for web scrapping and Pytest for the testing part and raport generation. 
   
   3. Selenium is a popular and powerful open-source automation testing framework widely used for web application testing. It enables testers and developers to automate interactions with web browsers,       simulating user actions like clicking buttons, filling out forms, and navigating through pages. Originally developed by Jason Huggins in 2004, Selenium has since grown into a comprehensive suite of           tools that support various programming languages and browser platforms.

   Key features of Selenium include:

    Cross-browser compatibility: Selenium supports multiple browsers like Chrome, Firefox, Safari, Edge, and more, allowing testers to ensure their web applications work seamlessly across different browsers.

    Multi-language support: Selenium supports various programming languages such as Java, Python, C#, Ruby, and JavaScript, providing flexibility for testers and developers to use their preferred language.

    Test automation: Selenium allows the creation of automated test scripts that can be executed repeatedly, reducing manual testing efforts and improving the efficiency of testing processes.

    Integration: Selenium integrates well with popular testing frameworks like TestNG and JUnit, as well as with Continuous Integration (CI) tools like Jenkins, making it suitable for seamless test automation in the development lifecycle.

    Extensibility: Selenium's modular design allows users to create custom extensions and integrate with third-party tools, enhancing its capabilities and adapting to specific testing needs.

    Web element interaction: Selenium provides various methods to interact with web elements such as clicking buttons, entering text, selecting options, and verifying page content, enabling comprehensive testing scenarios.

    Remote testing: Selenium allows testers to run tests on remote machines or cloud-based platforms, making it efficient for running tests on multiple environments simultaneously.

Whether you are a QA engineer, software developer, or anyone involved in web application testing, Selenium is a valuable tool for achieving robust and reliable test automation, contributing to improved software quality and faster delivery.

   4. Pytest is a popular and easy-to-use testing framework for Python that simplifies the process of writing and executing test cases. It was created by Holger Krekel and is widely adopted in the Python community for unit testing, functional testing, and integration testing.

Key features of pytest include:

    Simple and expressive syntax: Pytest offers a straightforward syntax that allows developers to write clear and concise test cases using Python's assert statement. This simplicity reduces boilerplate code and makes the tests more readable.

    Powerful fixture mechanism: Pytest's fixture system helps set up and tear down test dependencies, such as initializing databases, establishing connections, or creating test data. This promotes code reusability and ensures a clean testing environment.

    Test discovery: Pytest automatically discovers and runs all test functions within specified directories, making it easy to organize and maintain test suites. It can also discover test cases in classes or modules, providing flexibility in test organization.

    Detailed reporting: When a test fails, pytest provides informative output that highlights the exact location of the failure, making it easier for developers to identify and fix issues quickly.

    Parameterized testing: Pytest allows parameterizing test functions, enabling multiple test cases to be executed with different inputs or configurations, which streamlines testing for various scenarios.

    Third-party plugins: Pytest boasts a rich ecosystem of plugins that extend its functionality, enabling features like code coverage analysis, test parallelization, and integration with other testing          frameworks.

    Compatibility and integration: Pytest can be easily integrated with other testing tools and frameworks, and it is compatible with popular testing tools such as Selenium and Django.
   
   Whether you are testing small Python modules or complex applications, pytest provides a user-friendly and powerful testing environment that encourages best testing practices and improves the overall          quality of Python projects. Its versatility, ease of use, and active community support have made it a favorite choice among Python developers for writing effective and maintainable tests.

## Installation
   In order to make this framework works you have to install following packages: pytest, selenium ,pytest-html, webdriver-manager.
   Also, you need to have Google Chrome to run the tests in the browser.
   The Selenium webdriver is automatically installed by ussing this code:
   ```
          driver = webdriver.Chrome(
            service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
            options=chrome_options)
   ```
         In Selenium, WebDriver is a crucial component that acts as a bridge between the Selenium test scripts and the web browsers. It provides a programming interface to control and automate the interactions with the web browsers, allowing testers and developers to simulate user actions and navigate through web pages.
      
      WebDriver supports various programming languages like Java, Python, C#, Ruby, and JavaScript, which means you can write your test scripts in your preferred language while interacting with the same underlying WebDriver API.
      
      The main functions of WebDriver include:
      
          Launching and Closing Browsers: WebDriver allows you to open and close web browsers programmatically. It supports popular browsers such as Chrome, Firefox, Safari, Edge, etc.
      
          Navigating Web Pages: With WebDriver, you can navigate to different URLs, click on links, and handle forward and backward browser navigation.
      
          Interacting with Web Elements: WebDriver provides methods to interact with web elements like clicking buttons, filling out forms, selecting options from dropdowns, and entering text into input fields.
      
          Handling Alerts and Pop-ups: WebDriver enables you to interact with browser alerts and handle pop-up windows that may appear during testing.
      
          Waiting for Elements: WebDriver allows you to wait for specific elements to appear or become interactive before performing actions. This helps synchronize the test script with the actual page loading process.
      
          Taking Screenshots: You can capture screenshots using WebDriver to document the state of the web page during test execution, helping with debugging and reporting.
      
      Overall, WebDriver is the heart of Selenium automation, offering a standardized API to interact with web browsers and enabling developers and testers to create powerful and maintainable test scripts for web application testing.

### Usage
   1.You can run individual tests by running them as a normal code file or using pytest flags line.
   
   2.When you are running test if you wanna exit headless mode of the browser comment this line of code
   ```
   chrome_options.add_argument('--headless')
   ```
   3.How to run a single test using pytest flag: pytest test_1
   
   4.If you write pytest in command line it will run all the tests.
   
   5.To generate XML raport you can use pytest --browser_name chrome --html=reports.html
   
   6.Another topic you can use it is to integrate this test framework with Jenkins to automate the build and see the statistics of the tests.
   
   7.This is the command line that I use for Jenkins build that generate XML raports.
   ```
   #!/bin/bash
   cd tests
   pytest --browser_name chrome --html=$WORKSPACE/reports/reports.html -v --junitxml="result.xml"
   ```
   This command is for Post-build Actions where you select Publish JUnit test result report from the dropdown menu.
   ```
   tests/*.xml
   ```
