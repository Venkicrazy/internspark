import os
import shutil
import logging

# Log file creation
logging.basicConfig(
    filename="operations.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

print("========== SMART FILE ORGANIZER ==========")

folder_path = input("Enter Folder Path: ")

try:

    if not os.path.exists(folder_path):
        raise Exception("Folder does not exist")

    files = os.listdir(folder_path)

    for file in files:

        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):

            extension = file.split(".")[-1].upper()

            destination_folder = os.path.join(
                folder_path,
                extension
            )

            if not os.path.exists(destination_folder):
                os.mkdir(destination_folder)

            shutil.move(
                file_path,
                os.path.join(destination_folder, file)
            )

            logging.info(
                f"{file} moved to {destination_folder}"
            )

    print("\nFiles Organized Successfully!")

except Exception as e:

    print("\nError:", e)

    logging.error(str(e))