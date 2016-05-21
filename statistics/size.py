import files
import stats

def totalLinesOfCode(directory="./"):
    sourceFiles = files.allFiles(directory)
    total = 0
    for sourceFile in sourceFiles:
        f = open(directory + sourceFile)
        total += len(f.readlines())
        f.close()

    return total


def nonEmptyLinesOfCode(directory="./"):
    sourceFiles = files.allFiles(directory)
    total = 0
    for sourceFile in sourceFiles:
        f = open(directory + sourceFile)
        lines = f.readlines()
        f.close()
        total += len(filter(lambda line: line.strip() != "", lines))

    return total


def nonEmptyNonCommetLinesOfCode(directory="./"):
    sourceFiles = files.allFiles(directory)
    total = 0
    for sourceFile in sourceFiles:
        f = open(directory + sourceFile)
        lines = f.readlines()
        f.close()
        nonEmpty = filter(lambda line: line.strip() != "", lines)
        nonComment = filter(lambda line: line.strip().startswith("//"))
        total += len(nonComment)

    return total

def numberOfClasses(directory="./"):
    headers = files.headers()
    classNames = set()
    for headerName in headers:
        f = open(directory + headerName)
        lines = f.readlines()
        f.close()
        classNames.add(stats.findClassName())
    return len(classNames)

