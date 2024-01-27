import os

def create_folders(path):
    # Check if the path already exists
    if not os.path.exists(path):
        # Create the directory and its parents if they don't exist
        os.makedirs(path)
        print(f"Directory created: {path}")
    else:
        print(f"Directory already exists: {path}")

# Example usage:
desired_path = "/path/to/your/new/directory"
create_folders(r"C:\Users\Itay")


