import os
import shutil

# Define file categories
FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".tar", ".rar"],
}

def organize_files(directory):
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return
    
    # Iterate over files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get file extension
        file_extension = os.path.splitext(filename)[1].lower()
        
        # Find the right category for the file
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                category_path = os.path.join(directory, category)
                
                # Create category folder if it doesn't exist
                if not os.path.exists(category_path):
                    os.makedirs(category_path)
                
                # Move file to the corresponding folder
                shutil.move(file_path, os.path.join(category_path, filename))
                print(f"Moved: {filename} -> {category}/")
                break
    
    print("File organization complete.")

if __name__ == "__main__":
    target_directory = input("Enter the directory to organize: ")
    organize_files(target_directory)
