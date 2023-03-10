def fileLength(filename):
    try:
    	file = open(filename, 'r')
    	contents = file.read()
    	file.close()
    	print(len(contents))
    except FileNotFoundError:
        print(" File " + filename + " not found.")
    except:
        print(" Could not read file " + filename + ".")