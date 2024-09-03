Feature: Test nafigation between pages
We can have a longer description 


    Scenario: Homepage can go to Blog
        Given I am on the Homepage
        When I click on the link "blog-link"
        Then I am on the blog 