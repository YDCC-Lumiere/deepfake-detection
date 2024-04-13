"""
WARNING: you must download the authentication file from https://www.kaggle.com/settings
and move it to ~/.kaggle directory
"""
import argparse
import os

from kaggle.api.kaggle_api_extended import KaggleApi

DEEPFAKERAPP_URL = "huynhngotrungtruc/fsd-deepfakerapp"

def download_dataset():
    url = DEEPFAKERAPP_URL
    api = KaggleApi()
    api.authenticate()
    os.makedirs("dataset", exist_ok=True)
    api.dataset_download_files(url, path="dataset", unzip=True, force=True)

if __name__ == "__main__":
    download_dataset()

