Feature: Car Valuation Check

  Scenario: Verify car details from valuation website
    Given an input file "car_input - V6.txt" with vehicle registration numbers
    When fetching the car details from the valuation website
    Then comparing the output with expected output file "car_output - V6.txt"
