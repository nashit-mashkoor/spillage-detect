# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 
import re
  
# Function to rename multiple files 
def main(): 

    regs = ['1 .*', '2 .*', '3 .*' ]
    for r in regs:
        for count, filename in enumerate(os.listdir(".")): 
            if re.match(r, filename):
                print('Found a file')
            new_name = filename.replace(' ', '_')
            # rename() function will 
            # rename all the files 
            os.rename(filename, new_name) 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 