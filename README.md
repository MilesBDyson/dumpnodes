# dumpnodes
mod for creating an automated colors.txt file to be used with Mapserver

this is a revised version of just the autogenerating-colors.txt of https://github.com/minetest/minetestmapper repo..

1. install dumpnodes as a mod on your server
2. enable it and add dumpnodes to your trusted mods list or temp. disable the mod security to allow dumpnodes to writ files.
2. start server and use chat command /dumpnodes
3. exit server
4. Make shure to disable this mod in your server for it does not have any privs and any one can exicute it...(needs privs added)
5. find the nodes.txt file, likley in minetest root folder if not in the mod dumpnodes folder.
6. move nodes.txt file to mods/dumpnodes folder
7. run bash ./gen.sh to create your colors.txt file
8. after inspection of the colors.txt file move it to your world folder where the mapserver binary is.
9. restart mapservre to see the changes.

Notes:

1. I had to use pip to unstall pil and install pillow to get the avgcolors.py to work properly in Xubuntu 18.04.
2. if you get file not found you will need to edit gen.sh and change the GAME_PATH and MODS_PATH accordingly.

