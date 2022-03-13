#!/usr/bin/python3
from cProfile import label
from dataclasses import field
from genericpath import exists
from ntpath import join
from optparse import Option
import os
from sqlite3 import connect
from tkinter import *
from tkinter import ttk
import tkinter
from tracemalloc import start
from turtle import width
import webbrowser
from click import open_file
from more_itertools import strip
from numpy import delete

#### (Start) Tkinter stuff
root = Tk()
notebook = ttk.Notebook(root)

### Modules
def text_grid(framenum, text_label_sentence, backgroundcolor, fontcolor, text_row, text_rowspan, text_column, text_columnspan): #file directory
    text_label = Label(framenum, text=text_label_sentence, # so before text, comes the frame it's on/tab it's under.
    bg=backgroundcolor,
    fg=fontcolor,
    font="none 15").grid(row=text_row, rowspan=text_rowspan, column=text_column, columnspan=text_columnspan, sticky=W)

def smalltext_grid(framenum, text_label_sentence, backgroundcolor, fontcolor, text_row, text_rowspan, text_column, text_columnspan, stickyangle): #file directory
    text_label = Label(framenum, text=text_label_sentence, # so before text, comes the frame it's on/tab it's under.
    bg=backgroundcolor,
    fg=fontcolor,
    font="none 11").grid(row=text_row, rowspan=text_rowspan, column=text_column, columnspan=text_columnspan, sticky=stickyangle)

def toolbartab(tab_title, tab_num, tab_row, tab_rowspan, tab_column, tab_columnspan):
    tab_num = ttk.Frame(notebook)
    notebook.grid(row=tab_row, rowspan=tab_rowspan, column=tab_column, columnspan=tab_columnspan)
    notebook.add(tab_num, text=tab_title)
    return tab_num # we use return because it's like having a global parameter/varialbe.

def frame_save_button(framenum, button_label_sentence, custom_command, backgroundcolor, fontcolor, text_row, text_rowspan, text_column, text_columnspan, sticky_angle):
    Button(framenum, text=button_label_sentence,
    bg=backgroundcolor, fg=fontcolor,
    font="none 15", command=custom_command).grid(row=text_row, rowspan=text_rowspan, column=text_column, columnspan=text_columnspan, sticky=sticky_angle)

def displaybox_with_refresh_button_clipboard_button(framenum, filename, width, height, displaybox_text_row, displaybox_text_rowspan, displaybox_text_column, displaybox_text_columnspan, displaybox_stickyangle, button_backgroundcolor, button_frontcolor, button_text_row, button_text_rowspan, button_text_column, button_text_columnspan, button_sticky_angle, clipbutton_text_row, clipbutton_text_rowspan, clipbutton_text_column, clipbutton_text_columnspan, clipbutton_sticky_angle):
    __location__ = os.chdir(os.path.realpath( 
        os.path.join(os.getcwd(), os.path.dirname(__file__)))) # opens relative path directory/location, then finds specific location
    create_file = open(filename, 'a') # creates file upon launching script, we do this because otherwise reading the file in the preview box would not work
    create_file.close()

    def refresh_displaybox():
        with open(filename, 'r') as file:                 # this is what keeps the displaybox from not showing lines it has already read beforehand.
            division_template_displaybox.delete(1.0, END) # deletes contents of text box
            division_template_displaybox.insert(1.0, file.read())
        delete_content = open(filename, 'w+')             # clears file so it can display next template that was made
        delete_content.close()    

    def copy_to_clipboard():
        division_template_displaybox.clipboard_clear()
        division_template_displaybox.clipboard_append(division_template_displaybox.get(1.0, END)) # gets information from text box

    division_template_displaybox = Text(framenum, wrap=WORD, width=width, height=height)
    #displaybox.insert(INSERT, file.read())
    division_template_displaybox.grid(row=displaybox_text_row, rowspan=displaybox_text_rowspan, column=displaybox_text_column, columnspan=displaybox_text_columnspan, sticky=displaybox_stickyangle,)

    refreshbutton = Button(framenum, text="refesh", bg=button_backgroundcolor, fg=button_frontcolor,
    font="none 15", command=lambda: refresh_displaybox()).grid(row=button_text_row, rowspan=button_text_rowspan, column=button_text_column, columnspan=button_text_columnspan, sticky=button_sticky_angle)
    clipboardbutton = Button(framenum, text="copy", bg=button_backgroundcolor, fg=button_frontcolor,
    font="none 15", command=copy_to_clipboard).grid(row=clipbutton_text_row, rowspan=clipbutton_text_rowspan, column=clipbutton_text_column, columnspan=clipbutton_text_columnspan, sticky=clipbutton_sticky_angle)

