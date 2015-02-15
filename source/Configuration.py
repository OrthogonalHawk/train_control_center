
def parseConfigurationFile(file_path):
    """Parse the provided configuration file and return a dictionary with the results."""
    EXPECTED_PARTS_PER_LINE = 2
    ret = {}

    configFile = open(file_path, 'rb')

    if (configFile):
    
        # read through the configuration file, looking for important values
        for line in configFile:

            # remove any trailing newline characters
            curLine = line.strip()

            # split the current line on any comma ',' characters
            parts = curLine.split(',')

            if (len(parts) == EXPECTED_PARTS_PER_LINE):
                ret[parts[0]] = parts[1]

    else:
        print "ERROR - Unable to open the provided configuration file: (%s)" % (file_path)

    print ret

    return ret

