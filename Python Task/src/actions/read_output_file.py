import csv
import os

class ReadOutputFile:
    @staticmethod
    def read(output_file):
        """Reads expected output from CSV."""
        output_map = {}
        file_path = os.path.join(os.getcwd(), "data", output_file)

        with open(file_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                reg_number = row["VARIANT_REG"].replace(" ", "")
                output_map[reg_number] = {key.lower(): value for key, value in row.items()}

        return output_map
