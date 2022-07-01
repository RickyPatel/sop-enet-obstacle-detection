
import os
import sys 

input_folder = sys.argv[1]+"/"
output_folder = sys.argv[2]+"/"
for filename in os.listdir(input_folder ):
   with open(os.path.join(input_folder, filename), 'r') as f:
       if(filename.endswith(".png")):
           print(filename)
           os.system("python color-convert.py "+filename+" "+input_folder+" "+output_folder)

# exec(open("color-convert.py "+filename).read())