def dropdownmenu_templatedesigner_namelists(framenum, text_row, text_rowspan, text_column, text_columnspan, sticky_angle):
    english_generic = [ 
    "BRENGL_INF_01", 
    "BRENGL_INFB_01", 
    "BRENGL_CAV_01", 
    "BRENGL_CAV_02", 
    "BRENGL_MOT_01", 
    "AMENGL_MOT_01", 
    "BRENGL_MEC_01", 
    "AMENGL_MEC_01", 
    "BRENGL_ARM_01",
    "BRENGL_ARM_02",
    "AMENGL_ARM_01",
    "BRENGL_PAR_01",
    "BRENGL_MAR_01",
    "BRENGL_MNT_01",
    "BRENGL_GAR_01",
    ]
    global dropdown_menu_namelists
    dropdown_menu_namelists = ttk.Combobox(framenum, 
    textvariable=english_generic,
    )
    dropdown_menu_namelists["value"] = english_generic                    ### tgus us required our else the list of options will not diplsay
    dropdown_menu_namelists.config(width=42)
    dropdown_menu_namelists.grid(row=text_row, rowspan=text_rowspan, column=text_column, columnspan=text_columnspan, sticky=sticky_angle)

def dropdownmenu_templatedesigner_regiment_type(framenum, text_row, text_rowspan, text_column, text_columnspan, sticky_angle):
    global clicked_unit_type                                    ### we declare global so we can use it in another function, to input the dropdown values
    clicked_unit_type = StringVar()
    global unit_type 
    unit_type = [ 
    "Infantry", 
    "Mobile",
    "Armored",
    ]

    global dropdown_menu_regiment_type
    dropdown_menu_regiment_type = ttk.Combobox(framenum, 
    textvariable=clicked_unit_type, state="readonly"          ### <--- textvariable is very important, because it along with many other things dictates what the other dropdownbox will display avaible
    )
    dropdown_menu_regiment_type.config(width=17)
    dropdown_menu_regiment_type.grid(row=text_row, rowspan=text_rowspan, column=text_column, columnspan=text_columnspan, sticky=sticky_angle)

