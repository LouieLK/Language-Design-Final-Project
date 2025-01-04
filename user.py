#Define the User
from sheet import Sheet


class User:
    def __init__(self, username):
        self.username = username  
        self.sheets = {}         

    def create_sheet(self, sheet_name):     
        if sheet_name not in self.sheets:
            new_sheet = Sheet(sheet_name, self)
            self.sheets[sheet_name] = new_sheet
            print(f'Create a sheet named "{sheet_name}" for User "{self.username}".')
            return new_sheet
        else:
            print(f'Sheet "{sheet_name}" already exists for User "{self.username}".')
            return None
