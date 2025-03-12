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
        elif self.unzipped_path == "LIRR":
            self.fix_lirr_fares()

        # Hard to fix
        elif self.unzipped_path == "NJT_Rail":
            self.fix_njtRail_fares()

        elif self.unzipped_path == "Metro_North":
            self.fix_metroNorth_fares()

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

        print(f"Updated {self.unzipped_path} fare_attributes.txt")

    def fix_nycFerry_fares(self):
        path = f"./transit_datasets_unzipped/{self.unzipped_path}/fare_attributes.txt"
        df = pd.read_csv(path, sep=",")
        df.to_csv(f"./{self.unzipped_path}_fare_attributes_temp.csv", index=False)
        df = pd.read_csv(f"./{self.unzipped_path}_fare_attributes_temp.csv")

        df.loc[0, "price"] = 4.50

        df.to_csv(f"./{self.unzipped_path}_fare_attributes_temp.csv", index=False)
        os.remove(path)
        os.rename(f"./{self.unzipped_path}_fare_attributes_temp.csv", path)

        print(f"Updated {self.unzipped_path} fare_attributes.txt")

    def fix_mtaSubway_fares(self):
        path = f"./transit_datasets_unzipped/{self.unzipped_path}/fare_attributes.txt"
        if not os.path.exists(path):
            subway_fares = {
                "fare_id": ["single_fare"],
                "price": [2.90],
                "currency_type": ["USD"],
                "payment_method": [1],
                "agency_id": [self.unzipped_path],
                "transfers": [None]
            }
            df = pd.DataFrame(subway_fares)
            df.to_csv(path, index = False)
            print(f"Created {self.unzipped_path} fare_attributes.txt")
        else:
            print(f"Error updating fare_attributes.txt in {self.unzipped_path}. File already exists")

    def fix_mtaBus_fares(self):
        path = f"./transit_datasets_unzipped/{self.unzipped_path}/fare_attributes.txt"
        if not os.path.exists(path):
            bus_fares = {
                "fare_id": ["local_fare", "express_fare"],
                "price": [2.90, 7.00],
                "currency_type": ["USD", "USD"],
                "payment_method": [0, 0],
                "agency_id": [self.unzipped_path, self.unzipped_path],
                "transfers": [None, None],
                "transfer_duration": [7200, 7200]
            }
            df = pd.DataFrame(bus_fares)
            df.to_csv(path, index = False)
            print(f"Created {self.unzipped_path} fare_attributes.txt")
        else:
            print(f"Error updating fare_attributes.txt in {self.unzipped_path}. File already exists")

        path = f"./transit_datasets_unzipped/{self.unzipped_path}/routes.txt"

        df = pd.read_csv(path, sep=",")
        route_names = df["route_long_name"].values
        route_ids = df["route_id"].values
        fare_ids = []

        for i in range(len(df)):
            if "express" in route_names[i].lower():
                fare_ids.append("express_fare")
            else:
                fare_ids.append("local_fare")

        path = f"./transit_datasets_unzipped/{self.unzipped_path}/fare_rules.txt"
        if not os.path.exists(path):
            df = pd.DataFrame({"route_id": route_ids, "fare_id": fare_ids})
            df.to_csv(path, index=False)
            print(f"Created {self.unzipped_path} fare_rules.txt")
        else:
            print(f"Error updating fare_rules.txt in {self.unzipped_path}. File already exists")

    def fix_septaBus_fares(self):
        path = f"./transit_datasets_unzipped/{self.unzipped_path}/fare_attributes.txt"
        if not os.path.exists(path):
            bus_fares = {
                "fare_id": ["single_fare"],
                "price": [2.50],
                "currency_type": ["USD"],
                "payment_method": [0],
                "agency_id": [self.unzipped_path],
                "transfers": [2],
                "transfer_duration": [7200]
            }
            df = pd.DataFrame(bus_fares)
            df.to_csv(path, index=False)
            print(f"Created {self.unzipped_path} fare_attributes.txt")
        else:
            print(f"Error updating fare_attributes.txt in {self.unzipped_path}. File already exists")

    def fix_lirr_fares(self):
        print("LIRR based off zones for fares")

    def fix_njtRail_fares(self):
        print("Must implement web scraping for NJT_Rail")

    def fix_metroNorth_fares(self):
        print("Metro_North based off zones for fares. complicated")

    def fix_njtBus_fares(self):
        print("FUCK NJT BUS")