def dropdownmenu_templatedesigner_regiment_unit(framenum, text_row, text_rowspan, text_column, text_columnspan, sticky_angle):
    
    def check_dropdown_list(index, value, op):                      ### This function checks to see the selected options in the unit-type-dropdownbox, then displays the corresponding units on the unit-dropdowmbox
        if clicked_unit_type.get() == unit_type[0]: # Infantry
            dropdown_menu_regiment_unit["value"] = unit_avaible_in_category_infantry
        elif clicked_unit_type.get() == unit_type[1]: # Mobile
            dropdown_menu_regiment_unit["value"] = unit_avaible_in_category_mobile
        elif clicked_unit_type.get() == unit_type[2]: # Armor/Tank
            dropdown_menu_regiment_unit["value"] = unit_avaible_in_category_armored
    
    ### Lists
    unit_avaible_in_category_infantry = [
                "infantry",
                "cavalry",
                "camelry",
                "bicycle_battalion",
                "marine",
                "mountaineers",
                "paratrooper",
                "anti_tank_brigade",
                "anti_air_brigade",
                "artillery_brigade",
                "rocket_artillery_brigade",
            ]
    unit_avaible_in_category_mobile = [
                "motorized",
                "armored_car",
                "mot_artillery_brigade",
                "mot_rocket_artillery_brigade",
                "motorized_rocket_brigade",
                "mechanized",
                "amphibious_mechanized",
            ]
    unit_avaible_in_category_armored = [
                "light_armor",
                "medium_armor",
                "heavy_armor",
                "super_heavy_armor",
                "modern_armor",
                "amphibious_armor",
                "light_sp_anti_air_brigade",
                "medium_sp_anti_air_brigade",
                "heavy_sp_anti_air_brigade",
                "super_heavy_sp_anti_air_brigade",
                "modern_sp_anti_air_brigade",
                "light_sp_artillery_brigade",
                "medium_sp_artillery_brigade",
                "heavy_sp_artillery_brigade",
                "super_heavy_sp_artillery_brigade",
                "modern_sp_artillery_brigade",
                "light_tank_destroyer_brigade",
                "medium_tank_destroyer_brigade",
                "heavy_tank_destroyer_brigade",
                "super_heavy_tank_destroyer_brigade",
                "modern_tank_destroyer_brigade",
            ]
    
    ###  |  This is more unit-type
    ###  v  related
    clicked_unit_type.trace("w", check_dropdown_list)
    dropdown_menu_regiment_type["value"] = unit_type                ### list of the unit_types. Also unit_types would not display without this command; this really belongs more in the regiment type function, but im just going to keep it here
    
    ### |   This is more unit
    ### v   related
    global dropdown_menu_regiment_unit
    dropdown_menu_regiment_unit = ttk.Combobox(framenum, state="readonly")
    dropdown_menu_regiment_unit["value"]=[""]
    dropdown_menu_regiment_unit.config(width=14)
    dropdown_menu_regiment_unit.grid(row=text_row, rowspan=text_rowspan, column=text_column, columnspan=text_columnspan, sticky=sticky_angle)

def dropdownmenu_templatedesigner_regiment_column(framenum, text_row, text_rowspan, text_column, text_columnspan, sticky_angle):
    global stringvar_regiment_column
    stringvar_regiment_column = StringVar()
    column_numberlist = ["0","0","1","2","3","4"]
    dropdown_menu = ttk.OptionMenu(framenum, stringvar_regiment_column, *column_numberlist)
    dropdown_menu.grid(row=text_row, rowspan=text_rowspan, column=text_column, columnspan=text_columnspan, sticky=sticky_angle)
    stringvar_regiment_column.set("")

def dropdownmenu_templatedesigner_regiment_starting_row(framenum, text_row, text_rowspan, text_column, text_columnspan, sticky_angle):
    global stringvar_start_row
    stringvar_start_row = StringVar()
    column_numberlist = ["0","0","1","2","3","4"]
    dropdown_menu = ttk.OptionMenu(framenum, stringvar_start_row, *column_numberlist)
    dropdown_menu.grid(row=text_row, rowspan=text_rowspan, column=text_column, columnspan=text_columnspan, sticky=sticky_angle)
    stringvar_start_row.set("")

def dropdownmenu_templatedesigner_regiment_ending_row(framenum, text_row, text_rowspan, text_column, text_columnspan, sticky_angle):
    global stringvar_end_row
    stringvar_end_row = StringVar()
    column_numberlist = ["0","0","1","2","3","4"]
    dropdown_menu = ttk.OptionMenu(framenum, stringvar_end_row, *column_numberlist)
    dropdown_menu.grid(row=text_row, rowspan=text_rowspan, column=text_column, columnspan=text_columnspan, sticky=sticky_angle)
    stringvar_end_row.set("")

def dropdownmenu_templatedesigner_support_row(framenum, text_row, text_rowspan, text_column, text_columnspan, sticky_angle):
    global stringvar_support_row
    stringvar_support_row = StringVar()
    row_numberlist = ["0","0","1","2","3"]
    dropdown_menu = ttk.OptionMenu(framenum, stringvar_support_row, *row_numberlist)
    dropdown_menu.grid(row=text_row, rowspan=text_rowspan, column=text_column, columnspan=text_columnspan, sticky=sticky_angle)
    stringvar_support_row.set("")

