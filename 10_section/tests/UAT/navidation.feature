Feature: Test nafigation between pages
We can have a longer description 


    Scenario: Homepage can go to Blog
        Given I am on the homepage
        When I click on the link with id "blog-link"
        Then I am on the blog page

    Scenario: Blog page can go to homepage
        Given I am on the blog page
        When I click on the link with id "home-link"
        Then I am on the homepage