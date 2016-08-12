# ios-automation-example

<p>This is a simple POC to show that Appium and Python can be used to quickly set up and execute automated tests
against an iOS application.</p>

# Prerequisites

To run these tests you need to have the following:

* Python 3.4 installed
* Virtualenv
* XCode
* Appium, specifically the OS X App version for this example

# Running Tests
To run these tests:

1. create a config.yaml file structured like the following:
        
        valid_user_creds:
          email: tester@somedomain.com
          password: tester_password

        app_path: /path/to/ios-calendar-app.app

2. Run the runtests.sh script

If all goes well, the script should do all of the required setup and begin executing the tests against the iOS simulator.



