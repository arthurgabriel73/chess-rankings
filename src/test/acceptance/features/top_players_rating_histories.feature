Feature: Top Players Rating Histories
  As a user
  I want to view the rating histories of top players for a specific category
  So that I can analyze their performance over time

  Scenario: View top players rating histories
    Given I have a request to view the rating histories of the top "50" players for the "classical" category for the previous "30" days
    When I send the request to view top players rating histories
    Then I should receive a response with status code 200
    And the response should contain a list of top "50" players rating histories for the "classical" category for the previous "30" days
