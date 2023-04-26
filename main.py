import os
import shutil

def organize_scripts(directory):
    file_extensions = {
        ".c": "C",
        ".cpp": "C++",
        ".cc": "C++",
        ".cxx": "C++",
        ".h": "C++",
        ".hpp": "C++",
        ".java": "Java",
        ".jar": "Java",
        ".py": "Python",
        ".js": "JavaScript",
        ".php": "PHP",
        ".php3": "PHP",
        ".php4": "PHP",
        ".php5": "PHP",
        ".phtml": "PHP",
        ".rb": "Ruby",
        ".swift": "Swift",
        ".m": "Objective-C",
        ".kt": "Kotlin",
        ".kts": "Kotlin",
        ".scala": "Scala",
        ".go": "Go",
        ".rs": "Rust",
        ".lua": "Lua",
        ".ts": "TypeScript",
        ".dart": "Dart",
        ".cs": "C#",
        ".vb": "Visual Basic",
        ".vbs": "Visual Basic",
        ".sql": "SQL",
        ".html": "HTML",
        ".htm": "HTML",
        ".css": "CSS",
        ".xml": "XML",
        ".json": "JSON",
        ".yml": "YAML",
        ".yaml": "YAML"
    }
    organized_directory = os.path.join(directory, "Organized Scripts")
    os.makedirs(organized_directory)
    for file in os.listdir(directory):
        # get the file extension
        file_extension = os.path.splitext(file)[1]
        
        # check if the file extension is in the file_extensions dictionary
        if file_extension in file_extensions:
            # create the folder if it doesn't exist
            folder_name = file_extensions[file_extension]
            folder_path = os.path.join(organized_directory, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            # move the file to the folder
            file_path = os.path.join(directory, file)
            shutil.move(file_path, folder_path)

directory = input("Enter the directory path: ")
organize_scripts(directory)
