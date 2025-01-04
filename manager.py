#Overall management
from user import User


class Manager:
    def __init__(self):
        self.users = {}

    def create_user(self, username):
        if username not in self.users:
            self.users[username] = User(username)
            print(f'Create a user named "{username}".')
        else:
            print(f'User "{username}" already exists.')

    def get_user(self, username):
        if username not in self.users:
            print(f'User "{username}" is not found.')
        else: 
            return self.users.get(username)

    def get_sheet(self, user, sheet_name):
        if user:
            sheet = user.sheets.get(sheet_name)
            if sheet:
                return sheet
            else:
                print(f'Sheet "{sheet_name}" not found in User "{user.username}"')

