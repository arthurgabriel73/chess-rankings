Feature: Generate Top Players Rating Histories CSV
  As a user
  I want to generate a CSV file of the rating histories of top players for a specific category
  So that I can download and analyze their performance data

  Scenario: Generate CSV for top players rating histories
    Given I have a request to generate a CSV file for the rating histories of the top "50" players for the "classical" category for the previous "30" days
    When I send the request to generate the CSV file
    Then I should receive a response with status code 201
    And the response should contain a CSV file with the rating histories of the top "50" players for the "classical" category for the previous "30" days

