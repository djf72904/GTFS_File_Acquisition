import pandas as pd
import os

class fare_validator:
    def __init__(self, unzipped_path):
        self.unzipped_path = unzipped_path

    def fix_current_fares(self):
        # Fare data already up to date
        if self.unzipped_path == "PATCO":
            print("Fare data for PATCO is already correct")

        elif self.unzipped_path == "SEPTA_Rail":
            print("Fare data for SEPTA_Rail is already correct")

        elif self.unzipped_path == "NY_Waterway":
            print("Fare data for NY_Waterway is already correct")

        # Fare data exists just wrong numbers
        elif self.unzipped_path == "PATH":
            self.fix_path_fares()

        elif self.unzipped_path == "NYC_Ferry":
            self.fix_nycFerry_fares()

        # Fare data doesn't exist, but it is simple to add
        elif self.unzipped_path == "MTA_Subway":
            self.fix_mtaSubway_fares()

        elif self.unzipped_path == "MTA_Bus":
            self.fix_mtaBus_fares()

        elif self.unzipped_path == "SEPTA_Bus":
            self.fix_septaBus_fares()

        # Fare based off zones
        elif self.unzipped_path == "Metro_North":
            self.fix_metroNorth_fares()

        elif self.unzipped_path == "LIRR":
            self.fix_lirr_fares()

        # Hard to fix
        elif self.unzipped_path == "NJT_Rail":
            self.fix_njtRail_fares()

        elif self.unzipped_path == "NJT_Bus":
            self.fix_njtBus_fares()

    def fix_path_fares(self):
        path = f"./transit_datasets_unzipped/{self.unzipped_path}/fare_attributes.txt"
        df = pd.read_csv(path, sep = ",")
        df.to_csv(f"./{self.unzipped_path}_fare_attributes_temp.csv", index = False)
        df = pd.read_csv(f"./{self.unzipped_path}_fare_attributes_temp.csv")

        df.loc[0, "price"] = 3.00

        df.to_csv(f"./{self.unzipped_path}_fare_attributes_temp.csv", index = False)
        os.remove(path)
        os.rename(f"./{self.unzipped_path}_fare_attributes_temp.csv", path)

        print("Updated PATH fare_attributes.txt")

    def fix_nycFerry_fares(self):
        path = f"./transit_datasets_unzipped/{self.unzipped_path}/fare_attributes.txt"
        df = pd.read_csv(path, sep=",")
        df.to_csv(f"./{self.unzipped_path}_fare_attributes_temp.csv", index=False)
        df = pd.read_csv(f"./{self.unzipped_path}_fare_attributes_temp.csv")

        df.loc[0, "price"] = 4.50

        df.to_csv(f"./{self.unzipped_path}_fare_attributes_temp.csv", index=False)
        os.remove(path)
        os.rename(f"./{self.unzipped_path}_fare_attributes_temp.csv", path)

        print("Updated NYC_Ferry fare_attributes.txt")

    def fix_mtaSubway_fares(self):
        path = f"./transit_datasets_unzipped/{self.unzipped_path}/fare_attributes.txt"
        if not os.path.exists(path):
            mta_fares = {
                "fare_id": [1],
                "price": [2.90],
                "currency_type": ["USD"],
                "payment_method": [1],
                "agency_id": [self.unzipped_path],
                "transfers": [None]
            }
            df = pd.DataFrame(mta_fares)
            df.to_csv(path, index = False)
            print("Updated MTA_Subway fare_attributes.txt")
        else:
            print("Error updating fare_attributes.txt in MTA_Subway. File already exists")

    def fix_mtaBus_fares(self):
        print("MTA_Bus express vs local for fares")

    def fix_septaBus_fares(self):
        print("SEPTA_Bus based off zones for fares")

    def fix_metroNorth_fares(self):
        print("Metro_North based off zones for fares")

    def fix_lirr_fares(self):
        print("LIRR based off zones for fares")

    def fix_njtRail_fares(self):
        print("Must implement web scraping for NJT_Rail")

    def fix_njtBus_fares(self):
        print("FUCK NJT BUS")