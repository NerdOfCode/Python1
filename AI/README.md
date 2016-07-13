In order to use this program you must get the files then delete data.dat to begin the setup.
You need git to get all the files.

To get the files(for Mac and Linux) run the commands below in a terminal:

shopt -s extglob; rm -rf Python1; rm -rf AI; git clone https://github.com/NerdOfCode/Python1.git; rm -rf Python1/!(AI); mv Python1/AI .; rm -rf Python1 

