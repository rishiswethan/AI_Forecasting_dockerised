import os

def create_folder(new_path):
    if not os.path.exists(new_path):
        os.makedirs(new_path)

create_folder("docker_app/save_files")
create_folder("docker_app/data")
create_folder(os.path.join("docker_app/data", "input_folder"))