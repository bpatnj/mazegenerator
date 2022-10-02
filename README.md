# mazegenerator
Maze generator using Pyamaze (INSTRUCTIONS BELOW)

1. First things first, ensure that you have python 3 installed in your environment, this code will not run without the prerequisite python packages installed.
2. The code requires a few items in your directory. First download pyamaze.py and yaymaze.py, or a combination of either pyamaze.py/example.py or pyamaze.py/anymaze.py into your desired work directory.
3. Next, download the input file, inputfile.txt into your directory as well. If you desire to use anymaze.py and generate a csvfile and output maze for any desired maze size, ensure that the dimensions of your input file match your desired maze size.
4. With those files in your desired directory, ensure that your input file is labelled correctly in line 107, where an object "a" of type maze will be created with your input file in mind. 
5. Do not mess with any of the input arguments in the CreateMaze function at line 100 as they are required for pyamaze.py. 
6. If you are using yaymaze.py, ensure your maze rows and cols match the input file and size set in the input argument of the class constructor.
7. If you made any edits to your csvfile after running yaymaze.py or anymaze.py, ensure that you delete the generate csvfile, as it will not update on successive runs. 
8. Otherwise, enjoy creating mazes.
