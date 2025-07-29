Feature: Top Players
  As a user
  I want to view the top players for a specific category
  So that I can see who is leading in the game in that category

  Scenario: View top players
    Given I have a valid request to view top players for a specific category
    When I send the request to view top players
    Then I should receive a response with status code 200
    And the response should contain a list of top players usernames for that category
