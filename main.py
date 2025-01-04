from manager import Manager
#main 
def main():
    manager = Manager()
    while True:
        print("\n---------------Menu---------------")
        print("1. Create a user")
        print("2. Create a sheet")
        print("3. Check a sheet")
        print("4. Change the value in a sheet" )
        print("5. Change a sheet's access right")
        print("6. Collaborate or uncollaborate with another user")
        print("7. List all sheets with access rights")
        print("----------------------------------")
        action = input("> Input the command number: ").strip()

        if action == "1":
            print("Please enter a username.")
            username = input("> (Format: UserName): ").strip()
            if username == "":
                print("Please enter a username.")
                continue
            manager.create_user(username)
                
        elif action == "2":
            try:
                username, sheet_name = input("> (Format: UserName SheetName): ").split()
            except:
                print("Please enter data as > (Format: UserName SheetName)")
                continue
            user = manager.get_user(username)
            if user:
                new_sheet = user.create_sheet(sheet_name) 
                if new_sheet: #examine the sheet is in the list or not
                    print(f'Create a sheet named "{sheet_name}" for "{username}".')
                else:
                    print(f'Sheet "{sheet_name}" already exists for "{username}".')

        elif action == "3":
            try:
                username, sheet_name = input("> (Format: UserName SheetName): ").split()
            except:
                print("Please enter data as > (Format: UserName SheetName)")       
                continue        
            user = manager.get_user(username)
            sheet = manager.get_sheet(username, sheet_name)
            if sheet:
                print(sheet.check_sheet())
            else:
                print("Sheet or user not found.")

        elif action == "4":
            try:
                username, sheet_name = input("> (Format: UserName SheetName): ").split()
            except:
                print("Please enter data as > (Format: UserName SheetName)")    
                continue
            user = manager.get_user(username)
            sheet = manager.get_sheet(username, sheet_name)
            if sheet:
                print(sheet.check_sheet())
                try:
                    try:
                        row, col, value = input("> (Format: row col val): ").split()
                    except:
                        print("Please enter data as > (Format: row col val)")    
                        continue
                    row, col = int(row) - 1, int(col) - 1  
                    if "+" in value or "-" in value or "*" in value or "/" in value:
                        value = eval(value)
                    else:
                        value = float(value)
                    sheet.update_cell(row, col, value)
                    print(sheet.check_sheet())
                except Exception as e:
                    print("Error:", e)
            else:
                print("Sheet or user not found.")

        elif action == "5":
            try:
                username, sheet_name, access_right = input("> (Format: UserName SheetName E(Editable) or R(ReadOnly)): ").split()
            except:
                print("Please enter data as > (Format: UserName SheetName E(Editable) or R(ReadOnly)))")    
                continue
            sheet = manager.get_sheet(username, sheet_name)
            user=manager.get_user(username)
            if sheet:
                if access_right=="e" or access_right=="E":
                    sheet.change_access_right("Editable",user)
                elif access_right=="r"or access_right=="R":
                    sheet.change_access_right("ReadOnly",user)
            else:
                print("Sheet not found.")

        elif action == "6":
            try:
                username, sheet_name, collaborator_name, operation = input("> (Format: UserName SheetName Collaborator Operation(Share/Unshare)): ").split()
            except:
                print("Please enter data as > (Format: UserName SheetName Collaborator Operation(Share/Unshare))")    
                continue
            sheet = manager.get_sheet(username, sheet_name)
    
            if sheet:
                if operation=="Share":
                    collborator=manager.get_user(collaborator_name)
                    if collborator:
                        sheet.share_sheet(collborator)
                    else:
                        print(f"collborator {collaborator_name} does not exist.")
                elif operation=="Unshare":
                    collborator=manager.get_user(collaborator_name)
                    if collborator:
                        sheet.unshare_sheet(collborator)
                    else:
                        print(f"collborator {collaborator_name} does not exist.")
                else:
                    print("Invalid operation. Please use 'Share' or 'Unshare'.")
            else:
                print("Sheet or user not found.")


        elif action == "7":
            username = input("> (Format: UserName): ").strip()
            if username == "":
                print("Please enter a username.")
                continue
            user = manager.get_user(username) 
            if user:
                editable_sheets = []
                readonly_sheets = []
                
                # examine every sheets properties
                for sheet_name, sheet in user.sheets.items():
                    if sheet.access_right == "Editable":
                        editable_sheets.append(sheet_name)
                    elif sheet.access_right == "ReadOnly":
                        readonly_sheets.append(sheet_name)
                
                print(f"User: {username}")
                print(f"Sheets (Editable): {', '.join(editable_sheets) or 'None'}")
                print(f"Sheets (ReadOnly): {', '.join(readonly_sheets) or 'None'}")
            else:
                print(f"User {username} does not exist.")
        
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()


