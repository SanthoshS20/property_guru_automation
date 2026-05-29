import json

class JSONReader:

    @staticmethod
    def read_json_data_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                json_data = json.load(file)
            return json_data
        except json.JSONDecodeError as json_err:
            raise json.JSONDecodeError(f"Error decoding JSON from file: {file_path} - {json_err}")
        except FileNotFoundError:
            raise FileNotFoundError(f"file not found: {file_path}")
        except Exception as err:
            raise Exception(f"An error occurred while reading JSON data: {err}")
