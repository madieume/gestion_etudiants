import csv
import json
import pandas as pd

class ExportService:
    @staticmethod
    def export_csv(data, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    @staticmethod
    def export_json(data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def export_excel(data, filename):
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)

    @staticmethod
    def export_pdf(data, filename):
        # Implementation for exporting as PDF can be added here
        pass