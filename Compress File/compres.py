import os
import tarfile

archive_name = "archive.tar.gz"
files_to_add = ["file1.txt", "file2.txt"]


with tarfile.open(archive_name, "w:gz") as tar:
    for f in files_to_add:
        if not os.path.exists(f):
            
            with open(f, "w") as file:
                file.write(f"This is a placeholder for {f}\n")
            print(f"{f} not found. Created with default content.")

        tar.add(f)

print(f"{archive_name} created successfully.")
