class fare_validator:
    def __init__(self, unzipped_path):
        self.unzipped_path = unzipped_path

    def fix_current_fares(self):
        print(f"must fix fares for {self.unzipped_path}")