def dropdownmenu_templatedesigner_support_unit(framenum, text_row, text_rowspan, text_column, text_columnspan, sticky_angle):
    global stringvar_support_list
    stringvar_support_list = StringVar()
    support_list = [
        'anti_tank',
        'anti_air',
        'artillery',
        'rocket_artillery',
        'engineer',
        'recon',
        'field_hospital',
        'signal_company',
        'maintenance_company',
        'military_police'
    ]
    dropdown_menu = ttk.OptionMenu(framenum, stringvar_support_list, *support_list)
    dropdown_menu.grid(row=text_row, rowspan=text_rowspan, column=text_column, columnspan=text_columnspan, sticky=sticky_angle)
    dropdown_menu.config(width=5)
    stringvar_support_list.set("")

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

    ### Getting info from Entry boxes & dropdown boxes
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

def create_regiment_config_file():
    ### Directory
    config_filename = "regiment_constructor.txt"
    __location__ = os.chdir(os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))))
    save_path = open(config_filename, 'a')

    ### Getting directory info from Entry box
    regiment_unit = dropdown_menu_regiment_unit.get()
    regiment_column = stringvar_regiment_column.get()
    start_row = stringvar_start_row.get()
    end_row = stringvar_end_row.get()

    range_math = int(end_row) - int(start_row)
    int_start_now = int(start_row) + 1
    ### Saving to config file
    save_path.seek(0)
    save_path.write("       "+regiment_unit+" = { x = "+start_row+" y ="+regiment_column+" }\n") # print initially
    for i in range(range_math): # repeat making the same unit over and over until given row number is reached
        save_path.write(f"       {regiment_unit}")
        save_path.write(" = { x = ")
        save_path.write(f"{int_start_now} y ={regiment_column}")
        save_path.write("}\n")
        int_start_now += 1
    save_path.close

def create_support_config_file():
    ### Directory
    config_filename = "support_constructor.txt"
    __location__ = os.chdir(os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))))
    save_path = open(config_filename, 'a')

    ### Getting directory info from Entry box
    support_unit = stringvar_support_list.get()
    start_row = stringvar_support_row.get()

    ### Saving to config file
    save_path.seek(0)
    save_path.write("       "+support_unit+" = { x = "+start_row+" y = 0 }\n") # print initially
    save_path.close

def create_division_template_config_file():
    ### Directory
    config_filename = "division_template_conflig.txt"
    __location__ = os.chdir(os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))))
    save_path = open(config_filename, 'a')

    ### Getting directory info from Entry box
    division_name = custom_division_name_entry.get()
    namelist = dropdown_menu_namelists.get()

    ### Reading regiment_constructor.txt & support_constructor.txt to then copy the contents of so and then clear the txt files
    __location__ = os.chdir(os.path.realpath( 
        os.path.join(os.getcwd(), os.path.dirname(__file__)))) # opens relative path directory/location, then finds specific location (which is regiment_constructor.txt)
    regiment_config_file = open("regiment_constructor.txt", 'r+') # reads in the relative path of the .py script for regiment_constructor.txt
    regiment_file_content = regiment_config_file.readlines()

    __location__ = os.chdir(os.path.realpath( 
        os.path.join(os.getcwd(), os.path.dirname(__file__)))) # opens relative path directory/location, then finds specific location (which is support_constructor.txt)
    support_config_file = open("support_constructor.txt", 'r+') # reads in the relative path of the .py script for support_constructor.txt
    support_file_content = support_config_file.readlines()
    
    ### Saving to config file
    save_path.write("division_template = {\n")
    save_path.write("   name=\"" + division_name + "\"\n")
    save_path.write("   divisions_name_group=\""+ namelist +"\"\n\n")
    save_path.write("   regiments = {\n")
    save_path.writelines(regiment_file_content)                      # writes in the content of the regiments
    delete_file = open("regiment_constructor.txt", 'w+')             # clears file, because we no longer need the information. Makes this avaible for the next template.
    delete_file.close()
    save_path.write("   }\n\n")
    save_path.write("   support = {\n")
    save_path.writelines(support_file_content)                       # writes in the content of the support companies
    delete_file = open("support_constructor.txt", 'w+')              # clears file, because we no longer need the information. Makes this avaible for the next template.
    delete_file.close()
    save_path.write("   }\n}")

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
frame3 = toolbartab("Template Designer", "frame3", 1, 1, 1, 1)
frame4 = toolbartab("Info", "frame4", 1, 1, 1, 1)


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
text_grid(frame2, "Image location (I.E gfx/interface/ideas/idea.dds)", "lightgrey", "black", 9, 1, 1, 2) #ROW 9 ideas
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
text_grid(frame3, "Name of Division Template:", "lightgrey", "black", 2, 1, 1, 3)
custom_division_name_entry = Entry(frame3, width=43)
custom_division_name_entry.grid(row=3, rowspan=1, column=1, columnspan=3, sticky=W)

