import os
import shutil

from gtfs_validator import gtfs_validator
from transit_data_retriever import transit_data_retriever

# Dictionary of transit agencies and their GTFS dataset URLs
datasets = {
    "MTA_Bus": "https://files.mobilitydatabase.org/mdb-516/mdb-516-202408080013/mdb-516-202408080013.zip",
    "MTA_Subway": "https://files.mobilitydatabase.org/mdb-516/mdb-516-202408080013/mdb-516-202408080013.zip",
    "LIRR": "https://files.mobilitydatabase.org/mdb-507/mdb-507-202412050038/mdb-507-202412050038.zip",
    "PATH": "https://files.mobilitydatabase.org/mdb-517/mdb-517-202411280023/mdb-517-202411280023.zip",
    "PATCO": "https://files.mobilitydatabase.org/mdb-505/mdb-505-202411070009/mdb-505-202411070009.zip",
    "Metro_North": "https://files.mobilitydatabase.org/mdb-524/mdb-524-202503100036/mdb-524-202503100036.zip",
    "SEPTA_Rail": "https://files.mobilitydatabase.org/mdb-503/mdb-503-202411280039/mdb-503-202411280039.zip",
    "SEPTA_Bus": "https://files.mobilitydatabase.org/mdb-502/mdb-502-202411280022/mdb-502-202411280022.zip",
    "NJT_Bus": "https://files.mobilitydatabase.org/mdb-508/mdb-508-202411280006/mdb-508-202411280006.zip",
    "NJT_Rail": "https://files.mobilitydatabase.org/mdb-509/mdb-509-202412050056/mdb-509-202412050056.zip",
    "NYC_Ferry": "https://files.mobilitydatabase.org/mdb-515/mdb-515-202503060058/mdb-515-202503060058.zip",
    "NY_Waterway": "https://files.mobilitydatabase.org/mdb-525/mdb-525-202402080014/mdb-525-202402080014.zip"
    #"Coach_USA": "https://files.mobilitydatabase.org/tld-5741/tld-5741-202502200043/tld-5741-202502200043.zip"
}

def main():

    # if os.path.exists("./transit_datasets_unzipped"):
    #     shutil.rmtree("./transit_datasets_unzipped")
    #     print("removed transit_datasets_unzipped")
    # if os.path.exists("./transit_datasets_zipped"):
    #     shutil.rmtree("./transit_datasets_zipped")
    #     print("removed transit_datasets_zipped")
    if os.path.exists("./transit_datasets_final"):
        shutil.rmtree("./transit_datasets_final")

    downloader = transit_data_retriever(datasets)
    # print("------------------------------------------------------------")
    # print("Downloading and unzipping transit data from MobilityDatabase")
    # print("------------------------------------------------------------")
    # downloader.download_data()
    # downloader.unzip_data()

    validators = []
    for name, url in datasets.items():
        validators.append(gtfs_validator(name))

    for validator in validators:
        print("---------------------------------------------------------")
        print(f"Validating GTFS files for {validator.unzipped_gtfs_path}")
        print("---------------------------------------------------------")
        validator.fix_fares()
        validator.make_agency_unique()

    print("------------------------------------------------------------")
    print("Zip final files back up for validation")
    print("------------------------------------------------------------")
    downloader.zip_data()

    print("------------------------------------------------------------")
    print("Validate final zip files with command line validator")
    print("------------------------------------------------------------")

    for validator in validators:
        validator.run_mdb_validator()

    print("GTFS File Acquisition Complete. Check transit_datasets_final for complete zip files")

if __name__ == "__main__":
    main()