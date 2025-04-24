import os
import json

class mdb_validator:
    def __init__(self, unzipped_gtfs_path):
        self.unzipped_gtfs_path = unzipped_gtfs_path

    def validate_final(self):
        print(f"Validating final zip for {self.unzipped_gtfs_path}")

        os.system(f"java -jar GTFS_File_Acquisition/gtfs-validator-6.0.0-cli.jar -i ./transit_datasets_final/{self.unzipped_gtfs_path}.gtfs.zip -o ./validation/{self.unzipped_gtfs_path} -p")
        self.check_report()

    def check_report(self):
        report_file = open(f"./validation/{self.unzipped_gtfs_path}/report.json")
        report_data = json.load(report_file)
        notices = report_data["notices"]

        errorAmt = 0
        for notice in notices:
            if notice["severity"] == "ERROR":
                print(f"Error validating {self.unzipped_gtfs_path}!\n code: {notice['code']}")
                errorAmt += 1

        if errorAmt > 0:
            os.remove(f"transit_datasets_final/{self.unzipped_gtfs_path}.gtfs.zip")
            print(f"{self.unzipped_gtfs_path}.zip removed from transit_datasets_final due to error")
        else:
            print(f"{self.unzipped_gtfs_path}.zip validated")

