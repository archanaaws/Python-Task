import re
import os

class ReadInputFile:
    REG_PATTERN = re.compile(r"[A-Z]{2}[0-9]{2}\s?[A-Z]{3}")

    @staticmethod
    def read(input_file):
        reg_numbers = []
        file_path = os.path.join(os.getcwd(), "data", input_file)
        print(file_path)

        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                matches = ReadInputFile.REG_PATTERN.findall(line)
                reg_numbers.extend([match.replace(" ", "") for match in matches])
        print(reg_numbers)
        return reg_numbers
