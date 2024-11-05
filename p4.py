import os
import shutil

def organize_files(directory):
    file_types = {
        'Images': ['jpg', 'jpeg', 'png', 'gif'],
        'Documents': ['pdf', 'docx', 'txt', 'pptx'],
        'Videos': ['mp4', 'avi', 'mov'],
        'Music': ['mp3', 'wav'],
        'Archives': ['zip', 'rar', 'tar']
    }
    for category in file_types.keys():
        category_path = os.path.join(directory, category)
        os.makedirs(category_path, exist_ok=True)
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = filename.split('.')[-1].lower()
            moved = False

            for category, extensions in file_types.items():
                if file_extension in extensions:
                    shutil.move(os.path.join(directory, filename), os.path.join(directory, category, filename))
                    print(f'Moved: {filename} -> {category}')
                    moved = True
                    break
            
            if not moved:
                print(f'No category found for: {filename}')

if __name__ == "__main__":
    target_directory = input("Enter the directory path to organize: ")
    organize_files(target_directory)
