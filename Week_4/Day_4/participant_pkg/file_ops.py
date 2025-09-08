
import csv
from pathlib import Path


header = ["name", "age", "phone", "track"]


def save_participants(path, participant_dict):
    file = Path(path)
    file_exist = file.exists()

    with open(file, "a", newline ="", encoding = "utf-8") as f:
        writer = csv.DictWriter(f, fieldnames = header)

        if not file_exist or file.stat().st_size == 0:
            writer.writeheader() 
        writer.writerow(participant_dict)


def load_participants(path):
    file = Path(path)
    file_exist = file.exists()

    if not file_exist:
        print("The file does not exist")
        #return []
    else:
        print(f"loading participant from {file.name}")
        with open(file, "r", newline ="", encoding = "utf-8") as f:
            print(f.read())
            #reader = csv.DictReader(f)
            #return list(reader)



