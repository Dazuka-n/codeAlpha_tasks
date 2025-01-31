import os
import shutil

# Define file categories and extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh", ".html", ".css"],
    "Others": []  # Files with unknown extensions
}

def organize_directory(directory):
    """Organize files in the specified directory."""
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(filepath):
            continue

        # Identify the file extension
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        # Determine the category
        category = "Others"
        for cat, extensions in FILE_CATEGORIES.items():
            if extension in extensions:
                category = cat
                break

        # Create category folder if not exists
        category_folder = os.path.join(directory, category)
        os.makedirs(category_folder, exist_ok=True)

        # Move the file
        shutil.move(filepath, os.path.join(category_folder, filename))
        print(f"Moved '{filename}' to '{category}/'.")

if __name__ == "__main__":
    # Specify the directory to organize
    directory_to_organize = input("Enter the path to the directory to organize: ").strip()
    organize_directory(directory_to_organize)