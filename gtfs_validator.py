import pandas as pd
import os
from fare_validator import fare_validator
from agency_validator import agency_validator
from mdb_validator import mdb_validator

class gtfs_validator:
    def __init__(self, unzipped_gtfs_path):
        self.unzipped_gtfs_path = unzipped_gtfs_path

    def fix_fares(self):
        fare_fixer = fare_validator(self.unzipped_gtfs_path)

        fare_fixer.fix_current_fares()

    def make_agency_unique(self):
        agency_fixer = agency_validator(self.unzipped_gtfs_path)

        agency_fixer.fix_current_agencies()

    def fix_misc_issues(self):

        # NJT Rail stop distances
        if self.unzipped_gtfs_path == "NJT_Rail":
            path = f"./transit_datasets_unzipped/{self.unzipped_gtfs_path}/stop_times.txt"
            df = pd.read_csv(path, sep=",")
            df.to_csv(f"./{self.unzipped_gtfs_path}_stop_times_temp.csv", index=False)

            for i in range(len(df)):
                if df.loc[i, "stop_id"] == 26326 and df.loc[i, "shape_dist_traveled"] == 1.2583:
                    df.loc[i, "shape_dist_traveled"] = 1.2584

            df.to_csv(f"./{self.unzipped_gtfs_path}_stop_times_temp.csv", index=False)

            os.remove(path)
            os.rename(f"{self.unzipped_gtfs_path}_stop_times_temp.csv", path)

            print("Fixed NJT_Rail stop_times.txt error")

        # Path transfer time for fare
        if self.unzipped_gtfs_path == "PATH_Rail":
            path = f"./transit_datasets_unzipped/{self.unzipped_gtfs_path}/fare_attributes.txt"
            df = pd.read_csv(path, sep=",")
            df.to_csv(f"./{self.unzipped_gtfs_path}_fare_attributes_temp.csv", index=False)
            df = pd.read_csv(f"./{self.unzipped_gtfs_path}_fare_attributes_temp.csv")

            df["transfer_duration"] = df["transfer_duration"].astype(object)
            df.loc[0, "transfer_duration"] = ""

            df.to_csv(f"./{self.unzipped_gtfs_path}_fare_attributes_temp.csv", index=False)
            os.remove(path)
            os.rename(f"./{self.unzipped_gtfs_path}_fare_attributes_temp.csv", path)

            print(f"Updated transfer duration in {self.unzipped_gtfs_path} fare_attributes.txt")

        # NYW color and integer
        if self.unzipped_gtfs_path == "NYW_Ferry":
            print("fix error and color issue")

    def run_mdb_validator(self):
        mdb_fixer = mdb_validator(self.unzipped_gtfs_path)

        mdb_fixer.validate_final()


