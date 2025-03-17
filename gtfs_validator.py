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

    def run_mdb_validator(self):
        mdb_fixer = mdb_validator(self.unzipped_gtfs_path)

        mdb_fixer.validate_final()


