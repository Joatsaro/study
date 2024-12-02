# Created by asaquelares at 11/11/24
Feature: GitHub API validation
  # Enter feature description here

  Scenario: Session management check
    Given I have github auth credentials
    When I hit getRepo API of github
    Then status code of response should be 200
