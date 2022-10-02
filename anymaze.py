from pyamaze import maze,COLOR, agent
import shlex
import re


class YayMaze:
    #constructor for the Yaymaze class, this constructor will initialize
    #key variables such as the input file, csv file, original position of the 
    #maze, size of the maze, along with the dictionary. The key difference in this file
    #is the versatility of this script being able to use any desired size of maze in the 
    #input argument of the class
    def __init__(self, ifile, origPos=(1,1),size=4):
        self.ifile = ifile
        self.csvfile = 'mazerunning.csv'
        self.origPos = origPos
        self.size = size
        self.maze = maze(rows=self.size, cols=self.size)
        self.dict = {}
        
        #every time we call this constructor or create an object of this class
        #the following functions will run and process the input file, format it and make a csv
        self.read_and_process(ifile)
        self.fix_format(ifile)
        self.generate_csv()
        #print (self.dict)
       

    #this function will read and process the input file and store 
    # it into a dictionary
    def read_and_process(self, ifile):
        file1 = open(self.ifile, 'r')
        Lines = file1.readlines()
        count = 0
        
        #Strips the newline character
        #for each line in the input file, format and strip the data
        for line in Lines:
            count += 1
            output = self.fix_format(line.strip())
            wall = ''
            
            #this for loop will change the lidar data values into either
            #0s or 1s based on the value being greater than or less than 0.25
            for indx in range(1,5):
                if float(output[indx]) > 0.25:
                    wall = wall + '1,'
                else:
                    wall = wall + '0,'
                    
                    
            #print(wall[0:-1])
            #self.dict[str(output[0]).replace('  ',' ')] = str(tuple(output[1:5])).replace(' ','')
            
            
            #this is the most important line in the function, the first value of the input file
            #or the coordinates are stripped of spaces and placed as the key of the dictionary
            #while the four following values (N,E,S,W) are placed as the value of the dictionary
            self.dict[str(output[0]).replace('  ',' ')] = wall[0:-1]
            
            
            #this section ensures the variable type of the dictionary
            #is both an int for the dictionary value and tuple for the 
            #coordinate value 
            #print(self.dict)
            self.dict[tuple(output[0])]=tuple(output[0])
            for indx1 in range(1,5):
               output[indx1] = int(output[indx1])
           
           
           
    #this function is for formatting the input file
    #commas are replaced with comma space and the space
    #between the 5 values of the input file are deleted   
    def fix_format(self,line):
        line = line.replace(",", ", ")
        output = shlex.split(line)
        #print (output)
        output = [re.sub(r",$","",w) for w in output]
        return output
    
    
    #this function will generate the csv
    def generate_csv(self):
        
        #open the csv file and write to it
        #first write the cell and EWNS header
        with open(self.csvfile,'w') as csv_file:
            csv_file.write("  cell  ,E,W,N,S")
            csv_file.write("\n")
            
            #for j and i of 1 to 4, the strtoken will search for
            #coordinates in the organization of (j,i) in the dictionary
            for i in range (1,self.size+1):
                for j in range (1,self.size+1):
                    strtoken = '({}, {})'.format(j,i)  
                    
                    #if that coordinate is found as a key in the dictionary, the value is the following
                    #four values for EWNS
                    if strtoken in self.dict:
                        csv_file.write('"{}",{}'.format(strtoken,self.dict[strtoken]))
                        csv_file.write("\n")
                        
                    #if the coordinate is not listed as a key in the dictionary, the the value is 0000 
                    else:
                        csv_file.write('"{}",{}'.format(strtoken,"0,0,0,0"))
                        csv_file.write("\n")
                   
    #this will call pyamaze.py to generate the maze
    #using the csvfile as an input variable
    def createMaze(self):
        self.maze.CreateMaze(x=self.origPos[0],y=self.origPos[1],loopPercent=100, loadMaze=self.csvfile)
        self.maze.run()


#whenever yaymaze.py is run, the object a is created
#with the input argument of the input file. Object A will contain
#the csvfile that will feed into createMaze to generate the output maze
if __name__=="__main__":
    a = YayMaze('inputfile.txt', (1,1), size = 4)
    a.createMaze()