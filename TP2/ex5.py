import os
import csv

def read_csv(file_path):
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(", ".join(row))
    except FileNotFoundError:
        print("File not found!")

def delete_all_files(folder_path):
    try:
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")
    except Exception as e:
        print("Error:", e)

def search_keyword(file_path, keyword):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            for i, line in enumerate(lines, 1):
                if keyword in line:
                    print(f"Line {i}: {line.strip()}")
    except FileNotFoundError:
        print("File not found!")

def create_log(message):
    with open("log.txt", "a") as log_file:
        log_file.write(message + "\n")
