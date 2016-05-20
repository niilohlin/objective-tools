from numberOfPublicMethods import *

def headersIsClass():
    return headers()[0] == "class.h"

def propertiesIs4():
    return parseFile("class.h") == ObjectiveCClass(publicMethods=4, className="TestClass")

if __name__ == "__main__":
    print(headersIsClass())
    print(propertiesIs4())
    print(calculateAveragePublic([ObjectiveCClass(publicMethods=5, className="")]) == 5)

