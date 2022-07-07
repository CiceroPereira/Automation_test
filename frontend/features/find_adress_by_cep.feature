Feature: Find adress by cep

@find_adress
Scenario: Verify searching a valid cep
    Given I open the application
    And I am on find address Home Page
    When I type the following cep number: "71608900"
    And I click on search button
    Then I verify that the following success message is displayed: "sucesso - cep completo"
    And I verify that all field are filled
