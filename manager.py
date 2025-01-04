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
            print(f'User is not found.')
        else: 
            return self.users.get(username)

    def get_sheet(self, username, sheet_name):
        user = self.get_user(username)
        if user:
            return user.sheets.get(sheet_name)

    def check_user(self,username):
        if username not in self.users:
            self.users[username]=User(username)
            return self.users.get(username)
        else: 
            return 
