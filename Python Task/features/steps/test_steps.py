import allure
from behave import given, when, then
from src.actions.read_input_file import ReadInputFile
from src.actions.read_output_file import ReadOutputFile
from src.actions.fetch_car_details import FetchCarDetails


@given('an input file "{input_file}" with vehicle registration numbers')
def step_extract_registration_numbers(context, input_file):
    context.reg_numbers = ReadInputFile.read(input_file)
    print(context.reg_numbers)


@when('fetching the car details from the valuation website')
def step_fetch_car_details(context):
    context.fetched_data = {}
    for reg in context.reg_numbers:
        details = FetchCarDetails.fetch(reg)
        if details:
            context.fetched_data[reg] = details

    print(context.fetched_data)


@then('comparing the output with expected output file "{output_file}"')
def step_compare_with_expected(context, output_file):
    expected_data = ReadOutputFile.read(output_file)
    mismatches = []

    for reg, details in context.fetched_data.items():
        if reg in expected_data:
            print("Registration Number found in the Output File")
            expected = expected_data[reg]
            if expected["make"] != details["MAKE"] or expected["model"] != details["MODEL"] or expected["year"] != details["YEAR"] :
                mismatches.append(f"Mismatch for {reg}: Expected {expected}, Got {details}")
                allure.attach(f"Mismatch for {reg}", name="Log Details", attachment_type=allure.attachment_type.TEXT)

            else:
                allure.attach(f"Data Matched for {reg}", name="Log Details", attachment_type=allure.attachment_type.TEXT)

        else:
            mismatches.append(f"{reg} not found in expected output.")
            allure.attach(f"{reg} not found in expected output.", name="Log Details", attachment_type=allure.attachment_type.TEXT)
    print(mismatches)

    report_path = "reports/test_report.txt"
    with open(report_path, "w") as report:
        if mismatches:
            report.write("Test Failed:\n" + "\n".join(mismatches))
        else:
            report.write("All tests passed successfully.")

    print(f"Test report generated at {report_path}")
