# Databricks notebook source
import zipfile
import os

dbutils.widgets.text("source_directory", "/mnt/customer-data/vendor/ad_hoc_data/data/datavant-tokenization/", "Source of data")
dbutils.widgets.text("destination_directory", "/mnt/customer-data/vendor/ad_hoc_data/data/datavant", "Destination of unzipped data")
dbutils.widgets.text("vendor_db", "nextgen.vendor", "Vendor database")
dbutils.widgets.text("extract_date", "20240801", "Extract date")

source_dir = dbutils.widgets.get("source_directory")
destination_dir = dbutils.widgets.get("destination_directory")
vendor_db = dbutils.widgets.get("vendor_db")
extract_date = dbutils.widgets.get("extract_date")

def unzip_files_in_directory(directory, extract_to_base_path):
    for filename in os.listdir(directory):
        if filename.endswith(".zip"):
            file_path = os.path.join(directory, filename)
            extract_to_path = os.path.join(extract_to_base_path, os.path.splitext(filename)[0])
            
            os.makedirs(extract_to_path, exist_ok=True)
            
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to_path)

source = f"/dbfs{source_dir}"
destination = f"/dbfs{destination_dir}/{extract_date}"

for filename in os.listdir(source):
    if filename.endswith(".zip"):
        if filename.contains(extract_date):
            print(filename)
            file_path = os.path.join(source, filename)
            extract_to_path = os.path.join(destination, os.path.splitext(filename)[0])
            
            os.makedirs(extract_to_path, exist_ok=True)
            
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to_path)
