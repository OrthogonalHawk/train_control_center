
import pygame

from random import randint

class Configuration:

    backgroundImages = []

    optionNotFoundString = "ERROR - Unable to provide configuration option %s. No value found in file %s"

    # Expected options
    backgroundImageOption = "BackgroundImage"

    fpsOption = "FPS"

    leftButtonRectOption = "LeftButtonRect"
    leftButtonImageOption = "LeftButtonImage"
    leftButtonFileOption = "LeftButtonFile"
 
    middleButtonRectOption = "MiddleButtonRect"
    middleButtonImageOption = "MiddleButtonImage"
    middleButtonFileOption = "MiddleButtonFile"

    rightButtonRectOption = "RightButtonRect"
    rightButtonImageOption = "RightButtonImage"
    rightButtonFileOption = "RightButtonFile"

    def __init__(self, configFilePath):
        """Class constructor; parses the provided configuration file."""
        self.configFilePath = configFilePath
        self.configurationOptions = self.parseConfigurationFile(self.configFilePath)

    def _getConfigurationOption(self, optionName):
        if (optionName in self.configurationOptions.keys()):
            return self.configurationOptions[optionName]
        else:
            print self.optionNotFoundString % (optionName, self.configFilePath)
            return ""

    def parseConfigurationFile(self, configFilePath):
        """Parse the provided configuration file and return a dictionary with the results."""
        EXPECTED_PARTS_PER_LINE = 2
        ret = {}

        configFile = open(configFilePath, 'rb')

        if (configFile):
    
            # read through the configuration file, looking for important values
            for line in configFile:

                # remove any trailing newline characters
                curLine = line.strip()

                # split the current line on any comma ',' characters
                parts = curLine.split(',')

                if (len(parts) == EXPECTED_PARTS_PER_LINE):

                    # provide special handling if this is a background image option
                    if parts[0] == self.backgroundImageOption:
                        self.backgroundImages.append(parts[1])
                    else:
                        ret[parts[0]] = parts[1]

        else:
            print "ERROR - Unable to open the provided configuration file: (%s)" % (file_path)

        return ret

    def getBackgroundImagePath(self):
        return self.backgroundImages[randint(0, len(self.backgroundImages) - 1)] 

    def getFPS(self):
        return int(self._getConfigurationOption(self.fpsOption))

    def getRectOption(self, optionName):
        rectString = self._getConfigurationOption(optionName)
  
        # split this on the semi-colon characters to form a list
        rectParams = rectString.split(';')

        rectList = []
        for param in rectParams:
            rectList.append(int(param))

        return pygame.Rect(tuple(rectList))

    def getLeftButtonRect(self):
        return self.getRectOption(self.leftButtonRectOption)

    def getLeftButtonImage(self):
        return self._getConfigurationOption(self.leftButtonImageOption)

    def getLeftFile(self):
        return self._getConfigurationOption(self.leftButtonFileOption)

    def getMiddleButtonRect(self):
        return self.getRectOption(self.middleButtonRectOption)

    def getMiddleButtonImage(self):
        return self._getConfigurationOption(self.middleButtonImageOption)

    def getMiddleFile(self):
        return self._getConfigurationOption(self.middleButtonFileOption)

    def getRightButtonRect(self):
        return self.getRectOption(self.rightButtonRectOption)

    def getRightButtonImage(self):
        return self._getConfigurationOption(self.rightButtonImageOption)
   
    def getRightButtonFile(self):
        return self._getConfigurationOption(self.rightButtonFileOption)