text_grid(frame3, "Namelist:", "lightgrey", "black", 4, 1, 1, 4)
dropdownmenu_templatedesigner_namelists(frame3, 5, 1, 1, 3, "W")

text_grid(frame3, "Regiments:", "lightgrey", "black", 6, 1, 1, 4)
text_grid(frame3, "Type", "lightgrey", "black", 7, 1, 1, 1)
dropdownmenu_templatedesigner_regiment_type(frame3, 7, 1, 2, 1, "W")
dropdownmenu_templatedesigner_regiment_unit(frame3, 7, 1, 3, 1, "W")

smalltext_grid(frame3, "column", "lightgrey", "black", 8, 1, 1, 1, "W")
dropdownmenu_templatedesigner_regiment_column(frame3, 8, 1, 2, 1, "W")
smalltext_grid(frame3, "starting row", "lightgrey", "black", 8, 1, 2, 1, "E")
dropdownmenu_templatedesigner_regiment_starting_row(frame3, 8, 1, 3, 1, "W")
smalltext_grid(frame3, "ending row", "lightgrey", "black", 9, 1, 1, 1, "W")
dropdownmenu_templatedesigner_regiment_ending_row(frame3, 9, 1, 2, 1, "W")
frame_save_button(frame3, "commit", create_regiment_config_file, "lightgrey", "black", 9, 1, 3, 2, "W")

text_grid(frame3, "Support:", "lightgrey", "black", 10, 1, 1, 3)
smalltext_grid(frame3, "Unit", "lightgrey", "black", 11, 1, 1, 1, "W")
dropdownmenu_templatedesigner_support_unit(frame3, 11, 1, 2, 1, "W")
smalltext_grid(frame3, "row", "lightgrey", "black", 11, 1, 2, 1, "E")
dropdownmenu_templatedesigner_support_row(frame3, 11, 1, 3, 1, "W")
frame_save_button(frame3, "commit", create_support_config_file, "lightgrey", "black", 12, 1, 1, 1, "W")
frame_save_button(frame3, "make template", create_division_template_config_file, "lightgrey", "black", 12, 1, 2, 2, "W")

displaybox_with_refresh_button_clipboard_button(frame3, 'division_template_conflig.txt', 28, 20, 2, 10, 4, 1, "W", "lightgrey", "black", 12, 1, 4, 1, "E", 12, 1, 4, 1, "W")
#frame_save_button(frame3, "copy to clipboard", )
## FRAME4
text_grid(frame4, "Details:", "lightgrey", "black", 2, 1, 1, 1)
text_grid(frame4, "Version: ", "lightgrey", "black", 3, 1, 1, 1)
text_grid(frame4, "1.2.5", "lightgrey", "black", 3, 1, 2, 1)
text_grid(frame4, "Liscence: ", "lightgrey", "black", 4, 1, 1, 1)
text_grid(frame4, "GPL3", "lightgrey", "black", 4, 1, 2, 1)
text_grid(frame4, "Gitpage: ", "lightgrey", "black", 5, 1, 1, 1)
githublink = Button(frame4, text="Bleeplo/HOI4-Modders-Little-Helper",bg="lightgrey",fg="blue",font="none 15", cursor="hand2", command=lambda aurl='https://github.com/Bleeplo/HOI4-Modders-Little-Helper':webbrowser.open_new_tab('https://github.com/Bleeplo/HOI4-Modders-Little-Helper')).grid(row=5, rowspan=1, column=2, columnspan=1, sticky=W) # this opens up a link to the github page, both links have to be identical to each

### Main loop
root.mainloop() #keeps the window open forever, till closed
#### (End) Tkinter stuff