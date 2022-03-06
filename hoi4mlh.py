### maybe for when have to implement our code in a specific place, we use Python seek() function https://www.geeksforgeeks.org/python-seek-function/
from ntpath import join
import os
from sqlite3 import connect
from tkinter import *
from tkinter import ttk
import tkinter
from turtle import width
import webbrowser
from click import open_file

from more_itertools import strip

#### (Start) Tkinter stuff
root = Tk()
notebook = ttk.Notebook(root)

### Modules
def text_grid(framenum, text_label_sentence, backgroundcolor, fontcolor, text_row, text_rowspan, text_column, text_columnspan): #file directory
    text_label = Label(framenum, text=text_label_sentence, # so before text, comes the frame it's on/tab it's under.
    bg=backgroundcolor,
    fg=fontcolor,
    font="none 15").grid(row=text_row, rowspan=text_rowspan, column=text_column, columnspan=text_columnspan, sticky=W)

def toolbartab(tab_title, tab_num, tab_row, tab_rowspan, tab_column, tab_columnspan):
    tab_num = ttk.Frame(notebook)
    notebook.grid(row=tab_row, rowspan=tab_rowspan, column=tab_column, columnspan=tab_columnspan)
    notebook.add(tab_num, text=tab_title)
    return tab_num # we use return because it's like having a global parameter/varialbe.

def frame_save_button(framenum, button_label_sentence, custom_command, backgroundcolor, fontcolor, text_row, text_rowspan, text_column, text_columnspan, sticky_angle):
    Button(framenum, text=button_label_sentence,
    bg=backgroundcolor, fg=fontcolor,
    font="none 15", command=custom_command).grid(row=text_row, rowspan=text_rowspan, column=text_column, columnspan=text_columnspan, sticky=sticky_angle)

def goals_sprite_writer(line_location, sprite_id, sprite_texturefile):                       # line location is what the int value of the line that is being read from the config_directories.txt file. This will then read that line, which should be a directory/file-location. Which then it will write into the directory/file-location.
    given_line_location= open(line_location, 'a')                                            # line location will basically be the return value given from the function stripped_content from the edit_interface_files_goals & edit_interface_files_ideas functions
    countLines = len(open(line_location).readlines())
    ###   |   |    credit to:
    ###   v   v              https://www.geeksforgeeks.org/python-program-to-delete-specific-line-from-file/
    with open(line_location, 'r') as fr:                            # opening file in reading mode
        lines = fr.readlines()                                      # reading line by line
        ptr = 1                                                     # pointer for position
        with open(line_location, 'w') as fw:                        # opening file in write mode
            for line in lines:
                if ptr != countLines:                               # we want to remove the last line
                    fw.write(line)
                ptr += 1
    
    given_line_location.write("SpriteType = {\n")
    given_line_location.write("    name = \"GFX_focus_" + sprite_id + "\"\n")
    given_line_location.write("    texturefile = \"" + sprite_texturefile + "\"\n")
    given_line_location.write("}\n\n")
    given_line_location.write("}") # we need this here, because we cleared the spriteTypes curly-bracket before we pasted our code. So we need to reclose the spriteTypes

def goals_shine_sprite_writer(line_location, sprite_id, sprite_texturefile):
    given_line_location= open(line_location, 'a')
    countLines = len(open(line_location).readlines())
    with open(line_location, 'r') as fr:                            # opening file in reading mode
        lines = fr.readlines()                                      # reading line by line
        ptr = 1                                                     # pointer for position
        with open(line_location, 'w') as fw:                        # opening file in write mode
            for line in lines:
                if ptr != countLines:                               # we want to remove the last line
                    fw.write(line)
                ptr += 1

    given_line_location.write("SpriteType = {")
    given_line_location.write("    name = \"GFX_focus_" + sprite_id + "_shine\"\n")
    given_line_location.write("    texturefile = \"" + sprite_texturefile + "\"\n")
    given_line_location.write("        effectFile = \"gfx/FX/buttonstate.lua\"\n")
    given_line_location.write("    animation = {\n")
    given_line_location.write("        animationmaskfile = \"" + sprite_texturefile + "\"\n")
    given_line_location.write("        animationtexturefile = \"gfx/interface/goals/shine_overlay.dds\"\n")
    given_line_location.write("        animationrotation = -90.0\n        animationlooping = no\n        animationtime = 0.75\n        animationdelay = 0\n        animationblendmode = \"add\"\n        animationtype = \"scrolling\"\n        animationrotationoffset = { x = 0.0 y = 0.0 }\n        animationtexturescale = { x = 1.0 y = 1.0 }\n")
    given_line_location.write("    }\n\n")
    given_line_location.write("    animation = {\n")
    given_line_location.write("        animationmaskfile = \"" + sprite_texturefile + "\"\n")
    given_line_location.write("        animationtexturefile = \"gfx/interface/goals/shine_overlay.dds\"\n")
    given_line_location.write("        animationrotation = -90.0\n        animationlooping = no\n        animationtime = 0.75\n        animationdelay = 0\n        animationblendmode = \"add\"\n        animationtype = \"scrolling\"\n        animationrotationoffset = { x = 0.0 y = 0.0 }\n        animationtexturescale = { x = 1.0 y = 1.0 }\n")
    given_line_location.write("    }\n")
    given_line_location.write("    legacy_lazy_load = no\n")
    given_line_location.write("}\n\n")
    given_line_location.write("}") # we need this here, because we cleared the spriteTypes curly-bracket before we pasted our code. So we need to reclose the spriteTypes

