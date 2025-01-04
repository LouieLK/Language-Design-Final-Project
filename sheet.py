#Define Sheet content
class Sheet:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.access_right = "Editable"  # Initial access right
        self.content = [[0 for _ in range(3)] for _ in range(3)]  # Default 3x3 space
        self.permissions = {"owner": owner.username}
    
    # def check_sheet(self):
    #     return "\n".join([", ".join(map(str, row)) for row in self.content])

    def check_sheet(self):
        column_widths = [max(len(str(item)) for item in column) for column in zip(*self.content)]
        aligned_rows = []
        for row in self.content:
            aligned_row = [str(item).rjust(width) for item, width in zip(row, column_widths)]
            aligned_rows.append(", ".join(aligned_row))
        return "\n".join(aligned_rows)
    
    def update_cell(self, row, col, value):
        try:
            if self.access_right == "ReadOnly":
                print("This sheet is not accessible.")
            else:
                self.content[row][col] = value
        except IndexError:
            print("Invalid cell position.")

    def change_access_right(self, access_right, user):
        # Ensure only the owner can change the access right
        if user.username == self.owner.username:
            self.access_right = access_right
            print(f"Changed access rights of {self.name} to {access_right}.")
        else:
            print("Only the owner can edit the sheet's permission.")

    def share_sheet(self, collaborator):
        if self.owner.username == collaborator.username:
            print(f"{self.owner.username} cannot share the sheet with themselves.")
        elif collaborator.username in self.permissions:
            print(f"{collaborator.username} already has access to the sheet '{self.name}'.")
        elif self.name in collaborator.sheets:
            print(f"{collaborator.username} already has the file name '{self.name}'.")

        else:
            self.permissions[collaborator.username] = "Editable"
            collaborator.sheets[self.name] = self
            print(f"{self.owner.username} shared the sheet '{self.name}' with {collaborator.username}.")

    def unshare_sheet(self, collaborator):
        if collaborator.username in self.permissions:
            del self.permissions[collaborator.username]  
            if self.name in collaborator.sheets:
                del collaborator.sheets[self.name]  
            print(f"Access to sheet '{self.name}' has been revoked from {collaborator.username}.")
        else:
            print(f"{collaborator.username} does not have access to the sheet '{self.name}'.")
