import numpy as np
from termcolor import colored
import os
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
    shapeInput = np.random.randint(1, 100, [2,])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    a = cArray.getNumpyArray()
    if (cArray.shape().rows == shape.rows and cArray.shape().cols == shape.cols and
            cArray.size() == shape.rows * shape.cols and not a.any()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing 1D List Constructor', 'cyan'))
    if NumC.NdArray.test1DListContructor():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing 2D List Constructor', 'cyan'))
    if NumC.NdArray.test2DListContructor():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing Copy Constructor', 'cyan'))
    cArray2 = NumC.NdArray(cArray)
    if np.array_equal(cArray2.getNumpyArray(), cArray.getNumpyArray()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing at flat', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    randomIdx = np.random.randint(0, shapeInput.prod(), [1,]).item()
    if cArray.get(randomIdx) == data.flatten()[randomIdx]:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing at row/col', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    randomRowIdx = np.random.randint(0, shapeInput[0], [1,]).item()
    randomColIdx = np.random.randint(0, shapeInput[1], [1,]).item()
    if cArray.get(randomRowIdx, randomColIdx) == data[randomRowIdx, randomColIdx]:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing at slice 1D', 'cyan'))
    shapeInput = np.random.randint(100, 500, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    start = np.random.randint(0, shapeInput.prod() // 10, [1,]).item()
    stop = np.random.randint(start + 1, shapeInput.prod(), [1,]).item()
    step = np.random.randint(1, shapeInput.prod() // 10, [1,]).item()
    if np.array_equal(cArray.get(NumC.Slice(start, stop, step)).flatten().astype(np.uint32), data.flatten()[start:stop:step]):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing at slice 2D', 'cyan'))
    shapeInput = np.random.randint(100, 500, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    startRow = np.random.randint(0, shapeInput[0] // 10, [1,]).item()
    stopRow = np.random.randint(startRow + 1, shapeInput[0], [1,]).item()
    stepRow = np.random.randint(1, shapeInput[0] // 10, [1,]).item()
    startCol = np.random.randint(0, shapeInput[1] // 10, [1,]).item()
    stopCol = np.random.randint(startCol + 1, shapeInput[1], [1,]).item()
    stepCol = np.random.randint(1, shapeInput[1] // 10, [1,]).item()
    if np.array_equal(cArray.get(NumC.Slice(startRow, stopRow, stepRow), NumC.Slice(startCol, stopCol, stepCol)).astype(np.uint32),
                      data[startRow:stopRow:stepRow, startCol:stopCol:stepCol]):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing at slice 1D list', 'cyan'))
    if NumC.NdArray.testGetSlice1DList():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing at slice 2D list', 'cyan'))
    if NumC.NdArray.testGetSlice2DList():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing all: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if cArray.all(NumC.Axis.NONE).astype(np.bool).item() == np.all(data).item():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing all: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(cArray.all(NumC.Axis.ROW).flatten().astype(np.bool), np.all(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing all: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(cArray.all(NumC.Axis.COL).flatten().astype(np.bool), np.all(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing any: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if cArray.any(NumC.Axis.NONE).astype(np.bool).item() == np.any(data).item():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing any: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(cArray.any(NumC.Axis.ROW).flatten().astype(np.bool), np.any(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing any: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(cArray.any(NumC.Axis.COL).flatten().astype(np.bool), np.any(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argmax: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(cArray.argmax(NumC.Axis.NONE).item(), np.argmax(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argmax: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(cArray.argmax(NumC.Axis.ROW).flatten(), np.argmax(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argmax: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(cArray.argmax(NumC.Axis.COL).flatten(), np.argmax(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argmin: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(cArray.argmin(NumC.Axis.NONE).item(), np.argmin(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argmin: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(cArray.argmin(NumC.Axis.ROW).flatten(), np.argmin(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argmin: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(cArray.argmin(NumC.Axis.COL).flatten(), np.argmin(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argsort: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    dataFlat = data.flatten()
    if np.array_equal(dataFlat[cArray.argsort(NumC.Axis.NONE).flatten().astype(np.uint32)], dataFlat[np.argsort(data, axis=None)]):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argsort: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    pIdx = np.argsort(data, axis=0)
    cIdx = cArray.argsort(NumC.Axis.ROW).astype(np.uint16)
    allPass = True
    for idx, row in enumerate(data.T):
        if not np.array_equal(row[cIdx[:, idx]], row[pIdx[:, idx]]):
            allPass = False
            break
    if allPass:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argsort: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    pIdx = np.argsort(data, axis=1)
    cIdx = cArray.argsort(NumC.Axis.COL).astype(np.uint16)
    allPass = True
    for idx, row in enumerate(data):
        if not np.array_equal(row[cIdx[idx, :]], row[pIdx[idx, :]]):
            allPass = False
            break
    if allPass:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing clip', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(cArray.clip(5, 90).astype(np.ushort), data.clip(5, 90)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cumprod: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 5, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 4, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(cArray.cumprod(NumC.Axis.NONE).flatten().astype(np.uint32), data.cumprod()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cumprod: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 5, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 4, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(cArray.cumprod(NumC.Axis.ROW).astype(np.uint32), data.cumprod(axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cumprod: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(1, 5, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 4, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(cArray.cumprod(NumC.Axis.COL).astype(np.uint32), data.cumprod(axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cumsum: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(cArray.cumsum(NumC.Axis.NONE).flatten().astype(np.uint32), data.cumsum()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cumsum: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(cArray.cumsum(NumC.Axis.ROW).astype(np.uint32), data.cumsum(axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cumsum: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(cArray.cumsum(NumC.Axis.COL).astype(np.uint32), data.cumsum(axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing diagonal: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    offset = np.random.randint(0, min(shape.rows, shape.cols), [1,]).item()
    if np.array_equal(cArray.diagonal(offset, NumC.Axis.ROW).astype(np.uint32).flatten(), data.diagonal(offset, axis1=1, axis2=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing diagonal: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    offset = np.random.randint(0, min(shape.rows, shape.cols), [1,]).item()
    if np.array_equal(cArray.diagonal(offset, NumC.Axis.COL).astype(np.uint32).flatten(), data.diagonal(offset, axis1=0, axis2=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing dot vector', 'cyan'))
    size = np.random.randint(1, 100, [1,]).item()
    shape = NumC.Shape(1, size)
    cArray1 = NumC.NdArray(shape)
    cArray2 = NumC.NdArray(shape)
    data1 = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    data2 = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if cArray1.dot(cArray2).item() == np.dot(data1, data2.T).item():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing dot array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2,])
    shape1 = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    shape2 = NumC.Shape(shapeInput[1].item(), np.random.randint(1, 100, [1,]).item())
    cArray1 = NumC.NdArray(shape1)
    cArray2 = NumC.NdArray(shape2)
    data1 = np.random.randint(1, 50, [shape1.rows, shape1.cols], dtype=np.uint32)
    data2 = np.random.randint(1, 50, [shape2.rows, shape2.cols], dtype=np.uint32)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(cArray1.dot(cArray2), np.dot(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing dump', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    tempDir = r'C:\Temp'
    if not os.path.exists(tempDir):
        os.mkdir(tempDir)
    tempFile = os.path.join(tempDir, 'NdArrayDump.bin')
    cArray.dump(tempFile)
    if os.path.exists(tempFile):
        filesize = os.path.getsize(tempFile)
        if filesize == data.size * 8:
            print(colored('\tPASS', 'green'))
        else:
            print(colored('\tFAIL', 'red'))
    else:
        print(colored('\tFAIL', 'red'))
    os.remove(tempFile)

    print(colored('Testing fill', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    fillValue = np.random.randint(1,100, [1,]).item()
    ret = cArray.fill(fillValue)
    if np.all(ret == fillValue):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing flatten', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(cArray.flatten().astype(np.uint32), data.reshape([1, data.size])):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing item', 'cyan'))
    shape = NumC.Shape(1, 1)
    cArray = NumC.NdArray(shape)
    fillValue = np.random.randint(1, 100, [1, ]).item()
    cArray.fill(fillValue)
    if cArray.item() == fillValue:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing max: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if cArray.max(NumC.Axis.NONE).item() == np.max(data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing max: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(cArray.max(NumC.Axis.ROW).flatten(), np.max(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing max: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(cArray.max(NumC.Axis.COL).flatten(), np.max(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing min: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if cArray.min(NumC.Axis.NONE).item() == np.min(data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing min: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(cArray.min(NumC.Axis.ROW).flatten(), np.min(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing min: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(cArray.min(NumC.Axis.COL).flatten(), np.min(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing mean: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if cArray.mean(NumC.Axis.NONE).item() == np.mean(data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing mean: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(cArray.mean(NumC.Axis.ROW).flatten(), np.mean(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    # only test the odd sized array, even will not match by design
    print(colored('Testing mean: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(cArray.mean(NumC.Axis.COL).flatten(), np.mean(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing median: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    while np.prod(shapeInput) % 2 == 0:
        shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if cArray.median(NumC.Axis.NONE).item() == np.median(data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing median: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    while shapeInput[0] % 2 == 0:
        shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(cArray.median(NumC.Axis.ROW).flatten(), np.median(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing median: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    while shapeInput[1] % 2 == 0:
        shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(cArray.median(NumC.Axis.COL).flatten(), np.median(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nbytes', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if cArray.nbytes() == 8 * data.size:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing newbyteorder', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArrayInt(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols], dtype=np.uint)
    cArray.setArray(data)
    if np.array_equal(cArray.newbyteorder(NumC.Endian.BIG), data.newbyteorder()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nonzero', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(cArray.nonzero(), data.flatten().nonzero()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing norm: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if cArray.norm(NumC.Axis.NONE) == np.linalg.norm(data.flatten()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing norm: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    norms = cArray.norm(NumC.Axis.ROW).flatten()
    allPass = True
    for idx, row in enumerate(data.transpose()):
        if norms[idx] != np.linalg.norm(row):
            allPass = False
            break
    if allPass:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing norm: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    norms = cArray.norm(NumC.Axis.COL).flatten()
    allPass = True
    for idx, row in enumerate(data):
        if norms[idx] != np.linalg.norm(row):
            allPass = False
            break
    if allPass:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing ones', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    ret = cArray.ones()
    if np.all(ret == 1):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing partition: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    kthElement = np.random.randint(0, shapeInput.prod(), [1,], dtype=np.uint32).item()
    partitionedArray = cArray.partition(kthElement, NumC.Axis.NONE).flatten()
    if (np.all(partitionedArray[:kthElement] <= partitionedArray[kthElement]) and
        np.all(partitionedArray[kthElement:] >= partitionedArray[kthElement])):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing partition: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    kthElement = np.random.randint(0, shapeInput[0], [1,], dtype=np.uint32).item()
    partitionedArray = cArray.partition(kthElement, NumC.Axis.ROW).transpose()
    allPass = True
    for row in partitionedArray:
        if not (np.all(row[:kthElement] <= row[kthElement]) and
                np.all(row[kthElement:] >= row[kthElement])):
            allPass = False
            break
    if allPass:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing partition: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    kthElement = np.random.randint(0, shapeInput[1], [1,], dtype=np.uint32).item()
    partitionedArray = cArray.partition(kthElement, NumC.Axis.COL)
    allPass = True
    for row in partitionedArray:
        if not (np.all(row[:kthElement] <= row[kthElement]) and
                np.all(row[kthElement:] >= row[kthElement])):
            allPass = False
            break
    if allPass:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing prod: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 10, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 15, [shape.rows, shape.cols], dtype=np.uint32).astype(np.double)
    cArray.setArray(data)
    if cArray.prod(NumC.Axis.NONE).item() == data.prod():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing prod: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 10, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 15, [shape.rows, shape.cols], dtype=np.uint32).astype(np.double)
    cArray.setArray(data)
    if np.array_equal(cArray.prod(NumC.Axis.ROW).flatten(), data.prod(axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing prod: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(1, 10, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 15, [shape.rows, shape.cols], dtype=np.uint32).astype(np.double)
    cArray.setArray(data)
    if np.array_equal(cArray.prod(NumC.Axis.COL).flatten(), data.prod(axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing ptp: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 10, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 15, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if cArray.ptp(NumC.Axis.NONE).astype(np.uint32).item() == data.ptp():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing ptp: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 10, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 15, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(cArray.ptp(NumC.Axis.ROW).flatten().astype(np.uint32), data.ptp(axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing ptp: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(1, 10, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 15, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(cArray.ptp(NumC.Axis.COL).flatten().astype(np.uint32), data.ptp(axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing put flat', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    randomIdx = np.random.randint(0, shapeInput.prod(), [1,]).item()
    randomValue = np.random.randint(1, 500, [1, ]).item()
    cArray.put(randomIdx, randomValue)
    if cArray.get(randomIdx) == randomValue:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing put row/col', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    randomRowIdx = np.random.randint(0, shapeInput[0], [1,]).item()
    randomColIdx = np.random.randint(0, shapeInput[1], [1,]).item()
    randomValue = np.random.randint(1, 500, [1, ]).item()
    cArray.put(randomRowIdx, randomColIdx, randomValue)
    if cArray.get(randomRowIdx, randomColIdx) == randomValue:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing put slice 1D value', 'cyan'))
    shapeInput = np.random.randint(100, 500, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    start = np.random.randint(0, shapeInput.prod() // 4, [1,]).item()
    stop = np.random.randint(start + 1, shapeInput.prod(), [1,]).item()
    step = np.random.randint(1, shapeInput.prod() // 10, [1,]).item()
    randomValue = np.random.randint(1, 500, [1, ]).item()
    inputSlice = NumC.Slice(start, stop, step)
    cArray.put(inputSlice, randomValue)
    if np.all(cArray.get(inputSlice).astype(np.uint32) == randomValue):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing put slice 1D values', 'cyan'))
    shapeInput = np.random.randint(100, 500, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    start = np.random.randint(0, shapeInput.prod() // 4, [1,]).item()
    stop = np.random.randint(start + 1, shapeInput.prod(), [1,]).item()
    step = np.random.randint(1, shapeInput.prod() // 10, [1,]).item()
    inputSlice = NumC.Slice(start, stop, step)
    randomValues = np.random.randint(1, 500, [inputSlice.numElements(cArray.size()), ])
    cArray.put(inputSlice, randomValues)
    if np.array_equal(cArray.get(inputSlice).flatten().astype(np.uint32), randomValues):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing put slice 2D value', 'cyan'))
    shapeInput = np.random.randint(100, 500, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    startRow = np.random.randint(0, shapeInput[0] // 10, [1,]).item()
    stopRow = np.random.randint(startRow + 1, shapeInput[0], [1,]).item()
    stepRow = np.random.randint(1, shapeInput[0] // 10, [1,]).item()
    startCol = np.random.randint(0, shapeInput[1] // 10, [1,]).item()
    stopCol = np.random.randint(startCol + 1, shapeInput[1], [1,]).item()
    stepCol = np.random.randint(1, shapeInput[1] // 10, [1,]).item()
    inputRowSlice = NumC.Slice(startRow, stopRow, stepRow)
    inputColSlice = NumC.Slice(startCol, stopCol, stepCol)
    randomValue = np.random.randint(1, 500, [1, ]).item()
    cArray.put(inputRowSlice, inputColSlice, randomValue)
    if np.all(cArray.get(inputRowSlice, inputColSlice).astype(np.uint32) == randomValue):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing put slice 2D values', 'cyan'))
    shapeInput = np.random.randint(100, 500, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    startRow = np.random.randint(0, shapeInput[0] // 10, [1,]).item()
    stopRow = np.random.randint(startRow + 1, shapeInput[0], [1,]).item()
    stepRow = np.random.randint(1, shapeInput[0] // 10, [1,]).item()
    startCol = np.random.randint(0, shapeInput[1] // 10, [1,]).item()
    stopCol = np.random.randint(startCol + 1, shapeInput[1], [1,]).item()
    stepCol = np.random.randint(1, shapeInput[1] // 10, [1,]).item()
    inputRowSlice = NumC.Slice(startRow, stopRow, stepRow)
    inputColSlice = NumC.Slice(startCol, stopCol, stepCol)
    randomValues = np.random.randint(1, 500, [inputRowSlice.numElements(shape.rows), inputColSlice.numElements(shape.cols)])
    cArray.put(inputRowSlice, inputColSlice, randomValues)
    if np.array_equal(cArray.get(inputRowSlice, inputColSlice).astype(np.uint32), randomValues):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing put slice 1D list value', 'cyan'))
    if NumC.NdArray.testPutSlice1DValueList():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing put slice 1D list value', 'cyan'))
    if NumC.NdArray.testPutSlice1DValuesList():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing put slice 2D list value', 'cyan'))
    if NumC.NdArray.testPutSlice2DValueList():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing put slice 2D list value', 'cyan'))
    if NumC.NdArray.testPutSlice2DValuesList():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing reshape', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    newShape = NumC.Shape(shapeInput[1].item(), shapeInput[0].item())
    if np.array_equal(cArray.reshape(newShape), data.reshape(shapeInput[::-1])):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing reshape list', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    newShape = NumC.Shape(shapeInput[1].item(), shapeInput[0].item())
    if np.array_equal(cArray.reshapeList(newShape), data.reshape(shapeInput[::-1])):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing resizeFast', 'cyan'))
    shapeInput1 = np.random.randint(1, 100, [2, ])
    shapeInput2 = np.random.randint(1, 100, [2, ])
    shape1 = NumC.Shape(shapeInput1[0].item(), shapeInput1[1].item())
    shape2 = NumC.Shape(shapeInput2[0].item(), shapeInput2[1].item())
    cArray = NumC.NdArray(shape1)
    data = np.random.randint(1, 100, [shape1.rows, shape1.cols], dtype=np.uint32)
    cArray.setArray(data)
    res = cArray.resizeFast(shape2)
    if np.all(res == 0) and cArray.shape().rows == shape2.rows and cArray.shape().cols == shape2.cols:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing resizeFastList', 'cyan'))
    shapeInput1 = np.random.randint(1, 100, [2, ])
    shapeInput2 = np.random.randint(1, 100, [2, ])
    shape1 = NumC.Shape(shapeInput1[0].item(), shapeInput1[1].item())
    shape2 = NumC.Shape(shapeInput2[0].item(), shapeInput2[1].item())
    cArray = NumC.NdArray(shape1)
    data = np.random.randint(1, 100, [shape1.rows, shape1.cols], dtype=np.uint32)
    cArray.setArray(data)
    res = cArray.resizeFastList(shape2)
    if np.all(res == 0) and cArray.shape().rows == shape2.rows and cArray.shape().cols == shape2.cols:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing resizeSlow', 'cyan'))
    shapeInput1 = np.random.randint(1, 100, [2, ])
    shapeInput2 = np.random.randint(1, 100, [2, ])
    shape1 = NumC.Shape(shapeInput1[0].item(), shapeInput1[1].item())
    shape2 = NumC.Shape(shapeInput2[0].item(), shapeInput2[1].item())
    cArray = NumC.NdArray(shape1)
    data = np.random.randint(1, 100, [shape1.rows, shape1.cols], dtype=np.uint32)
    cArray.setArray(data)
    res = cArray.resizeSlow(shape2)
    if cArray.shape().rows == shape2.rows and cArray.shape().cols == shape2.cols and not np.all(res == 0):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing resizeSlowList', 'cyan'))
    shapeInput1 = np.random.randint(1, 100, [2, ])
    shapeInput2 = np.random.randint(1, 100, [2, ])
    shape1 = NumC.Shape(shapeInput1[0].item(), shapeInput1[1].item())
    shape2 = NumC.Shape(shapeInput2[0].item(), shapeInput2[1].item())
    cArray = NumC.NdArray(shape1)
    data = np.random.randint(1, 100, [shape1.rows, shape1.cols], dtype=np.uint32)
    cArray.setArray(data)
    res = cArray.resizeSlowList(shape2)
    if cArray.shape().rows == shape2.rows and cArray.shape().cols == shape2.cols and not np.all(res == 0):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing round', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randn(shape.rows, shape.cols)
    cArray.setArray(data)
    numRoundDecimals = np.random.randint(0, 10, [1,]).item()
    if np.array_equal(cArray.round(numRoundDecimals), np.round(data, numRoundDecimals)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing shape', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    if cArray.shape().rows == shape.rows and cArray.shape().cols == shape.cols:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing size', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    if cArray.size() == shapeInput.cumprod()[-1].item():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing sort: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    d = data.flatten()
    d.sort()
    if np.array_equal(cArray.sort(NumC.Axis.NONE).flatten(), d):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing sort: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    pSorted = np.sort(data, axis=0)
    cSorted = cArray.sort(NumC.Axis.ROW).astype(np.uint32)
    if np.array_equal(cSorted, pSorted):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing sort: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    pSorted = np.sort(data, axis=1)
    cSorted = cArray.sort(NumC.Axis.COL).astype(np.uint32)
    if np.array_equal(cSorted, pSorted):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing std: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.round(cArray.std(NumC.Axis.NONE).item(), 10) == np.round(np.std(data), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing std: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    if np.array_equal(np.round(cArray.std(NumC.Axis.ROW).flatten(), 10), np.round(np.std(data, axis=0), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing std: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    if np.array_equal(np.round(cArray.std(NumC.Axis.COL).flatten(), 10), np.round(np.std(data, axis=1), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing sum: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if cArray.sum(NumC.Axis.NONE).item() == np.sum(data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing sum: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    if np.array_equal(cArray.sum(NumC.Axis.ROW).flatten(), np.sum(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing sum: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    if np.array_equal(cArray.sum(NumC.Axis.COL).flatten(), np.sum(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing swapaxes', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    if np.array_equal(cArray.swapaxes(), data.T):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing tofile bin', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    filename = r'C:\Temp\temp'
    cArray.tofile(filename, '')
    if os.path.exists(filename + '.bin'):
        print(colored('\tPASS', 'green'))
        os.remove(filename + '.bin')
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing tofile txt', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    filename = r'C:\Temp\temp'
    cArray.tofile(filename, '\n')
    if os.path.exists(filename + '.txt'):
        print(colored('\tPASS', 'green'))
        os.remove(filename + '.txt')
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing toStlVector', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    out = np.asarray(cArray.toStlVector())
    if np.array_equal(out, data.flatten()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing trace: Offset=Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    offset = np.random.randint(0, shape.rows, [1,]).item()
    if np.array_equal(cArray.trace(offset, NumC.Axis.ROW), data.trace(offset, axis1=1, axis2=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing trace: Offset=Col', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    offset = np.random.randint(0, shape.rows, [1,]).item()
    if np.array_equal(cArray.trace(offset, NumC.Axis.COL), data.trace(offset, axis1=0, axis2=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing transpose', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    if np.array_equal(cArray.transpose(), data.T):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing var: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.round(cArray.var(NumC.Axis.NONE).item(), 10) == np.round(np.var(data), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing var: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    if np.array_equal(np.round(cArray.var(NumC.Axis.ROW).flatten(), 10), np.round(np.var(data, axis=0), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing var: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    if np.array_equal(np.round(cArray.var(NumC.Axis.COL).flatten(), 10), np.round(np.var(data, axis=1), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing zeros', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    cArray.zeros()
    if np.all(cArray.getNumpyArray() == 0):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator + scalar', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    randScalar = np.random.randint(1, 100, [1,]).item()
    if np.array_equal(cArray.operatorPlusScalar(randScalar), data + randScalar):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator + array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumC.NdArray(shape)
    cArray2 = NumC.NdArray(shape)
    data1 = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data2 = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(cArray1.operatorPlusArray(cArray2), data1 + data2):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator - scalar', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    randScalar = np.random.randint(1, 100, [1,]).item()
    if np.array_equal(cArray.operatorMinusScalar(randScalar), data - randScalar):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator - array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumC.NdArray(shape)
    cArray2 = NumC.NdArray(shape)
    data1 = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data2 = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(cArray1.operatorMinusArray(cArray2), data1 - data2):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator * scalar', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    randScalar = np.random.randint(1, 100, [1,]).item()
    if np.array_equal(cArray.operatorMultiplyScalar(randScalar), data * randScalar):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator * array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumC.NdArray(shape)
    cArray2 = NumC.NdArray(shape)
    data1 = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data2 = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(cArray1.operatorMultiplyArray(cArray2), data1 * data2):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator / scalar', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    randScalar = np.random.randint(1, 100, [1,]).item()
    if np.array_equal(cArray.operatorDivideScalar(randScalar), data / randScalar):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator / array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumC.NdArray(shape)
    cArray2 = NumC.NdArray(shape)
    data1 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.double)
    data2 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(cArray1.operatorDivideArray(cArray2), data1 / data2):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator % scalar', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArrayInt(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    randScalar = np.random.randint(1, 100, [1,]).item()
    if np.array_equal(cArray.operatorModulusScalar(randScalar), data % randScalar):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator % array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumC.NdArrayInt(shape)
    cArray2 = NumC.NdArrayInt(shape)
    data1 = np.random.randint(1, 100, [shape.rows, shape.cols])
    data2 = np.random.randint(1, 100, [shape.rows, shape.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(cArray1.operatorModulusArray(cArray2), data1 % data2):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator | scalar', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArrayInt(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray.setArray(data)
    randScalar = np.random.randint(1, 100, [1,]).item()
    if np.array_equal(cArray.operatorBitwiseOrScalar(randScalar), np.bitwise_or(data, randScalar)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator | array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumC.NdArrayInt(shape)
    cArray2 = NumC.NdArrayInt(shape)
    data1 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    data2 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(cArray1.operatorBitwiseOrArray(cArray2), np.bitwise_or(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator & scalar', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArrayInt(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray.setArray(data)
    randScalar = np.random.randint(1, 100, [1,]).item()
    if np.array_equal(cArray.operatorBitwiseAndScalar(randScalar), np.bitwise_and(data, randScalar)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator & array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumC.NdArrayInt(shape)
    cArray2 = NumC.NdArrayInt(shape)
    data1 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    data2 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(cArray1.operatorBitwiseAndArray(cArray2), np.bitwise_and(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator ^ scalar', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArrayInt(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray.setArray(data)
    randScalar = np.random.randint(1, 100, [1,]).item()
    if np.array_equal(cArray.operatorBitwiseXorScalar(randScalar), np.bitwise_xor(data, randScalar)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator ^ array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumC.NdArrayInt(shape)
    cArray2 = NumC.NdArrayInt(shape)
    data1 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    data2 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(cArray1.operatorBitwiseXorArray(cArray2), np.bitwise_xor(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator ~', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArrayInt(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray.setArray(data)
    if np.array_equal(cArray.operatorBitwiseNot(), ~data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator ==', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumC.NdArray(shape)
    cArray2 = NumC.NdArray(shape)
    data1 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    data2 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(cArray1.operatorEquality(cArray2), data1 == data2):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator !=', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumC.NdArray(shape)
    cArray2 = NumC.NdArray(shape)
    data1 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    data2 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(cArray1.operatorNotEquality(cArray2), data1 != data2):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator << scalar', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArrayInt(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray.setArray(data)
    randScalar = np.random.randint(1, 10, [1,]).item()
    if np.array_equal(cArray.operatorBitshiftLeft(randScalar), data << randScalar):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator >> scalar', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArrayInt(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray.setArray(data)
    randScalar = np.random.randint(1, 10, [1,]).item()
    if np.array_equal(cArray.operatorBitshiftRight(randScalar), data >> randScalar):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator post++ scalar', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray.setArray(data)
    if np.array_equal(cArray.operatorPostPlusPlus(), data) and np.array_equal(cArray.getNumpyArray(), data + 1):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator post-- scalar', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray.setArray(data)
    if np.array_equal(cArray.operatorPostMinusMinus(), data) and np.array_equal(cArray.getNumpyArray(), data - 1):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator pre++ scalar', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray.setArray(data)
    if np.array_equal(cArray.operatorPrePlusPlus(), data + 1):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing operator pre-- scalar', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray.setArray(data)
    if np.array_equal(cArray.operatorPreMinusMinus(), data - 1):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

####################################################################################
if __name__ == '__main__':
    doTest()
