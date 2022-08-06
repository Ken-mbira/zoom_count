import pathlib

def is_csv(file_path:str) -> bool:
    if pathlib.Path(file_path).suffix == '.csv':
        return True
    
    return False

# def date_checker(date_string:str)