def ideas_sprite_writer(line_location, sprite_id, sprite_texturefile):
    given_line_location = open(line_location, 'a')
    countLines = len(open(line_location).readlines())
    with open(line_location, 'r') as fr:                            # opening file in reading mode
        lines = fr.readlines()                                      # reading line by line
        ptr = 1                                                     # pointer for position
        with open(line_location, 'w') as fw:                        # opening file in write mode
            for line in lines:
                if ptr != countLines:                               # we want to remove the last line
                    fw.write(line)
                ptr += 1


    given_line_location.write("SpriteType = {\n")
    given_line_location.write("    name= \"GFX_idea_" + sprite_id + "\"\n")
    given_line_location.write("    texturefile = \"" + sprite_texturefile + "\"\n")
    given_line_location.write("}\n\n")
    given_line_location.write("}") # we need this here, because we cleared the spriteTypes curly-bracket before we pasted our code. So we need to reclose the spriteTypes

def create_config_dir_file():
    ### Directory
    config_filename = "config_directories.txt"
    __location__ = os.chdir(os.path.realpath( # credit to this https://stackoverflow.com/questions/4060221/how-to-reliably-open-a-file-in-the-same-directory-as-the-currently-running-scrip
        os.path.join(os.getcwd(), os.path.dirname(__file__)))) # The join() call prepends the current working directory, but the documentation says that if some path is absolute, all other paths left of it are dropped. Therefore, getcwd() is dropped when dirname(__file__) returns an absolute path.
    save_path = open(config_filename, 'a')                     # opens up/saves config_directories.txt, and appends to them (read & write)

    ### Getting directory info from Entry box
    goalsgfx_entry_dir = goalsgfx_entry.get()
    goalsshinegfx_entry_dir = goalsshinegfx_entry.get()
    ideasgfx_entry_dir = ideasgfx_entry.get()

    ### Saving to config file
    save_path.seek(0)
    save_path.truncate()
    save_path.write(goalsgfx_entry_dir)
    save_path.write("\n")
    save_path.write(goalsshinegfx_entry_dir)
    save_path.write("\n")
    save_path.write(ideasgfx_entry_dir)
    save_path.close

def edit_interface_files_goals():
    ### Getting directory info from Entry box
    goals_name_entry_info = goals_name_entry.get()              # name of goal
    goals_location_entry_dir = goals_location_entry.get()       # goal location

    ### Reading config_directories.txt to then go to file location for editing
    __location__ = os.chdir(os.path.realpath( 
        os.path.join(os.getcwd(), os.path.dirname(__file__)))) # opens relative path directory/location, then finds specific location (which is config_directories.txt)
    config_open_file = open("config_directories.txt", 'r') # reads in the relative path of the .py script for config_directories.txt
    
    content = config_open_file.readlines()                 # what we use here to read the lines of the file
    #^^!! to read specific line, format: content[linenumber] or content[linenumber:linenumber]
    
    ### Fixing directory location
    def stripped_content(linenumber):
        return content[linenumber].strip("\n") # we use .strip because other wise, when it writes to the gfx file, it will create a gile with the same name but with a new-line after the file extention. So we need to remove \n, because when it reads the line, it will read the line break (\n) as well
    #   ^^^ Stripped_content essentially turns our directory on the line, from having an "\n" at the ending to not having it. Thus turning our directory/file-location into an actual directory, instead of creating a new file with an "new line" at the end.

    ### Commiting change into location
    goals_sprite_writer(stripped_content(0),goals_name_entry_info, goals_location_entry_dir)         # write in goals.gfx
    goals_shine_sprite_writer(stripped_content(1),goals_name_entry_info, goals_location_entry_dir)   # write in goals_shine.gfx

def edit_interface_files_ideas():
    ### Getting directory info from Entry box
    idea_name_entry_info = idea_name_entry.get()                # name of idea
    idea_location_entry_dir = idea_location_entry.get()         # idae location

    ### Reading config_directories.txt to then go to file location for editing
    __location__ = os.chdir(os.path.realpath( 
        os.path.join(os.getcwd(), os.path.dirname(__file__)))) # opens relative path directory/location, then finds specific location (which is config_directories.txt)
    config_open_file = open("config_directories.txt", 'r') # reads in the relative path of the .py script for config_directories.txt
    
    content = config_open_file.readlines()                 # what we use here to read the lines of the file
    #^^!! to read specific line, format: content[linenumber] or content[linenumber:linenumber]
    
    ### Fixing directory location
    def stripped_content(linenumber):
        return content[linenumber].strip("\n") # we use .strip because other wise, when it writes to the gfx file, it will create a gile with the same name but with a new-line after the file extention. So we need to remove \n, because when it reads the line, it will read the line break (\n) as well

    ### Commiting change into location
    ideas_sprite_writer(stripped_content(2),idea_name_entry_info, idea_location_entry_dir)         # write in ideas.gfx

