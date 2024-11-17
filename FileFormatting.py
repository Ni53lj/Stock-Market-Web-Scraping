def file_formatting():
    with open(#locatio of FILE_COMPANY_NAME_Main.txt",'r+') as edit_file:
        lines = edit_file.readlines()
        edit_file.seek(0)
        #edit_file.truncate()
        for number, line in enumerate(lines):
            if number not in range(0,9):
                edit_file.write(line)
                
