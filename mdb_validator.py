import os

class mdb_validator:
    def __init__(self, unzipped_gtfs_path):
        self.unzipped_gtfs_path = unzipped_gtfs_path

    def validate_finals(self):
        print(f"Validating final zip for {self.unzipped_gtfs_path}")

        #os.system(f"java -jar gtfs-validator-6.0.0-cli.jar -i ./trans_datasets_final/{self.unzipped_gtfs_path}.zip -o ./validation/{self.unzipped_gtfs_path} -p")

