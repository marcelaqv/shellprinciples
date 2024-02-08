# shellprinciples

Project name: Shell Principles
By: Marcela Quintanilla

The program will reinforce the understanding of basic shell commands and their execution. This program was written using python version 3.11.5 in Visual Studio.



The program will display results using shell commands and their version for a windows system.

For functionality purposes subprocess is imported, and os
To create a GUI I imported the tkinter module

The first function that will run the commmands is the execute_command that takes the shell command as input to execute it to return it as a string

Then the functions are defined that will be called once the buttons are created. 

Overall the Tkinter command will show the user a list/menu of options that once clicked they will perform the action. Then it will display it in a window under the options.

First option on the menu is list the directories that will be perform by clicking the button and will display all items in the current directory.
The shell command that will be run is the dir

Second option will print the current directory will use cd to print it in the window below.

Third option is to create a new directory, the newdir will be called to call a window that will get user input for the new name. Then create_directory will be called to checked if there is a directory with that name exists with the os library. 
If a directory with the name already exists then will display in the window that already exists otherwise the mkdir from shell will be called to create it and then it will call the 1st option to display the elements in the directory.

Fourth option I added a delete dir that works the same as the make dir (without the validation) using the rmdir command because it was added for convenience. 

Fifth option is to display a message using the echo command, once clicked it will get the message that will be displayed from the user. 

Sixth option is to concatenate two files separated by a comma. It has the validation to check if the files exist in the dir. 
If they do then a new file named new_file.txt will be created otherwise a message will be displayed. 

Final button is the exit that closes the GUI interface for user. 


