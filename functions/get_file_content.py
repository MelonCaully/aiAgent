import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.join(abs_working_dir, file_path)

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target_file, "r") as f:
            file_content = f.read(MAX_CHARS)
            if len(file_content) == 10000:
                file_content += f' ["{file_path}" truncated at 10000 characters]'
        return file_content
    except Exception as e:
        return f"Error reading file: {e}"