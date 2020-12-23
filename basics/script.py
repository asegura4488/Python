file = open('bdt_features.csv','r')

for line in file:
        print(line)
        
read_ = file.readlines()
nlines_ = len(read_)
print ("there are {} in the file".format(nlines_))

        

        
        
