import os
import hashlib

def get_file_checksum(file_path):
    """Calculate the MD5 checksum of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def remove_duplicates(folder_path):
    """Remove duplicate files from the specified folder."""
    file_hashes = {}
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = get_file_checksum(file_path)
            if file_hash in file_hashes:
                print(f"Removing duplicate file: {file_path}")
                os.remove(file_path)
            else:
                file_hashes[file_hash] = file_path

if __name__ == "__main__":
    folder_path = #Actual folder location 
    remove_duplicates(folder_path)
