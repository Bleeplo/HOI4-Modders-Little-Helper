# HOI4-Modders-Little-Helper
Desc:A program/tool made in Python3 that helps deal with some of the tedious parts of HOI4 modding.

`# Plans can be changed at any time`
| What is implemented         | Planned to be implemented |
| ----------------------------|:-------------------------:|
|Automated goals.gfx          |Automated Localisation     |
|Automated goals_shine.gfx    |                           |
|Automated ideas.gfx          |                           |
|Automated Division Designer  |                           |

Requirements: Python3, Python Imported Libraries

Everything is really powered by os & tkinter with a few other libraries

# The way things work:
## Config
The `Config` tab is where you input all your locations of the files. This will save a txt file that will contain the locations of the files that you just inputed into the entry boxes. This is implemented, because now you don't have to keep reputting in the location of the file. It will just remember because it saved it in the .txt file mentioned previously.

![alt text][logo]

[logo]: https://github.com/Bleeplo/HOI4-Modders-Little-Helper/blob/main/screenshot_of_program/screenshot01.png?raw=true "Screenshot of Config Tab"

## Interface
The `interface` tab is where you would input the Names of things and if it is a sprite related, the location of the sprite.

![alt text][logo]

[logo]: https://github.com/Bleeplo/HOI4-Modders-Little-Helper/blob/main/screenshot_of_program/screenshot02.png?raw=true "Screenshot of Interface Tab"

## Template Designer
The `Template Designer` tab is where you would input the name of your division template, namelist, unit & their column+row, along with the support units that accompany the division.

![alt text][logo]

[logo]: https://github.com/Bleeplo/HOI4-Modders-Little-Helper/blob/main/screenshot_of_program/screenshot04.png?raw=true "Screenshot of Template Designer Tab"

## Info
The `info` tab is where information about the program is. Such as the version of the program, liscence, etc.

![alt text][logo]

[logo]: https://github.com/Bleeplo/HOI4-Modders-Little-Helper/blob/main/screenshot_of_program/screenshot03.png?raw=true "Screenshot of Info Tab"


# IMPORTANT
When you are dealing with goals.gfx,goals_shine.gfx, & ideas.gfx! Make sure the ending line is the concluding curly brackect to spriteTypes. Otherwise the script will mess up the .gfx file (to an extent)
