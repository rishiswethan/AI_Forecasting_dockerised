import os
import json
import source.config as config

def create_folder(new_path):
    if not os.path.exists(new_path):
        os.makedirs(new_path)

print("Creating folders")
create_folder(config.INPUTS_PATH)
create_folder(config.DATA_FOLDER)
create_folder(config.TRAIN_DATA_FOLDER)
create_folder(config.TEST_DATA_FOLDER)
create_folder(config.OUTPUT_FOLDER_PATH)
create_folder(config.TESTING_OUTPUTS_PATH)
create_folder(config.DATA_SCHEMA_PATH)
create_folder(config.MODEL_FOLDER_PATH)
print("Folders created")

if not os.path.exists(config.TRAINING_USER_CHOICE_SAVE_PATH):
    with open(config.TRAINING_USER_CHOICE_SAVE_PATH, 'w') as f:
        json.dump({"data_column_number": 2, "id_name": "S1", "model_choice": "LSTM_model", "OS": "windows"}, f)