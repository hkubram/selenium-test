Install Firefox browser

Install Firefox Webdriver for your OS and replace the one in the selenium-test folder
    https://github.com/mozilla/geckodriver/releases

Setting up configurations:
    1, Open terminal
    2, Set Path (mines was below, the command is different on a Windows OS)
            export PATH=$PATH:/Users/michaelmarbukh/Desktop/DAU/ResourceAnalyticsWeb/selenium-test
    3, Download packages (there might be other dependencies)
        pip install behave
        pip install selenium

Run Vue project
    1, Run command
            "python3 main.py" in the resource-analytics-dev-server
            "npm run start -dev" in the Admin-Dashboard-Vue directory

Run Automation tests:
    1, Run the command below in the selenium-test folder
           bahave

-----------------------------------------------------------
Notes

Why are automation tests useful?
    Catch bugs that a developer/testers might have missed
    Relieves some of the burden of manual testing
    Typically you would like to test a user flow

Basic terminology
    Selenium - automated testing suite for web applications across different browsers
    Driver - executes the test engineer requests; it sends its own request to the browser

Important files
    geckodriver - Firefox Driver
    enviroment.py - defines what happens before and after every feature
    tests.py - defines what the test does, should be easy to read for non developers
        You can use parameters for dynamic data
    steps.py - contains the code
        (Show how to use parameters)

What is a wait?
    Wait is a way to stop the automation tests from running
        Used to make sure an element is visible before preceding
            Useful in order to make sure tests are not dependent on the computer, browser, or internet connection
                 wait = WebDriverWait(context.browser, 10)
                 element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > div > div > ul > a:nth-child(1) > li")))
        You can also wait for a number of seconds.
            Useful for debugging
                context.browser.implicitly_wait(20)

How does the driver identify Elements
    id (easiest)
    class
    css selector (standard)
    xpath

Identifying element by css selector
    1, Go to a browser
    2, Right click on element, inspect
    3, Right click on the element, click on "Copy Selector"

Check if selector is correct
    1, Go to a browser
    2, Go to the console
    3, type in document.querySelector("Selector")
        If the output is the correct element, then the selector is correct
        If the output is null, then the selector is not correct

Disadvantage of using Selectors
    If the element is moved to another location on the page then the selector will need to be changed
    It is good to keep the selector less specific, but most of the time, its not enough
    Good idea to use UNIQUE ids for elements instead but some ui frameworks make it difficult

Running into difficulties with Selectors
    Sometimes an element could be inside a component that is inside of another component
    In those scenarios, it is difficult for those selectors to pick up the element
    A solution to this problem is using ng-deep, however ng-deep will depreciate soon

What is left
    Better logging system (show an example by letting a test fail)
    Have the tests run on multiple browsers (Firefox, Chrome, IE)
    Improve Selectors (make them less specific, or add id to elements)
    Improve testing on what page your on by checking the URL, not what is on the page (havn't figured out how to do it yet)

https://www.seleniumhq.org/