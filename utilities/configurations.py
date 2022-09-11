import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('properties.ini')
    return config

def getPassword():
    return "pavan2"