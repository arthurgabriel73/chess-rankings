Feature: Top Players
  As a user
  I want to view the top players for a specific category
  So that I can see who is leading in the game in that category

  Scenario: View top players
    Given I have a request to view the top "50" players for the "classical" category
    When I send the request to view top players
    Then I should receive a response with status code 200
    And the response should contain a list of top players usernames for that category

  Scenario: View top players with invalid category
    Given I have a request to view the top "50" players for the "invalid" category
    When I send the request to view top players
    Then I should receive a response with status code 400

  Scenario: View top players with invalid players amount
    Given I have a request to view the top "500" players for the "classical" category
    When I send the request to view top players
    Then I should receive a response with status code 400