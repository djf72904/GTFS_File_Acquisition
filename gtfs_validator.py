import os
import pandas as pd
from fare_validator import fare_validator

class gtfs_validator:
    def __init__(self, unzipped_gtfs_path):
        self.unzipped_gtfs_path = unzipped_gtfs_path

    def fix_fares(self):
        fare_fixer = fare_validator(self.unzipped_gtfs_path)

        fare_fixer.fix_current_fares


    def make_agency_unique(self):
        # Files that have agency_id ->
        # agency.txt
        # fare_attributes.txt
        # routes.txt
        # attributions.txt

        # Agency.txt
        agency_path = f"./transit_datasets_unzipped/{self.unzipped_gtfs_path}/agency.txt"
        df = pd.read_csv(agency_path, sep=",")
        df.to_csv(f"./{self.unzipped_gtfs_path}_agency_temp.csv", index=False)
        df = pd.read_csv(f"./{self.unzipped_gtfs_path}_agency_temp.csv")

        if (self.unzipped_gtfs_path == "NJT_Rail"):
            df.drop(0, inplace=True)
            df["agency_id"] = df["agency_id"].astype(object)
            df.loc[1, "agency_id"] = f"{self.unzipped_gtfs_path}"
        else:
            df["agency_id"] = df["agency_id"].astype(object)
            df.loc[0, "agency_id"] = f"{self.unzipped_gtfs_path}"

        df.to_csv(f"./{self.unzipped_gtfs_path}_agency_temp.csv", index=False)

        os.remove(f"./transit_datasets_unzipped/{self.unzipped_gtfs_path}/agency.txt")
        os.rename(f"{self.unzipped_gtfs_path}_agency_temp.csv", f"./transit_datasets_unzipped/{self.unzipped_gtfs_path}/agency.txt")

        print(f"Updated agency_id in agency.txt of {self.unzipped_gtfs_path}")

        # Routes.txt
        routes_path = f"./transit_datasets_unzipped/{self.unzipped_gtfs_path}/routes.txt"
        df = pd.read_csv(routes_path, sep=",")
        df.to_csv(f"./{self.unzipped_gtfs_path}_routes_temp.csv", index=False)

        if ("agency_id" in df.columns):
            df["agency_id"] = df["agency_id"].astype(object)
            for i in range(len(df)):
                df.loc[i, "agency_id"] = f"{self.unzipped_gtfs_path}"

        else:
            agency_list = []
            for i in range(len(df)):
                agency_list.append(f"{self.unzipped_gtfs_path}")
            df["agency_id"] = agency_list

        df.to_csv(f"./{self.unzipped_gtfs_path}_routes_temp.csv", index=False)

        os.remove(f"./transit_datasets_unzipped/{self.unzipped_gtfs_path}/routes.txt")
        os.rename(f"{self.unzipped_gtfs_path}_routes_temp.csv", f"./transit_datasets_unzipped/{self.unzipped_gtfs_path}/routes.txt")

        print(f"Updated agency_id in routes.txt of {self.unzipped_gtfs_path}")

        # Fare_attributes.txt
        if (os.path.exists(f"./transit_datasets_unzipped/{self.unzipped_gtfs_path}/fare_attributes.txt")):
            fare_path = f"./transit_datasets_unzipped/{self.unzipped_gtfs_path}/fare_attributes.txt"
            df = pd.read_csv(fare_path, sep=",")
            df.to_csv(f"./{self.unzipped_gtfs_path}_fare_temp.csv", index=False)

            if ("agency_id" in df.columns):
                df["agency_id"] = df["agency_id"].astype(object)
                for i in range(len(df)):
                    df.loc[i, "agency_id"] = f"{self.unzipped_gtfs_path}"

            else:
                agency_list = []
                for i in range(len(df)):
                    agency_list.append(f"{self.unzipped_gtfs_path}")
                df["agency_id"] = agency_list

            df.to_csv(f"./{self.unzipped_gtfs_path}_fare_temp.csv", index=False)

            os.remove(f"./transit_datasets_unzipped/{self.unzipped_gtfs_path}/fare_attributes.txt")
            os.rename(f"{self.unzipped_gtfs_path}_fare_temp.csv", f"./transit_datasets_unzipped/{self.unzipped_gtfs_path}/fare_attributes.txt")

            print(f"Updated agency_id in fare_attributes.txt of {self.unzipped_gtfs_path}")

        # Attributions
        if (os.path.exists(f"./transit_datasets_unzipped/{self.unzipped_gtfs_path}/attributions.txt")):
            attributions_path = "./transit_datasets_unzipped/{self.unzipped_gtfs_path}/attributions.txt"
            df = pd.read_csv(attributions_path, sep=",")
            df.to_csv(f"./{self.unzipped_gtfs_path}_attributions_temp.csv", index=False)

            if ("agency_id" in df.columns):
                df["agency_id"] = df["agency_id"].astype(object)
                for i in range(len(df)):
                    df.loc[i, "agency_id"] = f"{self.unzipped_gtfs_path}"

            else:
                agency_list = []
                for i in range(len(df)):
                    agency_list.append(f"{self.unzipped_gtfs_path}")
                df["agency_id"] = agency_list

            df.to_csv(f"./{self.unzipped_gtfs_path}_attributions_temp.csv", index=False)

            os.remove(f"./transit_datasets_unzipped/{self.unzipped_gtfs_path}/attributions.txt")
            os.rename(f"{self.unzipped_gtfs_path}_attributions_temp.csv", f"./transit_datasets_unzipped/{self.unzipped_gtfs_path}/attributions.txt")

            print(f"Updated agency_id in attributions.txt of {self.unzipped_gtfs_path}")

        print(f"Made unique agency ids for {self.unzipped_gtfs_path}")
