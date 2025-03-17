import os

class mdb_validator:
    def __init__(self, unzipped_gtfs_path):
        self.unzipped_gtfs_path = unzipped_gtfs_path

    def validate_finals(self):
        print(f"Validating final zip for {self.unzipped_gtfs_path}")

        os.system("echo hi")

