import numpy as np
from termcolor import colored
import sys
sys.path.append(r'../build/x64/Release')
import NumC

####################################################################################
def doTest():
    print(colored('Testing Methods Module', 'magenta'))

    print(colored('Testing abs scalar', 'cyan'))
    randValue = np.random.randint(-100, -1, [1,]).astype(np.double).item()
    if NumC.abs(randValue) == np.abs(randValue):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing abs array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(-100, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumC.abs(cArray), np.abs(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing add', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumC.NdArray(shape)
    cArray2 = NumC.NdArray(shape)
    data1 = np.random.randint(-100, 100, [shape.rows, shape.cols])
    data2 = np.random.randint(-100, 100, [shape.rows, shape.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumC.add(cArray1, cArray2), data1 + data2):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing alen array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(-100, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if NumC.alen(cArray) == shape.rows:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing all: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if NumC.all(cArray, NumC.Axis.NONE).astype(np.bool).item() == np.all(data).item():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing all: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumC.all(cArray, NumC.Axis.ROW).flatten().astype(np.bool), np.all(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing all: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumC.all(cArray, NumC.Axis.COL).flatten().astype(np.bool), np.all(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing allclose', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumC.NdArray(shape)
    cArray2 = NumC.NdArray(shape)
    cArray3 = NumC.NdArray(shape)
    tolerance = 1e-5
    data1 = np.random.randn(shape.rows, shape.cols)
    data2 = data1 + tolerance / 10
    data3 = data1 + 1
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    cArray3.setArray(data3)
    if NumC.allclose(cArray1, cArray2, tolerance) and not NumC.allclose(cArray1, cArray3, tolerance):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing amax: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if NumC.amax(cArray, NumC.Axis.NONE).item() == np.max(data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing amax: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumC.amax(cArray, NumC.Axis.ROW).flatten(), np.max(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing amax: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumC.amax(cArray, NumC.Axis.COL).flatten(), np.max(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing amin: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if NumC.amin(cArray, NumC.Axis.NONE).item() == np.min(data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing amin: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumC.amin(cArray, NumC.Axis.ROW).flatten(), np.min(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing amin: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumC.amin(cArray, NumC.Axis.COL).flatten(), np.min(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing any: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if NumC.any(cArray, NumC.Axis.NONE).astype(np.bool).item() == np.any(data).item():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing any: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumC.any(cArray, NumC.Axis.ROW).flatten().astype(np.bool), np.any(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing any: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumC.any(cArray, NumC.Axis.COL).flatten().astype(np.bool), np.any(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arange', 'cyan'))
    start = np.random.randn(1).item()
    stop = np.random.randn(1).item() * 100
    step = np.abs(np.random.randn(1).item())
    if stop < start:
        step *= -1
    data = np.arange(start, stop, step)
    if np.array_equal(np.round(NumC.arange(start, stop, step).flatten(), 10), np.round(data, 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arccos scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item())
    if np.round(NumC.arccos(value), 10) == np.round(np.arccos(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arccos array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumC.arccos(cArray), 10), np.round(np.arccos(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arccosh scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item()) + 1
    if np.round(NumC.arccosh(value), 10) == np.round(np.arccosh(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arccosh array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols) + 1
    cArray.setArray(data)
    if np.array_equal(np.round(NumC.arccosh(cArray), 10), np.round(np.arccosh(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arcsin scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item())
    if np.round(NumC.arcsin(value), 10) == np.round(np.arcsin(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arcsin array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumC.arcsin(cArray), 10), np.round(np.arcsin(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arcsinh scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item())
    if np.round(NumC.arcsinh(value), 10) == np.round(np.arcsinh(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arcsinh array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumC.arcsinh(cArray), 10), np.round(np.arcsinh(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arctan scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item())
    if np.round(NumC.arctan(value), 10) == np.round(np.arctan(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arctan array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumC.arctan(cArray), 10), np.round(np.arctan(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arctanh scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item())
    if np.round(NumC.arctanh(value), 10) == np.round(np.arctanh(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arctanh array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumC.arctanh(cArray), 10), np.round(np.arctanh(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argmax: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumC.argmax(cArray, NumC.Axis.NONE).item(), np.argmax(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argmax: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumC.argmax(cArray, NumC.Axis.ROW).flatten(), np.argmax(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argmax: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumC.argmax(cArray, NumC.Axis.COL).flatten(), np.argmax(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argmin: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumC.argmin(cArray, NumC.Axis.NONE).item(), np.argmin(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argmin: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumC.argmin(cArray, NumC.Axis.ROW).flatten(), np.argmin(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argmin: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumC.argmin(cArray, NumC.Axis.COL).flatten(), np.argmin(data, axis=1)):
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
    if np.array_equal(dataFlat[NumC.argsort(cArray, NumC.Axis.NONE).flatten().astype(np.uint32)], dataFlat[np.argsort(data, axis=None)]):
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
    cIdx = NumC.argsort(cArray, NumC.Axis.ROW).astype(np.uint16)
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
    cIdx = NumC.argsort(cArray, NumC.Axis.COL).astype(np.uint16)
    allPass = True
    for idx, row in enumerate(data):
        if not np.array_equal(row[cIdx[idx, :]], row[pIdx[idx, :]]):
            allPass = False
            break
    if allPass:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing around scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item()) * np.random.randint(1, 10, [1,]).item()
    numDecimalsRound = np.random.randint(0, 10, [1,]).astype(np.uint8).item()
    if NumC.around(value, numDecimalsRound) == np.round(value, numDecimalsRound):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing around array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols) * np.random.randint(1, 10, [1,]).item()
    cArray.setArray(data)
    numDecimalsRound = np.random.randint(0, 10, [1,]).astype(np.uint8).item()
    if np.array_equal(NumC.around(cArray, numDecimalsRound), np.round(data, numDecimalsRound)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing array_equal', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumC.NdArray(shape)
    cArray2 = NumC.NdArray(shape)
    cArray3 = NumC.NdArray(shape)
    data1 = np.random.randint(1, 100, shapeInput)
    data2 = np.random.randint(1, 100, shapeInput)
    cArray1.setArray(data1)
    cArray2.setArray(data1)
    cArray3.setArray(data2)
    if NumC.array_equal(cArray1, cArray2) and not NumC.array_equal(cArray1, cArray3):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing array_equiv', 'cyan'))
    shapeInput1 = np.random.randint(1, 100, [2, ])
    shapeInput3 = np.random.randint(1, 100, [2, ])
    shape1 = NumC.Shape(shapeInput1[0].item(), shapeInput1[1].item())
    shape2 = NumC.Shape(shapeInput1[1].item(), shapeInput1[0].item())
    shape3 = NumC.Shape(shapeInput3[0].item(), shapeInput3[1].item())
    cArray1 = NumC.NdArray(shape1)
    cArray2 = NumC.NdArray(shape2)
    cArray3 = NumC.NdArray(shape3)
    data1 = np.random.randint(1, 100, shapeInput1)
    data3 = np.random.randint(1, 100, shapeInput3)
    cArray1.setArray(data1)
    cArray2.setArray(data1.reshape([shapeInput1[1].item(), shapeInput1[0].item()]))
    cArray3.setArray(data3)
    if NumC.array_equiv(cArray1, cArray2) and not NumC.array_equiv(cArray1, cArray3):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing average: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if NumC.average(cArray, NumC.Axis.NONE).item() == np.average(data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing average: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumC.average(cArray, NumC.Axis.ROW).flatten(), np.average(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing average: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumC.average(cArray, NumC.Axis.COL).flatten(), np.average(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing average weighted: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    cWeights = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    weights = np.random.randint(1, 5, [shape.rows, shape.cols])
    cArray.setArray(data)
    cWeights.setArray(weights)
    if NumC.average(cArray, cWeights, NumC.Axis.NONE).item() == np.average(data, weights=weights):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing average weighted: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    cWeights = NumC.NdArray(1, shape.cols)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    weights = np.random.randint(1, 5, [1, shape.rows])
    cArray.setArray(data)
    cWeights.setArray(weights)
    if np.array_equal(NumC.average(cArray, cWeights, NumC.Axis.ROW).flatten(), np.average(data, weights=weights.flatten(), axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing average weighted: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    cWeights = NumC.NdArray(1, shape.rows)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    weights = np.random.randint(1, 5, [1, shape.cols])
    cWeights.setArray(weights)
    cArray.setArray(data)
    if np.array_equal(NumC.average(cArray, cWeights, NumC.Axis.COL).flatten(), np.average(data, weights=weights.flatten(), axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing bincount', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArrayInt(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint16)
    cArray.setArray(data)
    if np.array_equal(NumC.bincount(cArray, 0).flatten(), np.bincount(data.flatten(), minlength=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing bincount with minLength', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArrayInt(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint16)
    cArray.setArray(data)
    minLength = int(data.max() + 10)
    if np.array_equal(NumC.bincount(cArray, minLength).flatten(), np.bincount(data.flatten(), minlength=minLength)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing bincount weighted', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArrayInt(shape)
    cWeights = NumC.NdArrayInt(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint16)
    weights = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint16)
    cArray.setArray(data)
    cWeights.setArray(weights)
    if np.array_equal(NumC.bincount(cArray, cWeights, 0).flatten(), np.bincount(data.flatten(), minlength=0, weights=weights.flatten())):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing bincount weighted with minLength', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArrayInt(shape)
    cWeights = NumC.NdArrayInt(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint16)
    weights = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint16)
    cArray.setArray(data)
    cWeights.setArray(weights)
    minLength = int(data.max() + 10)
    if np.array_equal(NumC.bincount(cArray, cWeights, minLength).flatten(), np.bincount(data.flatten(), minlength=minLength, weights=weights.flatten())):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing bitwise_and', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumC.NdArrayInt64(shape)
    cArray2 = NumC.NdArrayInt64(shape)
    data1 = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint64)
    data2 = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint64)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumC.bitwise_and(cArray1, cArray2), np.bitwise_and(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing bitwise_not', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArrayInt64(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint64)
    cArray.setArray(data)
    if np.array_equal(NumC.bitwise_not(cArray), np.bitwise_not(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing bitwise_or', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumC.NdArrayInt64(shape)
    cArray2 = NumC.NdArrayInt64(shape)
    data1 = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint64)
    data2 = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint64)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumC.bitwise_or(cArray1, cArray2), np.bitwise_or(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing bitwise_xor', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumC.NdArrayInt64(shape)
    cArray2 = NumC.NdArrayInt64(shape)
    data1 = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint64)
    data2 = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint64)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumC.bitwise_xor(cArray1, cArray2), np.bitwise_xor(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cbrt', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    if np.array_equal(np.round(NumC.cbrt(cArray), 10), np.round(np.cbrt(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing ceil', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randn(shape.rows, shape.cols).astype(np.double) * 1000
    cArray.setArray(data)
    if np.array_equal(np.round(NumC.ceil(cArray), 10), np.round(np.ceil(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing clip scalar', 'cyan'))
    value = np.random.randint(0, 100, [1, ]).item()
    minValue = np.random.randint(0, 10, [1, ]).item()
    maxValue = np.random.randint(90, 100, [1, ]).item()
    if NumC.clip(value, minValue, maxValue) == np.clip(value, minValue, maxValue):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing clip array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    minValue = np.random.randint(0, 10, [1, ]).item()
    maxValue = np.random.randint(90, 100, [1, ]).item()
    if np.array_equal(NumC.clip(cArray, minValue, maxValue), np.clip(data, minValue, maxValue)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing copy', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumC.copy(cArray), data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing copysign', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumC.NdArray(shape)
    cArray2 = NumC.NdArray(shape)
    data1 = np.random.randint(-100, 100, [shape.rows, shape.cols])
    data2 = np.random.randint(-100, 100, [shape.rows, shape.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumC.copysign(cArray1, cArray2), np.copysign(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing copyto', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumC.NdArray(shape)
    cArray2 = NumC.NdArray()
    data1 = np.random.randint(-100, 100, [shape.rows, shape.cols])
    cArray1.setArray(data1)
    if np.array_equal(NumC.copyto(cArray2, cArray1), data1):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cos scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item())
    if np.round(NumC.cos(value), 10) == np.round(np.cos(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cos array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumC.cos(cArray), 10), np.round(np.cos(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cosh scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item())
    if np.round(NumC.cos(value), 10) == np.round(np.cos(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cosh array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumC.cosh(cArray), 10), np.round(np.cosh(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing count_nonzero: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 3, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if NumC.count_nonzero(cArray, NumC.Axis.NONE) == np.count_nonzero(data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing count_nonzero: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 3, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumC.count_nonzero(cArray, NumC.Axis.ROW).flatten(), np.count_nonzero(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing count_nonzero: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 3, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumC.count_nonzero(cArray, NumC.Axis.COL).flatten(), np.count_nonzero(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cube array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumC.cube(cArray), 10), np.round(data * data * data, 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cumprod: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 5, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 4, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumC.cumprod(cArray, NumC.Axis.NONE).flatten().astype(np.uint32), data.cumprod()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cumprod: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 5, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 4, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumC.cumprod(cArray, NumC.Axis.ROW).astype(np.uint32), data.cumprod(axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cumprod: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(1, 5, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 4, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumC.cumprod(cArray, NumC.Axis.COL).astype(np.uint32), data.cumprod(axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cumsum: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumC.cumsum(cArray, NumC.Axis.NONE).flatten().astype(np.uint32), data.cumsum()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cumsum: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumC.cumsum(cArray, NumC.Axis.ROW).astype(np.uint32), data.cumsum(axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cumsum: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumC.cumsum(cArray, NumC.Axis.COL).astype(np.uint32), data.cumsum(axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing deg2rad scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item()) * 360
    if np.round(NumC.deg2rad(value), 10) == np.round(np.deg2rad(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing deg2rad array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols) * 360
    cArray.setArray(data)
    if np.array_equal(np.round(NumC.deg2rad(cArray), 10), np.round(np.deg2rad(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing diagflat array', 'cyan'))
    numElements = np.random.randint(1, 25, [1, ]).item()
    shape = NumC.Shape(1, numElements)
    elements = np.random.randint(1, 100, [numElements,])
    cElements = NumC.NdArray(shape)
    cElements.setArray(elements)
    if np.array_equal(NumC.diagflat(cElements), np.diagflat(elements)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing diagonal: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    offset = np.random.randint(0, min(shape.rows, shape.cols), [1, ]).item()
    if np.array_equal(NumC.diagonal(cArray, offset, NumC.Axis.ROW).astype(np.uint32).flatten(),
                      np.diagonal(data, offset, axis1=1, axis2=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing diagonal: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    offset = np.random.randint(0, min(shape.rows, shape.cols), [1, ]).item()
    if np.array_equal(NumC.diagonal(cArray, offset, NumC.Axis.COL).astype(np.uint32).flatten(),
                      np.diagonal(data, offset, axis1=0, axis2=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing sqr array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumC.sqr(cArray), 10), np.round(data * data, 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing power array scalar', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    exponent = np.random.randint(0, 5, [1, ]).item()
    cArray.setArray(data)
    if np.array_equal(np.round(NumC.power(cArray, exponent), 10), np.round(np.power(data, exponent), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing power array array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2, ])
    shape = NumC.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumC.NdArray(shape)
    cExponents = NumC.NdArrayInt8(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    exponents = np.random.randint(0, 5, [shape.rows, shape.cols]).astype(np.uint8)
    cArray.setArray(data)
    cExponents.setArray(exponents)
    if np.array_equal(np.round(NumC.power(cArray, cExponents), 10), np.round(np.power(data, exponents), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

####################################################################################
if __name__ == '__main__':
    doTest()