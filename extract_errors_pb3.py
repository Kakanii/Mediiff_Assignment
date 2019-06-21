import logging

# Create and configure logger
logging.basicConfig(filename="newfile.log",
                    # format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero yet!!")
logger.critical("Internet is down guys!!")

file_in = open('newfile.log','r') # Read file
output_file = open('outputfile.txt','w')
for line in file_in: # Loop every line
    if 'ERROR' in line: # Search for ERROR in line
        output_file.write(line) # Print line
    elif "WARN" in line: # Remove INFO and WARN lines
        output_file.write(line) # Print line