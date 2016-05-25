
import os
from listtools import *
from collections import namedtuple
import files

ObjectiveCClass = namedtuple("ObjectiveCClass", "publicMethods, className, sloc")
class ObjectiveCClass(ObjectiveCClass):
    pass

ObjectiveCMethod = namedtuple("ObjectiveCMethod", "numberOfParameters, methodName, decisionPoints, sloc")

def findClassName(lines):
    for line in lines:
        if "@interface" in line:
            return line.split(" ")[1]
    return None

def getLinesBetween(start, end, lines):
    return takeWhile(lambda line: not line.startswith(end) ,dropWhile(lambda line: not line.startswith(start), lines))

def countPublicProperties(lines):
    properties = 0
    intefaceLines = getLinesBetween("@interface", "@end", lines)
    for line in intefaceLines:
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
    return sorted(classes, key=lambda oClass: oClass.publicMethods, reverse=True)[0:top]


def makeReport(directory="./"):
    allHeaders = files.headers(directory)
    classes = []
    for headerFile in allHeaders:
        classes.append(parseFile(directory + headerFile))

    average = calculateAveragePublic(classes)
    mostPublic = findMostPublic(classes, 10)

    print("average = " + str(average))
    print("******* worst *******")
    for oClass in mostPublic:
        print("worst = " + str(oClass))

if __name__ == "__main__":
    makeReport("/tmp/VivaOmsorg/VivaHemtjanst/")

