# Created by asaquelares at 08/11/24
Feature: Verify if Books are added and deleted using Library API
  # Enter feature description here

  @library
  Scenario: Verify AddBook API functionality
    Given the Book details which needs to be added to Library
    When we execute the AddBook PostAPI method
    Then book is successfully added
    And status code of response should be 200

  @library
  Scenario Outline: Verify AddBook API functionality
    Given the Book details which <isbn> and <aisle>
    When we execute the AddBook PostAPI method
    Then book is successfully added
      Examples:
        | isbn | aisle |
        | sdass| 8940  |
        | powre| 76332 |

