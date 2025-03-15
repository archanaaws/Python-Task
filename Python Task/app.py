import os
import shutil
import subprocess
from time import sleep


def main():
    allure_results_dir = os.path.join("reports")
    allure_results_dirreports = os.path.abspath("reports")
    os.makedirs(allure_results_dir, exist_ok=True)

    print("Running Behave tests with Allure...")
    subprocess.run(["behave", "-f", "allure_behave.formatter:AllureFormatter", "-o", allure_results_dir], check=True)

    print("Generating Allure report...")
    print(allure_results_dirreports)
    if shutil.which("allure"):
        subprocess.run(["allure", "serve", allure_results_dirreports], check=True)
    else:
        print("ERROR: Allure is not installed or not in PATH. Please install Allure and try again.")



if __name__ == "__main__":
    main()
