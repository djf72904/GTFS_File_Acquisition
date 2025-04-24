import os
import shutil

from gtfs_validator import gtfs_validator
from transit_data_retriever import transit_data_retriever

# Dictionary of transit agencies and their GTFS dataset ids
datasets = {
    "NYCT_Rail"     : "f-dr5r-nyctsubway",
    "NYCT_Q_Bus"    : "f-dr5x-mtanyctbusqueens",
    "NYCT_SI_Bus"   : "f-dr5r-mtanyctbusstatenisland",
    "NYCT_BRK_Bus"  : "f-dr5r-mtanyctbusbrooklyn",
    "NYCT_BRX_Bus"  : "f-dr72-mtanyctbusbronx",
    "NYCT_M_Bus"    : "f-dr5r-mtanyctbusmanhattan",
    "MTA_Bus"       : "f-dr5r-mtabc",

    "LIRR_Rail"     : "f-dr5-mtanyclirr",

    "PATH_Rail"     : "f-dr5r-path~nj~us",

    "PATCO_Rail"    : "f-dr4e-patco",

    "MN_HRL_Bus"    : "f-hudson~rail~link",
    "MN_Rail"       : "f-dr7-mtanyc~metro~north",

    "SEPTA_Rail"    : "f-dr4-septa~rail",
    "SEPTA_Bus"     : "f-dr4-septa~bus",

    "NJT_Rail"      : "f-dr5-nj~transit~rail",
    "NJT_Bus"       : "f-dr5-nj~transit~bus",

    "NYW_Ferry"     : "f-dr7-nywaterway",

    "NYCF_Ferry"    : "f-dr5r-nycferry"
}

def main():

    if os.path.exists("./transit_datasets_unzipped"):
        shutil.rmtree("./transit_datasets_unzipped")
        print("removed transit_datasets_unzipped")
    if os.path.exists("./transit_datasets_zipped"):
        shutil.rmtree("./transit_datasets_zipped")
        print("removed transit_datasets_zipped")
    if os.path.exists("./transit_datasets_final"):
        shutil.rmtree("./transit_datasets_final")
        print("removed transit_datasets_final")
    if os.path.exists("./validation"):
        shutil.rmtree("./validation")
        os.makedirs("./validation")
        print("removed validation")

    downloader = transit_data_retriever(datasets)
    print("------------------------------------------------------------")
    print("Downloading and unzipping transit data from MobilityDatabase")
    print("------------------------------------------------------------")
    downloader.download_data()
    downloader.unzip_data()

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
    shutil.rmtree(f"./transit_datasets_unzipped")

    print("------------------------------------------------------------")
    print("Validate final zip files with command line validator")
    print("------------------------------------------------------------")
    for validator in validators:
        validator.run_mdb_validator()

    print("-----------------------------------------------------------------------------------")
    print("GTFS File Acquisition Complete. Check transit_datasets_final for complete zip files")
    print("-----------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()