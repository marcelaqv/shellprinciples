import subprocess #imports the system shell commands
import os
from tkinter import *   # import everything from tkinter module, tkinter gives an gui 

def execute_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
    return result.stdout

def listd():                        #creates a function that will list the files in the dir
    output_text.delete(1.0, END)    #clear text window created later 
    result = execute_command("dir") #creates a result that will store the result of the dir execution
    output_text.insert(END, result) #tkinter way of adding the text to the text window
def printdir():                     #creates a function that will print the current dir
    output_text.delete(1.0, END)    #clear text window created later 
    result = execute_command("cd")  #creates a result that will store the result of the cd execution
    output_text.insert(END, result)
    
def newdir():
    
    input_window = Toplevel(root)       #create a window for user input
    input_window.title("Enter Directory Name")  #gives the title to the new window that helps the user

    
    label = Label(input_window, text="Enter desired directory name:") #label for instruction
    label.pack()  #to show it

    # Entry widget for user input
    entry = Entry(input_window) #to get the input as entry  
    entry.pack()                #to show the window

    # Button to confirm and create the new directory
    confirm_button = Button(input_window, text="Create Directory", command=lambda: create_directory(entry.get(), input_window))  #to create the button that will submit
    confirm_button.pack()

def create_directory(directory_name, input_window):
    
    input_window.destroy()      #closes the input window

    if os.path.exists(directory_name):
        result_message = f"The directory '{directory_name}' already exists"
        output_text.delete(1.0, END)
        output_text.insert(END, result_message)
    else:
        result = execute_command(f"mkdir {directory_name}") #executes mkdir
        listd()  #show directory listing
        output_text.insert("1.0", result)
    
def concatenate():
    input_window = Toplevel(root)
    input_window.title("Enter File Paths")

    label = Label(input_window, text="Enter file paths (comma-separated):")
    label.pack()

    entry = Entry(input_window)
    entry.pack()

    confirm_button = Button(input_window, text="Concatenate Files", command=lambda: concatenated(entry.get(), input_window))
    confirm_button.pack()

def concatenated(file_paths, input_window):
    input_window.destroy()
    output_text.delete("1.0", END)

    paths = file_paths.split(',')
    if len(paths) != 2:
        output_text.insert(END, "Provide two file names (including .txt)")
    else:
        file1_path, file2_path = paths
        if not (os.path.exists(file1_path.strip()) and os.path.exists(file2_path.strip())):
            output_text.insert(END, "One or both of the provided file paths do not exist.")
        else: 
            content1 = execute_command(f"type {file1_path.strip()}")
            content2 = execute_command(f"type {file2_path.strip()}")

        # Create a new file and write the concatenated contents
            with open("new_file.txt", "w") as new_file:
                new_file.write(content1)
                new_file.write("\n\n")  # Add a separator between contents
                new_file.write(content2)

            output_text.insert(END, f"New file 'new_file.txt' created with the contents of {file1_path.strip()} and {file2_path.strip()}")


    
def deldir(): #i added the delete because i started creating folder to test and i wanted a way to remove them 
    # Create a Toplevel window for user input
    input_window = Toplevel(root)
    input_window.title("Enter Directory Name")

    # Label for instruction
    label = Label(input_window, text="Enter directory name:")
    label.pack()

    # Entry widget for user input
    entry = Entry(input_window)
    entry.pack()

    # Button to confirm and delete the directory
    confirm_button = Button(input_window, text="Delete Directory", command=lambda: delete_dir(entry.get(), input_window))
    confirm_button.pack()

def delete_dir(directory_name, input_window):
    # Close the input window
    input_window.destroy()

    # Perform the directory deletion
    output_text.delete("1.0", END)  # Clear previous output
    result = execute_command(f"rmdir /s /q {directory_name}")
    listd()
    output_text.insert("1.0", result)
def messageInput():
    
    input_window = Toplevel(root)       #create a window for user input
    input_window.title("Enter a message to display")  #gives the title to the new window that helps the user

    
    label = Label(input_window, text="Enter a message to display:") #label for instruction
    label.pack()  #to show it

    # Entry widget for user input
    entry = Entry(input_window) #to get the input as entry  
    entry.pack()                #to show the window

    # Button to confirm and create the new directory
    confirm_button = Button(input_window, text="Create message", command=lambda: message(entry.get(), input_window))  #to create the button that will submit
    confirm_button.pack()
    

def message(messages, input_window):
    output_text.delete(1.0, END)  # Clear previous output
    ##need to get user to enter what message

    result = execute_command(f"echo the message: {messages}")
    output_text.insert(END, result)
    
# create a tkinter window
root = Tk()              
##root.maxsize(200, 200) 
# Open window having dimension 100x100
root.geometry('1000x8000') 
w = Label(root, text ='Operating Systems HW1:', font = "50")  
w.pack() 
w = Label(root, text ='Shell Commands', font = "25")  
w.pack() 




# Create a Button
btn1 = Button(root, text = 'List directory contents', bd = '5',
                          command = listd) 
btn1.pack(side = 'top') 
btn2 = Button(root, text = 'Print working directory', bd = '5',
                          command = printdir) 
# Set the position of button on the top of window.   
btn2.pack(side = 'top')    
btn3 = Button(root, text = 'Create a new directory', bd = '5',
                          command = newdir) 
btn3.pack(side = 'top') 

btn6 = Button(root, text = 'Delete dir', bd = '5',
                          command = deldir) 
# Set the position of button on the top of window.   
btn6.pack(side = 'top') 

btn4 = Button(root, text = 'Display a message', bd = '5',
                          command = messageInput) 
# Set the position of button on the top of window.   
btn4.pack(side = 'top') 
btn5 = Button(root, text = 'Concatenate and display content of a file', bd = '5',
                          command = concatenate) 
btn5.pack(side = 'top') 
 

# Text widget to display command output
output_text = Text(root, height=20, width=80)
output_text.pack()


# Create a Button
btn7 = Button(root, text = 'Exit !', bd = '5',
                          command = root.quit) 
# Set the position of button on the top of window.   
btn7.pack(side = 'top') 

root.mainloop()



