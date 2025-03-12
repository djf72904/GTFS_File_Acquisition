import os
import pandas as pd
from fare_validator import fare_validator
from agency_validator import agency_validator

class gtfs_validator:
    def __init__(self, unzipped_gtfs_path):
        self.unzipped_gtfs_path = unzipped_gtfs_path

    def fix_fares(self):
        fare_fixer = fare_validator(self.unzipped_gtfs_path)

        fare_fixer.fix_current_fares()


    def make_agency_unique(self):
        agency_fixer = agency_validator(self.unzipped_gtfs_path)

        agency_fixer.fix_current_agencies()


