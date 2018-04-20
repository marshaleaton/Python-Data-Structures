# Created by marshaleaton at 19/04/2018
Feature: Has a node with data and pointer to next node
  # Enter feature description here

  Scenario: Created Node has data and points to nothing
    When I Create Node
    Then The Node Contains data and a pointer with None

  Scenario: Create Head node and add second node, now the head node points to added node
    When I Create head node
    And Add a second node to the first one
    Then The head node contains data and a pointer to the second node
    And Second node contains data and an empty pointer

