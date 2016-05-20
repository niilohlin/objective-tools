
import os
from collections import namedtuple

ObjectiveCClass = namedtuple("ObjectiveCClass", "publicMethods, className")
class ObjectiveCClass(ObjectiveCClass):
    pass

def headers(directory="./"):
    files = os.listdir(directory)
    return filter(lambda f: f.endswith(".h"), files)

def findClassName(lines):
    for line in lines:
        if "@interface" in line:
            return line.split(" ")[1]
    return None

def countPublicProperties(lines):
    properties = 0
    for line in lines:
        if line.startswith("+") or line.startswith("-") or line.startswith("@property"):
            properties += 1
    return properties

def parseFile(fileName):
    f = open(fileName)
    lines = f.readlines()
    f.close()
    linesWithoutNewline = filter(lambda line: line != "\n", lines)
    className = findClassName(linesWithoutNewline)
    numberOfProperties = countPublicProperties(linesWithoutNewline)
    return ObjectiveCClass(publicMethods=numberOfProperties, className=className)

def calculateAveragePublic(classes):
    if len(classes) == 0:
        return 0
    return sum(map(lambda oClass: oClass.publicMethods, classes)) / len(classes)

def findMostPublic(classes, top=3):
    return sorted(classes, key=lambda oClass: oClass.publicMethods)[0:top]