### title & window
root.geometry('')                      #determines size of window, '' for no change, something like '400x400' for defined geometry
root.title('Modders Little Helper')
root.resizable(0,0)                    #makes window size unchangable
root.configure(background='lightgrey') #makes background white
###tabs/notebooks
frame1 = toolbartab("Config", "frame1", 1, 1, 1, 1)
frame2 = toolbartab("Interface", "frame2", 1, 1, 1, 1)
frame3 = toolbartab("Info", "frame3", 1, 1, 1, 1)

### What is Displayed/UI
## FRAME1
text_grid(frame1, "File directory of goals.gfx:", "lightgrey", "black", 2, 1, 1, 2)         # ROW 1 goals.gfx
text_grid(frame1, "File directory of goals_shine.gfx:", "lightgrey", "black", 3, 1, 1, 2)   # ROW 2 goals_shine.gfx
text_grid(frame1, "File directory of ideas.gfx", "lightgrey", "black", 4, 1, 1, 1)          # ROW 3 ideas.gfx
goalsgfx_entry = Entry(frame1, width=25)                                                    # ROW 1 goals.gfx
goalsgfx_entry.grid(row=2, rowspan=1, column=3, columnspan=1, sticky=W)                     # ROW 1 goals.gfx
goalsshinegfx_entry = Entry(frame1, width=25)                                               # ROW 2 goals_shine.gfx
goalsshinegfx_entry.grid(row=3, rowspan=1, column=3, columnspan=1, sticky=W)                # ROW 2 goals_shine.gfx
ideasgfx_entry = Entry(frame1, width=25)                                                    # ROW 3 ideas.gfx
ideasgfx_entry.grid(row=4, rowspan=1, column=3, columnspan=1, sticky=W)                     # ROW 3 ideas.gfx
frame_save_button(frame1, "Save Config", create_config_dir_file, "lightgrey", "black", 5, 1, 2, 1, "W")
## FRAME 2
text_grid(frame2, "Name of Focus (I.E continous_research)", "lightgrey", "black", 2, 1, 1, 2)            #ROW 2 goals
text_grid(frame2, "Image location (I.E gfx/interface/goals/goal.dds)", "lightgrey", "black", 4, 1, 1, 2) #ROW 4 goals
text_grid(frame2, "Name of Idea (I.E continous_research)", "lightgrey", "black", 7, 1, 1, 2)             #ROW 7 ideas
text_grid(frame2, "Image location (I.E gfx/interface/ideas/idea.dds)", "lightgrey", "black", 9, 1, 1, 2)  #ROW 9 ideas
goals_name_entry = Entry(frame2, width=62)                                                               #ROW 3 goals
goals_name_entry.grid(row=3, rowspan=1, column=1, columnspan=2, sticky=W)                                #ROW 3 goals
goals_location_entry = Entry(frame2, width=62)                                                           #ROW 5 goals
goals_location_entry.grid(row=5, rowspan=1, column=1, columnspan=2, sticky=W)                            #ROW 5 goals
idea_name_entry = Entry(frame2, width=62)                                                                #ROW 8 ideas
idea_name_entry.grid(row=8, rowspan=1, column=1, columnspan=2, sticky=W)                                 #ROW 8 ideas
idea_location_entry = Entry(frame2, width=62)                                                            #ROW 10 ideas
idea_location_entry.grid(row=10, rowspan=1, column=1, columnspan=2, sticky=W)                            #ROW 10 ideas
frame_save_button(frame2, "Commit Goal", edit_interface_files_goals, "lightgrey", "black", 11, 1, 1, 1, "E")
frame_save_button(frame2, "Commit Idea", edit_interface_files_ideas, "lightgrey", "black", 11, 1, 2, 1, "W")
## FRAME3
text_grid(frame3, "Details:", "lightgrey", "black", 2, 1, 1, 1)
text_grid(frame3, "Version: ", "lightgrey", "black", 3, 1, 1, 1)
text_grid(frame3, "1.0.0", "lightgrey", "black", 3, 1, 2, 1)
text_grid(frame3, "Liscence: ", "lightgrey", "black", 4, 1, 1, 1)
text_grid(frame3, "GPL3", "lightgrey", "black", 4, 1, 2, 1)
text_grid(frame3, "Gitpage: ", "lightgrey", "black", 5, 1, 1, 1)
githublink = Button(frame3, text="Bleeplo/HOI4-Modders-Little-Helper",bg="lightgrey",fg="blue",font="none 15", cursor="hand2", command=lambda aurl='https://github.com/Bleeplo/HOI4-Modders-Little-Helper':webbrowser.open_new_tab('https://github.com/Bleeplo/HOI4-Modders-Little-Helper')).grid(row=5, rowspan=1, column=2, columnspan=1, sticky=W) # this opens up a link to the github page, both links have to be identical to each

### Main loop
root.mainloop() #keeps the window open forever, till closed
#### (End) Tkinter stuff