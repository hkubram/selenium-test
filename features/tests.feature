Feature: testing application

Scenario: the user can access all the pages
When the user visits the "home" page
Then the user ends up on the "Home" page
When the user visits the "accelerator-dashboard" page
Then the user ends up on the "accelerator-dashboard" page
When the user visits the "job-search" page
Then the user ends up on the "job-search" page
When the user visits the "cart" page
Then the user ends up on the "cart" page

Scenario: testing tabs
When the user visits the "home" page
When the user can click on the "Home" tab
Then the user ends up on the "Home" page
When the user can click on the "Find Jobs" tab
Then the user ends up on the "Find Jobs" page
When the user can click on the "Job Cart" tab
Then the user ends up on the "Job Cart" page

Scenario: home page displays user information
When the user visits the "home" page
Then the user sees the name "Sarah Fawson"
Then the user sees the title "Senior Consultant"
Then the user sees the Employee Id "605355"
Then the user sees the Clearence Level "Secret"

Scenario: the user visits the accelerator dashboard
When the user visits the "home" page
When the user clicks the Find Jobs button
Then the user ends up on the job-search page

Scenario: search for a user that does not exist
When the user visits the "accelerator-dashboard" page
When the user finds the employee "1"
Then employee workday profile does not exist

Scenario: search for employee 112233 and find their name
When the user visits the "accelerator-dashboard" page
When the user finds the employee "112233"
Then the user finds employee name "Christine"