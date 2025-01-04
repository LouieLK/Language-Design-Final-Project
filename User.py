#Define the User
class User:
    def __init__(self, username):
        self.username = username  
        self.sheets = {}         

    def create_sheet(self, sheet_name):     
        if sheet_name not in self.sheets:
            new_sheet = Sheet(sheet_name, self)
            self.sheets[sheet_name] = new_sheet
            return new_sheet
        return None