import numpy as np
from termcolor import colored
import sys
sys.path.append(r'../build/x64/Release')
import NumC

####################################################################################
def doTest():
    print(colored('Testing NdArray Class', 'magenta'))

    print(colored('Testing Default Constructor', 'cyan'))
    cArray = NumC.NdArray()
    if cArray.shape().rows == 0 and cArray.shape().cols == 0 and cArray.size() == 0:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing Square Constructor', 'cyan'))
    numRowsCols = np.random.randint(1, 100, [1,]).item()
    cArray = NumC.NdArray(numRowsCols)
    a = cArray.getNumpyArray()
    if (cArray.shape().rows == numRowsCols and cArray.shape().cols == numRowsCols and
            cArray.size() == numRowsCols**2 and not a.any()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing Rectangle Constructor', 'cyan'))
    numRowsCols = np.random.randint(1, 100, [2,])
    cArray = NumC.NdArray(numRowsCols[0].item(), numRowsCols[1].item())
    a = cArray.getNumpyArray()
    if (cArray.shape().rows == numRowsCols[0] and cArray.shape().cols == numRowsCols[1] and
            cArray.size() == numRowsCols.prod() and not a.any()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing Shape Constructor', 'cyan'))
    shapeInput = np.random.randint(0, 100, [2,])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    a = cArray.getNumpyArray()
    if (cArray.shape().rows == shape.rows and cArray.shape().cols == shape.cols and
            cArray.size() == shape.rows * shape.cols and not a.any()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing All: Axis = None', 'cyan'))
    shapeInput = np.random.randint(0, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(cArray.all(NumC.Axis.NONE).astype(np.bool).item(), np.all(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing All: Axis = None', 'cyan'))
    shapeInput = np.random.randint(0, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(cArray.all(NumC.Axis.ROW).flatten().astype(np.bool), np.all(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing All: Axis = None', 'cyan'))
    shapeInput = np.random.randint(0, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(cArray.all(NumC.Axis.COL).flatten().astype(np.bool), np.all(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

####################################################################################
if __name__ == '__main__':
    doTest()