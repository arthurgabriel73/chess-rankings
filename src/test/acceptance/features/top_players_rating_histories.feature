Feature: Top Players Rating Histories
  As a user
  I want to view the rating histories of top players for a specific category
  So that I can analyze their performance over time

  Scenario: View top players rating histories
    Given I have a request to view the rating histories of the top "50" players for the "classical" category for the previous "30" days
    When I send the request to view top players rating histories
    Then I should receive a response with status code 200
    And the response should contain a list of top "50" players rating histories for the "classical" category for the previous "30" days

  Scenario: View top players rating histories with invalid category
    Given I have a request to view the rating histories of the top "50" players for the "invalid-category" category for the previous "30" days
    When I send the request to view top players rating histories
    Then I should receive a response with status code 400

  Scenario: View top players rating histories with invalid number of players
    Given I have a request to view the rating histories of the top "invalid-number" players for the "classical" category for the previous "30" days
    When I send the request to view top players rating histories
    Then I should receive a response with status code 422

  Scenario: View top players rating histories with invalid number of days
    Given I have a request to view the rating histories of the top "50" players for the "classical" category for the previous "invalid-days" days
    When I send the request to view top players rating histories
    Then I should receive a response with status code 422

  Scenario: View top players rating histories with too many players
    Given I have a request to view the rating histories of the top "1000" players for the "classical" category for the previous "30" days
    When I send the request to view top players rating histories
    Then I should receive a response with status code 400

  Scenario: View top players rating histories with too many days
    Given I have a request to view the rating histories of the top "50" players for the "classical" category for the previous "365" days
    When I send the request to view top players rating histories
    Then I should receive a response with status code 400
