# dumpnodes
mod for creating an automated colors.txt file to be used with Mapserver

this is a revised version of just the autogenerating-colors.txt of https://github.com/minetest/minetestmapper repo..

1. install dumpnodes as a mod on your server
2. enable it and add dumpnodes to your trusted mods list or temp. disable the mod security to allow dumpnodes to writ files.
2. start server and use chat command /dumpnodes
3. exit server
4. find the nodes.txt file, likley in minetest root folder if not in the mod dumpnodes folder.
5. move nodes.txt file to mods/dumpnodes folder
6. run bash ./gen.sh to create your colors.txt file
7. after inspection of the colors.txt file move it to your world folder where the mapserver binary is.
8. restart mapservre to see the changes.

Note. i had to use pip to unstall pil and install pillow to get the avgcolors.py to work properly in Xubuntu 18.04.

