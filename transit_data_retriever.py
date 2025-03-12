import os
import requests
import zipfile

class transit_data_retriever:
    def __init__(self, datasets):
        self.datasets = datasets
        self.zipped_dir = "./transit_datasets_zipped"
        self.unzipped_dir = "./transit_datasets_unzipped"
        os.makedirs(self.zipped_dir, exist_ok=True)
        os.makedirs(self.unzipped_dir, exist_ok=True)

    def download_data(self):
        for name, url in self.datasets.items():
            print(f"Downloading {name}...")
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                file_path = os.path.join(self.zipped_dir, f"{name}.zip")
                with open(file_path, "wb") as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        file.write(chunk)
                print(f"Saved {name} to {file_path}")
            else:
                print(f"Failed to download {name}. HTTP Status: {response.status_code}")

    def unzip_data(self):
        for name, url in self.datasets.items():
            with zipfile.ZipFile(f"{self.zipped_dir}/{name}.zip", "r") as zip_ref:
                print(f"Unzipping {name}.zip")
                zip_ref.extractall(f"{self.unzipped_dir}/{name}")
                print(f"Saved {name}.zip to transit_datasets_unzipped")