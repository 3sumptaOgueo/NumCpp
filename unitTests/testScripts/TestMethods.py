import os
import numpy as np
from termcolor import colored
import sys
sys.path.append(r'../build/x64/Release')
import NumCpp

####################################################################################
def doTest():
    print(colored('Testing Methods Module', 'magenta'))

    print(colored('Testing abs scalar', 'cyan'))
    randValue = np.random.randint(-100, -1, [1,]).astype(np.double).item()
    if NumCpp.MethodsDouble.absScalar(randValue) == np.abs(randValue):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing abs array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(-100, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.absArray(cArray), np.abs(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing add', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randint(-100, 100, [shape.rows, shape.cols])
    data2 = np.random.randint(-100, 100, [shape.rows, shape.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.add(cArray1, cArray2), data1 + data2):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing alen array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(-100, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if NumCpp.MethodsDouble.alen(cArray) == shape.rows:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing all: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if NumCpp.MethodsDouble.all(cArray, NumCpp.Axis.NONE).astype(np.bool).item() == np.all(data).item():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing all: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.all(cArray, NumCpp.Axis.ROW).flatten().astype(np.bool), np.all(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing all: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.all(cArray, NumCpp.Axis.COL).flatten().astype(np.bool), np.all(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing allclose', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    cArray3 = NumCpp.NdArray(shape)
    tolerance = 1e-5
    data1 = np.random.randn(shape.rows, shape.cols)
    data2 = data1 + tolerance / 10
    data3 = data1 + 1
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    cArray3.setArray(data3)
    if NumCpp.MethodsDouble.allclose(cArray1, cArray2, tolerance) and not NumCpp.MethodsDouble.allclose(cArray1, cArray3, tolerance):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing amax: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if NumCpp.MethodsDouble.amax(cArray, NumCpp.Axis.NONE).item() == np.max(data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing amax: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.amax(cArray, NumCpp.Axis.ROW).flatten(), np.max(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing amax: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.amax(cArray, NumCpp.Axis.COL).flatten(), np.max(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing amin: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if NumCpp.MethodsDouble.amin(cArray, NumCpp.Axis.NONE).item() == np.min(data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing amin: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.amin(cArray, NumCpp.Axis.ROW).flatten(), np.min(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing amin: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.amin(cArray, NumCpp.Axis.COL).flatten(), np.min(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing any: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if NumCpp.MethodsDouble.any(cArray, NumCpp.Axis.NONE).astype(np.bool).item() == np.any(data).item():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing any: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.any(cArray, NumCpp.Axis.ROW).flatten().astype(np.bool), np.any(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing any: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.any(cArray, NumCpp.Axis.COL).flatten().astype(np.bool), np.any(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing append: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randint(0, 100, [shape.rows, shape.cols])
    data2 = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.append(cArray1, cArray2, NumCpp.Axis.NONE).getNumpyArray().flatten(), np.append(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing append: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    numRows = np.random.randint(1, 100, [1, ]).item()
    shape1 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    shape2 = NumCpp.Shape(shapeInput[0].item() + numRows, shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape1)
    cArray2 = NumCpp.NdArray(shape2)
    data1 = np.random.randint(0, 100, [shape1.rows, shape1.cols])
    data2 = np.random.randint(0, 100, [shape2.rows, shape2.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.append(cArray1, cArray2, NumCpp.Axis.ROW).getNumpyArray(), np.append(data1, data2, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing append: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    NumCppols = np.random.randint(1, 100, [1, ]).item()
    shape1 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    shape2 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item() + NumCppols)
    cArray1 = NumCpp.NdArray(shape1)
    cArray2 = NumCpp.NdArray(shape2)
    data1 = np.random.randint(0, 100, [shape1.rows, shape1.cols])
    data2 = np.random.randint(0, 100, [shape2.rows, shape2.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.append(cArray1, cArray2, NumCpp.Axis.COL).getNumpyArray(), np.append(data1, data2, axis=1)):
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
    if np.array_equal(np.round(NumCpp.MethodsDouble.arange(start, stop, step).flatten(), 10), np.round(data, 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arccos scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item())
    if np.round(NumCpp.MethodsDouble.arccosScalar(value), 10) == np.round(np.arccos(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arccos array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.arccosArray(cArray), 10), np.round(np.arccos(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arccosh scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item()) + 1
    if np.round(NumCpp.MethodsDouble.arccoshScalar(value), 10) == np.round(np.arccosh(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arccosh array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols) + 1
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.arccoshArray(cArray), 10), np.round(np.arccosh(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arcsin scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item())
    if np.round(NumCpp.MethodsDouble.arcsinScalar(value), 10) == np.round(np.arcsin(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arcsin array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.arcsinArray(cArray), 10), np.round(np.arcsin(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arcsinh scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item())
    if np.round(NumCpp.MethodsDouble.arcsinhScalar(value), 10) == np.round(np.arcsinh(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arcsinh array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.arcsinhArray(cArray), 10), np.round(np.arcsinh(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arctan scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item())
    if np.round(NumCpp.MethodsDouble.arctanScalar(value), 10) == np.round(np.arctan(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arctan array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.arctanArray(cArray), 10), np.round(np.arctan(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arctan2 scalar', 'cyan'))
    xy = NumCpp.Random.uniformOnSphere(1, 2).getNumpyArray().flatten()
    if np.round(NumCpp.MethodsDouble.arctan2Scalar(xy[1], xy[0]), 10) == np.round(np.arctan2(xy[1], xy[0]), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arctan2 array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArrayX = NumCpp.NdArray(shape)
    cArrayY = NumCpp.NdArray(shape)
    xy = NumCpp.Random.uniformOnSphere(np.prod(shapeInput).item(), 2).getNumpyArray()
    xData = xy[:, 0].reshape(shapeInput)
    yData = xy[:, 1].reshape(shapeInput)
    cArrayX.setArray(xData)
    cArrayY.setArray(yData)
    if np.array_equal(np.round(NumCpp.MethodsDouble.arctan2Array(cArrayY, cArrayX), 10), np.round(np.arctan2(yData, xData), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arctanh scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item())
    if np.round(NumCpp.MethodsDouble.arctanhScalar(value), 10) == np.round(np.arctanh(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing arctanh array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.arctanhArray(cArray), 10), np.round(np.arctanh(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argmax: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.argmax(cArray, NumCpp.Axis.NONE).item(), np.argmax(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argmax: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.argmax(cArray, NumCpp.Axis.ROW).flatten(), np.argmax(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argmax: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.argmax(cArray, NumCpp.Axis.COL).flatten(), np.argmax(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argmin: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.argmin(cArray, NumCpp.Axis.NONE).item(), np.argmin(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argmin: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.argmin(cArray, NumCpp.Axis.ROW).flatten(), np.argmin(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argmin: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.argmin(cArray, NumCpp.Axis.COL).flatten(), np.argmin(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argsort: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    dataFlat = data.flatten()
    if np.array_equal(dataFlat[NumCpp.MethodsDouble.argsort(cArray, NumCpp.Axis.NONE).flatten().astype(np.uint32)], dataFlat[np.argsort(data, axis=None)]):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argsort: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    pIdx = np.argsort(data, axis=0)
    cIdx = NumCpp.MethodsDouble.argsort(cArray, NumCpp.Axis.ROW).astype(np.uint16)
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
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    pIdx = np.argsort(data, axis=1)
    cIdx = NumCpp.MethodsDouble.argsort(cArray, NumCpp.Axis.COL).astype(np.uint16)
    allPass = True
    for idx, row in enumerate(data):
        if not np.array_equal(row[cIdx[idx, :]], row[pIdx[idx, :]]):
            allPass = False
            break
    if allPass:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing argwhere', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    randValue = np.random.randint(0,100, [1,]).item()
    data2 = data > randValue
    cArray.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.argwhere(cArray).flatten(), np.argwhere(data.flatten() > randValue).flatten()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing around scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item()) * np.random.randint(1, 10, [1,]).item()
    numDecimalsRound = np.random.randint(0, 10, [1,]).astype(np.uint8).item()
    if NumCpp.MethodsDouble.aroundScalar(value, numDecimalsRound) == np.round(value, numDecimalsRound):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing around array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols) * np.random.randint(1, 10, [1,]).item()
    cArray.setArray(data)
    numDecimalsRound = np.random.randint(0, 10, [1,]).astype(np.uint8).item()
    if np.array_equal(NumCpp.MethodsDouble.aroundArray(cArray, numDecimalsRound), np.round(data, numDecimalsRound)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing array_equal', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    cArray3 = NumCpp.NdArray(shape)
    data1 = np.random.randint(1, 100, shapeInput)
    data2 = np.random.randint(1, 100, shapeInput)
    cArray1.setArray(data1)
    cArray2.setArray(data1)
    cArray3.setArray(data2)
    if NumCpp.MethodsDouble.array_equal(cArray1, cArray2) and not NumCpp.MethodsDouble.array_equal(cArray1, cArray3):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing array_equiv', 'cyan'))
    shapeInput1 = np.random.randint(1, 100, [2, ])
    shapeInput3 = np.random.randint(1, 100, [2, ])
    shape1 = NumCpp.Shape(shapeInput1[0].item(), shapeInput1[1].item())
    shape2 = NumCpp.Shape(shapeInput1[1].item(), shapeInput1[0].item())
    shape3 = NumCpp.Shape(shapeInput3[0].item(), shapeInput3[1].item())
    cArray1 = NumCpp.NdArray(shape1)
    cArray2 = NumCpp.NdArray(shape2)
    cArray3 = NumCpp.NdArray(shape3)
    data1 = np.random.randint(1, 100, shapeInput1)
    data3 = np.random.randint(1, 100, shapeInput3)
    cArray1.setArray(data1)
    cArray2.setArray(data1.reshape([shapeInput1[1].item(), shapeInput1[0].item()]))
    cArray3.setArray(data3)
    if NumCpp.MethodsDouble.array_equiv(cArray1, cArray2) and not NumCpp.MethodsDouble.array_equiv(cArray1, cArray3):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing average: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if NumCpp.MethodsDouble.average(cArray, NumCpp.Axis.NONE).item() == np.average(data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing average: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.average(cArray, NumCpp.Axis.ROW).flatten(), np.average(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing average: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.average(cArray, NumCpp.Axis.COL).flatten(), np.average(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing average weighted: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    cWeights = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    weights = np.random.randint(1, 5, [shape.rows, shape.cols])
    cArray.setArray(data)
    cWeights.setArray(weights)
    if NumCpp.MethodsDouble.averageWeighted(cArray, cWeights, NumCpp.Axis.NONE).item() == np.average(data, weights=weights):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing average weighted: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    cWeights = NumCpp.NdArray(1, shape.cols)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    weights = np.random.randint(1, 5, [1, shape.rows])
    cArray.setArray(data)
    cWeights.setArray(weights)
    if np.array_equal(NumCpp.MethodsDouble.averageWeighted(cArray, cWeights, NumCpp.Axis.ROW).flatten(), np.average(data, weights=weights.flatten(), axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing average weighted: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    cWeights = NumCpp.NdArray(1, shape.rows)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    weights = np.random.randint(1, 5, [1, shape.cols])
    cWeights.setArray(weights)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.averageWeighted(cArray, cWeights, NumCpp.Axis.COL).flatten(), np.average(data, weights=weights.flatten(), axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing bincount', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArrayInt(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint16)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.bincount(cArray, 0).flatten(), np.bincount(data.flatten(), minlength=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing bincount with minLength', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArrayInt(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint16)
    cArray.setArray(data)
    minLength = int(data.max() + 10)
    if np.array_equal(NumCpp.MethodsDouble.bincount(cArray, minLength).flatten(), np.bincount(data.flatten(), minlength=minLength)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing bincount weighted', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArrayInt(shape)
    cWeights = NumCpp.NdArrayInt(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint16)
    weights = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint16)
    cArray.setArray(data)
    cWeights.setArray(weights)
    if np.array_equal(NumCpp.MethodsDouble.bincountWeighted(cArray, cWeights, 0).flatten(), np.bincount(data.flatten(), minlength=0, weights=weights.flatten())):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing bincount weighted with minLength', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArrayInt(shape)
    cWeights = NumCpp.NdArrayInt(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint16)
    weights = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint16)
    cArray.setArray(data)
    cWeights.setArray(weights)
    minLength = int(data.max() + 10)
    if np.array_equal(NumCpp.MethodsDouble.bincountWeighted(cArray, cWeights, minLength).flatten(), np.bincount(data.flatten(), minlength=minLength, weights=weights.flatten())):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing bitwise_and', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArrayInt64(shape)
    cArray2 = NumCpp.NdArrayInt64(shape)
    data1 = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint64)
    data2 = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint64)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.bitwise_and(cArray1, cArray2), np.bitwise_and(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing bitwise_not', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArrayInt64(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint64)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.bitwise_not(cArray), np.bitwise_not(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing bitwise_or', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArrayInt64(shape)
    cArray2 = NumCpp.NdArrayInt64(shape)
    data1 = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint64)
    data2 = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint64)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.bitwise_or(cArray1, cArray2), np.bitwise_or(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing bitwise_xor', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArrayInt64(shape)
    cArray2 = NumCpp.NdArrayInt64(shape)
    data1 = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint64)
    data2 = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint64)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.bitwise_xor(cArray1, cArray2), np.bitwise_xor(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cbrt', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.cbrtArray(cArray), 10), np.round(np.cbrt(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing ceil', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randn(shape.rows, shape.cols).astype(np.double) * 1000
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.ceilArray(cArray), 10), np.round(np.ceil(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing clip scalar', 'cyan'))
    value = np.random.randint(0, 100, [1, ]).item()
    minValue = np.random.randint(0, 10, [1, ]).item()
    maxValue = np.random.randint(90, 100, [1, ]).item()
    if NumCpp.MethodsDouble.clipScalar(value, minValue, maxValue) == np.clip(value, minValue, maxValue):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing clip array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    minValue = np.random.randint(0, 10, [1, ]).item()
    maxValue = np.random.randint(90, 100, [1, ]).item()
    if np.array_equal(NumCpp.MethodsDouble.clipArray(cArray, minValue, maxValue), np.clip(data, minValue, maxValue)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing column_stack', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape1 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    shape2 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item() + np.random.randint(1, 10, [1,]).item())
    shape3 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item() + np.random.randint(1, 10, [1,]).item())
    shape4 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item() + np.random.randint(1, 10, [1,]).item())
    cArray1 = NumCpp.NdArray(shape1)
    cArray2 = NumCpp.NdArray(shape2)
    cArray3 = NumCpp.NdArray(shape3)
    cArray4 = NumCpp.NdArray(shape4)
    data1 = np.random.randint(1, 100, [shape1.rows, shape1.cols])
    data2 = np.random.randint(1, 100, [shape2.rows, shape2.cols])
    data3 = np.random.randint(1, 100, [shape3.rows, shape3.cols])
    data4 = np.random.randint(1, 100, [shape4.rows, shape4.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    cArray3.setArray(data3)
    cArray4.setArray(data4)
    if np.array_equal(NumCpp.MethodsDouble.column_stack(cArray1, cArray2, cArray3, cArray4),
                      np.column_stack([data1, data2, data3, data4])):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing concatenate: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape1 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    shape2 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item() + np.random.randint(1, 10, [1,]).item())
    shape3 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item() + np.random.randint(1, 10, [1,]).item())
    shape4 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item() + np.random.randint(1, 10, [1,]).item())
    cArray1 = NumCpp.NdArray(shape1)
    cArray2 = NumCpp.NdArray(shape2)
    cArray3 = NumCpp.NdArray(shape3)
    cArray4 = NumCpp.NdArray(shape4)
    data1 = np.random.randint(1, 100, [shape1.rows, shape1.cols])
    data2 = np.random.randint(1, 100, [shape2.rows, shape2.cols])
    data3 = np.random.randint(1, 100, [shape3.rows, shape3.cols])
    data4 = np.random.randint(1, 100, [shape4.rows, shape4.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    cArray3.setArray(data3)
    cArray4.setArray(data4)
    if np.array_equal(NumCpp.MethodsDouble.concatenate(cArray1, cArray2, cArray3, cArray4, NumCpp.Axis.NONE).flatten(),
                      np.concatenate([data1.flatten(), data2.flatten(), data3.flatten(), data4.flatten()])):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing concatenate: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape1 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    shape2 = NumCpp.Shape(shapeInput[0].item() + np.random.randint(1, 10, [1,]).item(), shapeInput[1].item())
    shape3 = NumCpp.Shape(shapeInput[0].item() + np.random.randint(1, 10, [1,]).item(), shapeInput[1].item())
    shape4 = NumCpp.Shape(shapeInput[0].item() + np.random.randint(1, 10, [1,]).item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape1)
    cArray2 = NumCpp.NdArray(shape2)
    cArray3 = NumCpp.NdArray(shape3)
    cArray4 = NumCpp.NdArray(shape4)
    data1 = np.random.randint(1, 100, [shape1.rows, shape1.cols])
    data2 = np.random.randint(1, 100, [shape2.rows, shape2.cols])
    data3 = np.random.randint(1, 100, [shape3.rows, shape3.cols])
    data4 = np.random.randint(1, 100, [shape4.rows, shape4.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    cArray3.setArray(data3)
    cArray4.setArray(data4)
    if np.array_equal(NumCpp.MethodsDouble.concatenate(cArray1, cArray2, cArray3, cArray4, NumCpp.Axis.ROW),
                      np.concatenate([data1, data2, data3, data4], axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing concatenate: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape1 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    shape2 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item() + np.random.randint(1, 10, [1,]).item())
    shape3 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item() + np.random.randint(1, 10, [1,]).item())
    shape4 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item() + np.random.randint(1, 10, [1,]).item())
    cArray1 = NumCpp.NdArray(shape1)
    cArray2 = NumCpp.NdArray(shape2)
    cArray3 = NumCpp.NdArray(shape3)
    cArray4 = NumCpp.NdArray(shape4)
    data1 = np.random.randint(1, 100, [shape1.rows, shape1.cols])
    data2 = np.random.randint(1, 100, [shape2.rows, shape2.cols])
    data3 = np.random.randint(1, 100, [shape3.rows, shape3.cols])
    data4 = np.random.randint(1, 100, [shape4.rows, shape4.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    cArray3.setArray(data3)
    cArray4.setArray(data4)
    if np.array_equal(NumCpp.MethodsDouble.concatenate(cArray1, cArray2, cArray3, cArray4, NumCpp.Axis.COL),
                      np.concatenate([data1, data2, data3, data4], axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing contains: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    value = np.random.randint(0, 100, [1, ]).item()
    cArray.setArray(data)
    if NumCpp.MethodsDouble.contains(cArray, value, NumCpp.Axis.NONE).getNumpyArray().item() == (value in data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing contains: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    value = np.random.randint(0, 100, [1, ]).item()
    cArray.setArray(data)
    truth = list()
    for row in data:
        truth.append(value in row)
    if np.array_equal(NumCpp.MethodsDouble.contains(cArray, value, NumCpp.Axis.COL).getNumpyArray().flatten(), np.asarray(truth)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing contains: Axis = ROW', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    value = np.random.randint(0, 100, [1, ]).item()
    cArray.setArray(data)
    truth = list()
    for row in data.T:
        truth.append(value in row)
    if np.array_equal(NumCpp.MethodsDouble.contains(cArray, value, NumCpp.Axis.ROW).getNumpyArray().flatten(), np.asarray(truth)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing copy', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.copy(cArray), data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing copysign', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randint(-100, 100, [shape.rows, shape.cols])
    data2 = np.random.randint(-100, 100, [shape.rows, shape.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.copysign(cArray1, cArray2), np.copysign(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing copyto', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray()
    data1 = np.random.randint(-100, 100, [shape.rows, shape.cols])
    cArray1.setArray(data1)
    if np.array_equal(NumCpp.MethodsDouble.copyto(cArray2, cArray1), data1):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cos scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item())
    if np.round(NumCpp.MethodsDouble.cosScalar(value), 10) == np.round(np.cos(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cos array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.cosArray(cArray), 10), np.round(np.cos(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cosh scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item())
    if np.round(NumCpp.MethodsDouble.cosScalar(value), 10) == np.round(np.cos(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cosh array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.coshArray(cArray), 10), np.round(np.cosh(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing count_nonzero: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 3, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if NumCpp.MethodsDouble.count_nonzero(cArray, NumCpp.Axis.NONE) == np.count_nonzero(data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing count_nonzero: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 3, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.count_nonzero(cArray, NumCpp.Axis.ROW).flatten(), np.count_nonzero(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing count_nonzero: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 3, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.count_nonzero(cArray, NumCpp.Axis.COL).flatten(), np.count_nonzero(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cross 2D: Axis = None', 'cyan'))
    shape = NumCpp.Shape(1, 2)
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randint(1, 10, [shape.rows, shape.cols]).astype(np.double)
    data2 = np.random.randint(1, 10, [shape.rows, shape.cols]).astype(np.double)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if NumCpp.MethodsDouble.cross(cArray1, cArray2, NumCpp.Axis.NONE).item() == np.cross(data1, data2).item():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cross 2D: Axis = ROW', 'cyan'))
    shape = NumCpp.Shape(2, np.random.randint(1,100, [1, ]).item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randint(1, 10, [shape.rows, shape.cols]).astype(np.double)
    data2 = np.random.randint(1, 10, [shape.rows, shape.cols]).astype(np.double)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.cross(cArray1, cArray2, NumCpp.Axis.ROW).getNumpyArray().flatten(), np.cross(data1, data2, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cross 2D: Axis = COL', 'cyan'))
    shape = NumCpp.Shape(np.random.randint(1,100, [1, ]).item(), 2)
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randint(1, 10, [shape.rows, shape.cols]).astype(np.double)
    data2 = np.random.randint(1, 10, [shape.rows, shape.cols]).astype(np.double)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.cross(cArray1, cArray2, NumCpp.Axis.COL).getNumpyArray().flatten(), np.cross(data1, data2, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cross 3D: Axis = None', 'cyan'))
    shape = NumCpp.Shape(1, 3)
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randint(1, 10, [shape.rows, shape.cols]).astype(np.double)
    data2 = np.random.randint(1, 10, [shape.rows, shape.cols]).astype(np.double)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.cross(cArray1, cArray2, NumCpp.Axis.NONE).getNumpyArray().flatten(), np.cross(data1, data2).flatten()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cross 3D: Axis = ROW', 'cyan'))
    shape = NumCpp.Shape(3, np.random.randint(1,100, [1, ]).item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randint(1, 10, [shape.rows, shape.cols]).astype(np.double)
    data2 = np.random.randint(1, 10, [shape.rows, shape.cols]).astype(np.double)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.cross(cArray1, cArray2, NumCpp.Axis.ROW).getNumpyArray(), np.cross(data1, data2, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cross 3D: Axis = COL', 'cyan'))
    shape = NumCpp.Shape(np.random.randint(1,100, [1, ]).item(), 3)
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randint(1, 10, [shape.rows, shape.cols]).astype(np.double)
    data2 = np.random.randint(1, 10, [shape.rows, shape.cols]).astype(np.double)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.cross(cArray1, cArray2, NumCpp.Axis.COL).getNumpyArray(), np.cross(data1, data2, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cube array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.cube(cArray), 10), np.round(data * data * data, 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cumprod: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 5, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 4, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.cumprod(cArray, NumCpp.Axis.NONE).flatten().astype(np.uint32), data.cumprod()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cumprod: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 5, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 4, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.cumprod(cArray, NumCpp.Axis.ROW).astype(np.uint32), data.cumprod(axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cumprod: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(1, 5, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 4, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.cumprod(cArray, NumCpp.Axis.COL).astype(np.uint32), data.cumprod(axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cumsum: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.cumsum(cArray, NumCpp.Axis.NONE).flatten().astype(np.uint32), data.cumsum()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cumsum: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.cumsum(cArray, NumCpp.Axis.ROW).astype(np.uint32), data.cumsum(axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing cumsum: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.cumsum(cArray, NumCpp.Axis.COL).astype(np.uint32), data.cumsum(axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing deg2rad scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item()) * 360
    if np.round(NumCpp.MethodsDouble.deg2radScalar(value), 10) == np.round(np.deg2rad(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing deg2rad array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols) * 360
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.deg2radArray(cArray), 10), np.round(np.deg2rad(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing deleteIndices Slice: Axis = NONE', 'cyan'))
    shapeInput = np.asarray([100,100])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols])
    indices = NumCpp.Slice(0, 100, 4)
    indicesPy = slice(0, 99, 4)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.deleteIndicesSlice(cArray, indices, NumCpp.Axis.NONE).flatten(), np.delete(data, indicesPy, axis=None)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing deleteIndices Slice: Axis = Row', 'cyan'))
    shapeInput = np.asarray([100,100])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols])
    indices = NumCpp.Slice(0, 100, 4)
    indicesPy = slice(0, 99, 4)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.deleteIndicesSlice(cArray, indices, NumCpp.Axis.ROW), np.delete(data, indicesPy, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing deleteIndices Slice: Axis = Col', 'cyan'))
    shapeInput = np.asarray([100,100])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols])
    indices = NumCpp.Slice(0, 100, 4)
    indicesPy = slice(0, 99, 4)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.deleteIndicesSlice(cArray, indices, NumCpp.Axis.COL), np.delete(data, indicesPy, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing deleteIndices Scalar: Axis = NONE', 'cyan'))
    shapeInput = np.asarray([100,100])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols])
    index = np.random.randint(0, shape.size(), [1, ]).item()
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.deleteIndicesScalar(cArray, index, NumCpp.Axis.NONE).flatten(), np.delete(data, index, axis=None)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing deleteIndices Slice: Axis = Row', 'cyan'))
    shapeInput = np.asarray([100,100])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols])
    index = np.random.randint(0, 100, [1, ]).item()
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.deleteIndicesScalar(cArray, index, NumCpp.Axis.ROW), np.delete(data, index, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing deleteIndices Slice: Axis = Col', 'cyan'))
    shapeInput = np.asarray([100,100])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols])
    index = np.random.randint(0, 100, [1, ]).item()
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.deleteIndicesScalar(cArray, index, NumCpp.Axis.COL), np.delete(data, index, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing diagflat array', 'cyan'))
    numElements = np.random.randint(1, 25, [1, ]).item()
    shape = NumCpp.Shape(1, numElements)
    elements = np.random.randint(1, 100, [numElements,])
    cElements = NumCpp.NdArray(shape)
    cElements.setArray(elements)
    if np.array_equal(NumCpp.MethodsDouble.diagflat(cElements), np.diagflat(elements)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing diagonal: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    offset = np.random.randint(0, min(shape.rows, shape.cols), [1, ]).item()
    if np.array_equal(NumCpp.MethodsDouble.diagonal(cArray, offset, NumCpp.Axis.ROW).astype(np.uint32).flatten(),
                      np.diagonal(data, offset, axis1=1, axis2=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing diagonal: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    offset = np.random.randint(0, min(shape.rows, shape.cols), [1, ]).item()
    if np.array_equal(NumCpp.MethodsDouble.diagonal(cArray, offset, NumCpp.Axis.COL).astype(np.uint32).flatten(),
                      np.diagonal(data, offset, axis1=0, axis2=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing diff: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols]).astype(np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.diff(cArray, NumCpp.Axis.NONE).flatten().astype(np.uint32), np.diff(data.flatten())):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing diff: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols]).astype(np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.diff(cArray, NumCpp.Axis.ROW).astype(np.uint32), np.diff(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing diff: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols]).astype(np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.diff(cArray, NumCpp.Axis.COL).astype(np.uint32), np.diff(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(data)
        print(NumCpp.MethodsDouble.diff(cArray, NumCpp.Axis.COL).astype(np.uint32))
        print(colored('\tFAIL', 'red'))

    print(colored('Testing divide', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randint(1, 50, [shape.rows, shape.cols]).astype(np.double)
    data2 = np.random.randint(1, 50, [shape.rows, shape.cols]).astype(np.double)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(np.round(NumCpp.MethodsDouble.divide(cArray1, cArray2), 10), np.round(np.divide(data1, data2), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing dot vector', 'cyan'))
    size = np.random.randint(1, 100, [1,]).item()
    shape = NumCpp.Shape(1, size)
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    data2 = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if NumCpp.MethodsDouble.dot(cArray1, cArray2).astype(np.uint32).item() == np.dot(data1, data2.T).item():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing dot array', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2,])
    shape1 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    shape2 = NumCpp.Shape(shapeInput[1].item(), np.random.randint(1, 100, [1,]).item())
    cArray1 = NumCpp.NdArray(shape1)
    cArray2 = NumCpp.NdArray(shape2)
    data1 = np.random.randint(1, 50, [shape1.rows, shape1.cols], dtype=np.uint32)
    data2 = np.random.randint(1, 50, [shape2.rows, shape2.cols], dtype=np.uint32)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.dot(cArray1, cArray2).astype(np.uint32), np.dot(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing dump', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    tempDir = r'C:\Temp'
    if not os.path.exists(tempDir):
        os.mkdir(tempDir)
    tempFile = os.path.join(tempDir, 'NdArrayDump.bin')
    NumCpp.MethodsDouble.dump(cArray, tempFile)
    if os.path.exists(tempFile):
        data2 = np.fromfile(tempFile, dtype=np.double).reshape(shapeInput)
        if np.array_equal(data, data2):
            print(colored('\tPASS', 'green'))
        else:
            print(colored('\tFAIL', 'red'))
    else:
        print(colored('\tFAIL', 'red'))
    os.remove(tempFile)

    print(colored('Testing empty rectangle', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2,])
    cArray = NumCpp.MethodsDouble.emptyRowCol(shapeInput[0].item(), shapeInput[1].item())
    if (cArray.shape[0] == shapeInput[0] and cArray.shape[1] == shapeInput[1] and
            cArray.size == shapeInput.prod()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing empty Shape', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2,])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.MethodsDouble.emptyShape(shape)
    if (cArray.shape[0] == shape.rows and cArray.shape[1] == shape.cols and
            cArray.size == shapeInput.prod()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing empty_like', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2,])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.MethodsDouble.empty_like(cArray1)
    if (cArray2.shape().rows == shape.rows and cArray2.shape().cols == shape.cols and
            cArray2.size() == shapeInput.prod()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing endianess', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2,])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    if NumCpp.MethodsDouble.endianess(cArray) == NumCpp.Endian.NATIVE:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing equal', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2,])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randint(0, 10, [shape.rows, shape.cols])
    data2 = np.random.randint(0, 10, [shape.rows, shape.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.equal(cArray1, cArray2), np.equal(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing exp scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item())
    if np.round(NumCpp.MethodsDouble.expScalar(value), 10) == np.round(np.exp(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing exp array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.expArray(cArray), 10), np.round(np.exp(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing exp2 scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item())
    if np.round(NumCpp.MethodsDouble.exp2Scalar(value), 10) == np.round(np.exp2(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing exp2 array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.exp2Array(cArray), 10), np.round(np.exp2(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing expm1 scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item())
    if np.round(NumCpp.MethodsDouble.expm1Scalar(value), 10) == np.round(np.expm1(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing expm1 array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.expm1Array(cArray), 10), np.round(np.expm1(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing eye 1D', 'cyan'))
    shapeInput = np.random.randint(1, 100, [1, ]).item()
    randK = np.random.randint(0, shapeInput, [1, ]).item()
    if np.array_equal(NumCpp.MethodsDouble.eye1D(shapeInput, randK), np.eye(shapeInput, k=randK)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing eye 2D', 'cyan'))
    shapeInput = np.random.randint(10, 100, [2, ])
    randK = np.random.randint(0, shapeInput.min(), [1, ]).item()
    if np.array_equal(NumCpp.MethodsDouble.eye2D(shapeInput[0].item(), shapeInput[1].item(), randK), np.eye(shapeInput[0].item(), shapeInput[1].item(), k=randK)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing eye Shape', 'cyan'))
    shapeInput = np.random.randint(10, 100, [2, ])
    cShape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    randK = np.random.randint(0, shapeInput.min(), [1, ]).item()
    if np.array_equal(NumCpp.MethodsDouble.eyeShape(cShape, randK), np.eye(shapeInput[0].item(), shapeInput[1].item(), k=randK)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing fix scalar', 'cyan'))
    value = np.random.randn(1).item() * 100
    if NumCpp.MethodsDouble.fixScalar(value) == np.fix(value):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing fix array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randn(shape.rows, shape.cols) * 100
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.fixArray(cArray), np.fix(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing flatten', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.flatten(cArray).getNumpyArray(), np.resize(data, [1, data.size])):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing flatnonzero', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.flatnonzero(cArray).getNumpyArray().flatten(), np.flatnonzero(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing flip', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.flip(cArray, NumCpp.Axis.NONE).getNumpyArray(), np.flip(data.reshape(1, data.size), axis=1).reshape(shapeInput)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing fliplr', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.fliplr(cArray).getNumpyArray(), np.fliplr(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing flipud', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.flipud(cArray).getNumpyArray(), np.flipud(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing floor scalar', 'cyan'))
    value = np.random.randn(1).item() * 100
    if NumCpp.MethodsDouble.floorScalar(value) == np.floor(value):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing floor array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randn(shape.rows, shape.cols) * 100
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.floorArray(cArray), np.floor(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing floor_divide scalar', 'cyan'))
    value1 = np.random.randn(1).item() * 100 + 1000
    value2 = np.random.randn(1).item() * 100 + 1000
    if NumCpp.MethodsDouble.floor_divideScalar(value1, value2) == np.floor_divide(value1, value2):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing floor_divide array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randn(shape.rows, shape.cols) * 100 + 1000
    data2 = np.random.randn(shape.rows, shape.cols) * 100 + 1000
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.floor_divideArray(cArray1, cArray2), np.floor_divide(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing fmax scalar', 'cyan'))
    value1 = np.random.randn(1).item() * 100 + 1000
    value2 = np.random.randn(1).item() * 100 + 1000
    if NumCpp.MethodsDouble.fmaxScalar(value1, value2) == np.fmax(value1, value2):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing fmax array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randn(shape.rows, shape.cols) * 100 + 1000
    data2 = np.random.randn(shape.rows, shape.cols) * 100 + 1000
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.fmaxArray(cArray1, cArray2), np.fmax(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing fmin scalar', 'cyan'))
    value1 = np.random.randn(1).item() * 100 + 1000
    value2 = np.random.randn(1).item() * 100 + 1000
    if NumCpp.MethodsDouble.fminScalar(value1, value2) == np.fmin(value1, value2):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing fmin array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randn(shape.rows, shape.cols) * 100 + 1000
    data2 = np.random.randn(shape.rows, shape.cols) * 100 + 1000
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.fminArray(cArray1, cArray2), np.fmin(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing fmod scalar', 'cyan'))
    value1 = np.random.randint(1, 100, [1, ]).item() * 100 + 1000
    value2 = np.random.randint(1, 100, [1, ]).item() * 100 + 1000
    if NumCpp.MethodsDouble.fmodScalar(value1, value2) == np.fmod(value1, value2):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing fmod array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArrayInt(shape)
    cArray2 = NumCpp.NdArrayInt(shape)
    data1 = np.random.randint(1, 100, [shape.rows, shape.cols]) * 100 + 1000
    data2 = np.random.randint(1, 100, [shape.rows, shape.cols]) * 100 + 1000
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.fmodArray(cArray1, cArray2), np.fmod(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing fromfile: bin', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    tempDir = r'C:\Temp'
    if not os.path.exists(tempDir):
        os.mkdir(tempDir)
    tempFile = os.path.join(tempDir, 'NdArrayDump.bin')
    NumCpp.MethodsDouble.dump(cArray, tempFile)
    data2 = NumCpp.MethodsDouble.fromfile(tempFile, '').reshape(shape)
    if np.array_equal(data, data2):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))
    os.remove(tempFile)

    print(colored('Testing fromfile: txt', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    tempDir = r'C:\Temp'
    if not os.path.exists(tempDir):
        os.mkdir(tempDir)
    tempFile = os.path.join(tempDir, 'NdArrayDump')
    NumCpp.MethodsDouble.tofile(cArray, tempFile, '\n')
    data2 = NumCpp.MethodsDouble.fromfile(tempFile + '.txt', '\n').reshape(shape)
    if np.array_equal(data, data2):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))
    os.remove(tempFile + '.txt')

    print(colored('Testing full square', 'cyan'))
    shapeInput = np.random.randint(1, 100, [1,]).item()
    value = np.random.randint(1, 100, [1, ]).item()
    cArray = NumCpp.MethodsDouble.fullSquare(shapeInput, value)
    if (cArray.shape[0] == shapeInput and cArray.shape[1] == shapeInput and
            cArray.size == shapeInput**2 and np.all(cArray == value)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing full rectangle', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2,])
    value = np.random.randint(1, 100, [1, ]).item()
    cArray = NumCpp.MethodsDouble.fullRowCol(shapeInput[0].item(), shapeInput[1].item(), value)
    if (cArray.shape[0] == shapeInput[0] and cArray.shape[1] == shapeInput[1] and
            cArray.size == shapeInput.prod() and np.all(cArray == value)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing full Shape', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2,])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    value = np.random.randint(1, 100, [1, ]).item()
    cArray = NumCpp.MethodsDouble.fullShape(shape, value)
    if (cArray.shape[0] == shape.rows and cArray.shape[1] == shape.cols and
            cArray.size == shapeInput.prod() and np.all(cArray == value)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing full_like', 'cyan'))
    shapeInput = np.random.randint(1, 100, [2,])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    value = np.random.randint(1, 100, [1, ]).item()
    cArray2 = NumCpp.MethodsDouble.full_like(cArray1, value)
    if (cArray2.shape().rows == shape.rows and cArray2.shape().cols == shape.cols and
            cArray2.size() == shapeInput.prod() and np.all(cArray2.getNumpyArray() == value)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing greater', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    data2 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.greater(cArray1, cArray2).getNumpyArray(), np.greater(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing greater_equal array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    data2 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.greater_equal(cArray1, cArray2).getNumpyArray(), np.greater_equal(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing histogram', 'cyan'))
    shape = NumCpp.Shape(1024, 1024)
    cArray = NumCpp.NdArray(shape)
    data = np.random.randn(1024, 1024) * np.random.randint(1, 10, [1, ]).item() + np.random.randint(1, 10, [1, ]).item()
    cArray.setArray(data)
    numBins = np.random.randint(10, 30, [1,]).item()
    histogram, bins = NumCpp.MethodsDouble.histogram(cArray, numBins)
    h, b = np.histogram(data, numBins)
    if np.array_equal(histogram.getNumpyArray().flatten().astype(np.int32), h) and \
            np.array_equal(np.round(bins.getNumpyArray().flatten(), 10), np.round(b, 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing hstack', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape1 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    shape2 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item() + np.random.randint(1, 10, [1,]).item())
    shape3 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item() + np.random.randint(1, 10, [1,]).item())
    shape4 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item() + np.random.randint(1, 10, [1,]).item())
    cArray1 = NumCpp.NdArray(shape1)
    cArray2 = NumCpp.NdArray(shape2)
    cArray3 = NumCpp.NdArray(shape3)
    cArray4 = NumCpp.NdArray(shape4)
    data1 = np.random.randint(1, 100, [shape1.rows, shape1.cols])
    data2 = np.random.randint(1, 100, [shape2.rows, shape2.cols])
    data3 = np.random.randint(1, 100, [shape3.rows, shape3.cols])
    data4 = np.random.randint(1, 100, [shape4.rows, shape4.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    cArray3.setArray(data3)
    cArray4.setArray(data4)
    if np.array_equal(NumCpp.MethodsDouble.hstack(cArray1, cArray2, cArray3, cArray4),
                      np.hstack([data1, data2, data3, data4])):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing hypot scalar', 'cyan'))
    value1 = np.random.randn(1).item() * 100 + 1000
    value2 = np.random.randn(1).item() * 100 + 1000
    if NumCpp.MethodsDouble.hypotScalar(value1, value2) == np.hypot(value1, value2):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing hypot array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randn(shape.rows, shape.cols) * 100 + 1000
    data2 = np.random.randn(shape.rows, shape.cols) * 100 + 1000
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.hypotArray(cArray1, cArray2), np.hypot(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing identity', 'cyan'))
    squareSize = np.random.randint(10, 100, [1, ]).item()
    if np.array_equal(NumCpp.MethodsDouble.identity(squareSize).getNumpyArray(), np.identity(squareSize)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing intersect1d', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArrayInt(shape)
    cArray2 = NumCpp.NdArrayInt(shape)
    data1 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    data2 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.intersect1d(cArray1, cArray2).getNumpyArray().flatten(), np.intersect1d(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing invert', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArrayInt(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.invert(cArray).getNumpyArray(), np.invert(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing isclose', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.rand(shape.rows, shape.cols)
    data2 = data1 + np.random.randn(shape.rows, shape.cols) * 1e-5
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    rtol = 1e-5
    atol = 1e-8
    if np.array_equal(NumCpp.MethodsDouble.isclose(cArray1, cArray2, rtol, atol).getNumpyArray(), np.isclose(data1, data2, rtol=rtol, atol=atol)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing isnan scalar', 'cyan'))
    value = np.random.randn(1).item() * 100 + 1000
    if NumCpp.MethodsDouble.isnanScalar(value) == np.isnan(value):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing isnan array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randn(shape.rows, shape.cols) * 100 + 1000
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.isnanArray(cArray), np.isnan(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing ldexp scalar', 'cyan'))
    value1 = np.random.randn(1).item() * 100
    value2 = np.random.randint(1, 20, [1,]).item()
    if np.round(NumCpp.MethodsDouble.ldexpScalar(value1, value2), 10) == np.round(np.ldexp(value1, value2), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing ldexp array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArrayInt8(shape)
    data1 = np.random.randn(shape.rows, shape.cols) * 100
    data2 = np.random.randint(1, 20, [shape.rows, shape.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(np.round(NumCpp.MethodsDouble.ldexpArray(cArray1, cArray2), 10), np.round(np.ldexp(data1, data2), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing left_shift', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    bitsToShift = np.random.randint(1, 32, [1, ]).item()
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArrayInt(shape)
    data = np.random.randint(1, np.iinfo(np.uint32).max, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.left_shift(cArray, bitsToShift).getNumpyArray(), np.left_shift(data, bitsToShift)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing less', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    data2 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.less(cArray1, cArray2).getNumpyArray(), np.less(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing less_equal array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    data2 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.less_equal(cArray1, cArray2).getNumpyArray(), np.less_equal(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing load', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    tempDir = r'C:\Temp'
    if not os.path.exists(tempDir):
        os.mkdir(tempDir)
    tempFile = os.path.join(tempDir, 'NdArrayDump.bin')
    NumCpp.MethodsDouble.dump(cArray, tempFile)
    data2 = NumCpp.MethodsDouble.load(tempFile).reshape(shape)
    if np.array_equal(data, data2):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))
    os.remove(tempFile)

    print(colored('Testing linspace: include endPoint True', 'cyan'))
    start = np.random.randint(1, 10, [1, ]).item()
    end = np.random.randint(start + 10, 100, [1, ]).item()
    numPoints = np.random.randint(1, 100, [1, ]).item()
    if np.array_equal(np.round(NumCpp.MethodsDouble.linspace(start, end, numPoints, True).getNumpyArray().flatten(), 10),
                      np.round(np.linspace(start, end, numPoints, endpoint=True), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing linspace: include endPoint False', 'cyan'))
    start = np.random.randint(1, 10, [1, ]).item()
    end = np.random.randint(start + 10, 100, [1, ]).item()
    numPoints = np.random.randint(1, 100, [1, ]).item()
    if np.array_equal(np.round(NumCpp.MethodsDouble.linspace(start, end, numPoints, False).getNumpyArray().flatten(), 10),
                      np.round(np.linspace(start, end, numPoints, endpoint=False), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing log scalar', 'cyan'))
    value = np.random.randn(1).item() * 100 + 1000
    if np.round(NumCpp.MethodsDouble.logScalar(value), 10) == np.round(np.log(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing log array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randn(shape.rows, shape.cols) * 100 + 1000
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.logArray(cArray), 10), np.round(np.log(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing log10 scalar', 'cyan'))
    value = np.random.randn(1).item() * 100 + 1000
    if np.round(NumCpp.MethodsDouble.log10Scalar(value), 10) == np.round(np.log10(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing log10 array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randn(shape.rows, shape.cols) * 100 + 1000
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.log10Array(cArray), 10), np.round(np.log10(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing log1p scalar', 'cyan'))
    value = np.random.randn(1).item() * 100 + 1000
    if np.round(NumCpp.MethodsDouble.log1pScalar(value), 10) == np.round(np.log1p(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing log1p array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randn(shape.rows, shape.cols) * 100 + 1000
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.log1pArray(cArray), 10), np.round(np.log1p(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing log2 scalar', 'cyan'))
    value = np.random.randn(1).item() * 100 + 1000
    if np.round(NumCpp.MethodsDouble.log2Scalar(value), 10) == np.round(np.log2(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing log2 array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randn(shape.rows, shape.cols) * 100 + 1000
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.log2Array(cArray), 10), np.round(np.log2(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing logical_and', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randint(0, 20, [shape.rows, shape.cols])
    data2 = np.random.randint(0, 20, [shape.rows, shape.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.logical_and(cArray1, cArray2).getNumpyArray(), np.logical_and(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing logical_not', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 20, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.logical_not(cArray).getNumpyArray(), np.logical_not(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing logical_or', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randint(0, 20, [shape.rows, shape.cols])
    data2 = np.random.randint(0, 20, [shape.rows, shape.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.logical_or(cArray1, cArray2).getNumpyArray(), np.logical_or(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing logical_xor', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randint(0, 20, [shape.rows, shape.cols])
    data2 = np.random.randint(0, 20, [shape.rows, shape.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.logical_xor(cArray1, cArray2).getNumpyArray(), np.logical_xor(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing matmult', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape1 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    shape2 = NumCpp.Shape(shapeInput[1].item(), shapeInput[0].item())
    cArray1 = NumCpp.NdArray(shape1)
    cArray2 = NumCpp.NdArray(shape2)
    data1 = np.random.randint(0, 20, [shape1.rows, shape1.cols])
    data2 = np.random.randint(0, 20, [shape2.rows, shape2.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.matmul(cArray1, cArray2).getNumpyArray(), np.matmul(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing max: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if NumCpp.MethodsDouble.max(cArray, NumCpp.Axis.NONE).item() == np.max(data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing max: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.max(cArray, NumCpp.Axis.ROW).getNumpyArray().astype(np.uint32).flatten(), np.max(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing max: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.max(cArray, NumCpp.Axis.COL).getNumpyArray().astype(np.uint32).flatten(), np.max(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing maximum', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randint(0, 100, [shape.rows, shape.cols])
    data2 = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.maximum(cArray1, cArray2).getNumpyArray(), np.maximum(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing mean: axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if NumCpp.MethodsDouble.mean(cArray, NumCpp.Axis.NONE).getNumpyArray().flatten().item() == np.mean(data, axis=None).item():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing mean: axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.mean(cArray, NumCpp.Axis.ROW).getNumpyArray().flatten(), np.mean(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing mean: axis = Col', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.mean(cArray, NumCpp.Axis.COL).getNumpyArray().flatten(), np.mean(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing median: axis = None', 'cyan'))
    isEven = True
    while isEven:
        shapeInput = np.random.randint(20, 100, [2, ])
        isEven = shapeInput.prod().item() % 2 == 0
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if NumCpp.MethodsDouble.median(cArray, NumCpp.Axis.NONE).getNumpyArray().flatten().item() == np.median(data, axis=None).item():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing median: axis = Row', 'cyan'))
    isEven = True
    while isEven:
        shapeInput = np.random.randint(20, 100, [2, ])
        isEven = shapeInput.prod().item() % 2 == 0
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.median(cArray, NumCpp.Axis.ROW).getNumpyArray().flatten(), np.median(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing median: axis = Col', 'cyan'))
    isEven = True
    while isEven:
        shapeInput = np.random.randint(20, 100, [2, ])
        isEven = shapeInput.prod().item() % 2 == 0
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.median(cArray, NumCpp.Axis.COL).getNumpyArray().flatten(), np.median(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing min: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if NumCpp.MethodsDouble.min(cArray, NumCpp.Axis.NONE).item() == np.min(data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing min: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.min(cArray, NumCpp.Axis.ROW).getNumpyArray().astype(np.uint32).flatten(), np.min(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing min: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.min(cArray, NumCpp.Axis.COL).getNumpyArray().astype(np.uint32).flatten(), np.min(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing minimum', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randint(0, 100, [shape.rows, shape.cols])
    data2 = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.minimum(cArray1, cArray2).getNumpyArray(), np.minimum(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing mod', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArrayInt(shape)
    cArray2 = NumCpp.NdArrayInt(shape)
    data1 = np.random.randint(1, 100, [shape.rows, shape.cols])
    data2 = np.random.randint(1, 100, [shape.rows, shape.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.mod(cArray1, cArray2).getNumpyArray(), np.mod(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing multiply', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randint(0, 100, [shape.rows, shape.cols])
    data2 = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.multiply(cArray1, cArray2).getNumpyArray(), np.multiply(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanargmax: Axis = None', 'cyan'))
    shapeInput = np.random.randint(10, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if NumCpp.MethodsDouble.nanargmax(cArray, NumCpp.Axis.NONE).item() == np.nanargmax(data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanargmax: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(10, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.nanargmax(cArray, NumCpp.Axis.ROW).getNumpyArray().flatten(), np.nanargmax(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanargmax: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(10, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.nanargmax(cArray, NumCpp.Axis.COL).getNumpyArray().flatten(), np.nanargmax(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanargmin: Axis = None', 'cyan'))
    shapeInput = np.random.randint(10, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if NumCpp.MethodsDouble.nanargmin(cArray, NumCpp.Axis.NONE).item() == np.nanargmin(data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanargmin: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(10, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.nanargmin(cArray, NumCpp.Axis.ROW).getNumpyArray().flatten(), np.nanargmin(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanargmin: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(10, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.nanargmin(cArray, NumCpp.Axis.COL).getNumpyArray().flatten(), np.nanargmin(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nancumprod: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 5, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 4, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.nancumprod(cArray, NumCpp.Axis.NONE).getNumpyArray().flatten(), np.nancumprod(data, axis=None)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nancumprod: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 5, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 4, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.nancumprod(cArray, NumCpp.Axis.ROW).getNumpyArray(), np.nancumprod(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nancumprod: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(1, 5, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 4, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.nancumprod(cArray, NumCpp.Axis.COL).getNumpyArray(), np.nancumprod(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nancumsum: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.nancumsum(cArray, NumCpp.Axis.NONE).getNumpyArray().flatten(), np.nancumsum(data, axis=None)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nancumsum: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.nancumsum(cArray, NumCpp.Axis.ROW).getNumpyArray(), np.nancumsum(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nancumsum: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(1, 50, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.nancumsum(cArray, NumCpp.Axis.COL).getNumpyArray(), np.nancumsum(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanmax: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if NumCpp.MethodsDouble.nanmax(cArray, NumCpp.Axis.NONE).item() == np.nanmax(data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanmax: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.nanmax(cArray, NumCpp.Axis.ROW).getNumpyArray().flatten(),
                      np.nanmax(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanmax: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.nanmax(cArray, NumCpp.Axis.COL).getNumpyArray().flatten(),
                      np.nanmax(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanmean: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10, ])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if NumCpp.MethodsDouble.nanmean(cArray, NumCpp.Axis.NONE).item() == np.nanmean(data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanmean: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10, ])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.nanmean(cArray, NumCpp.Axis.ROW).getNumpyArray().flatten(),
                      np.nanmean(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanmean: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10, ])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.nanmean(cArray, NumCpp.Axis.COL).getNumpyArray().flatten(),
                      np.nanmean(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanmedian: axis = None', 'cyan'))
    isEven = True
    while isEven:
        shapeInput = np.random.randint(20, 100, [2, ])
        isEven = shapeInput.prod().item() % 2 == 0
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if NumCpp.MethodsDouble.nanmedian(cArray, NumCpp.Axis.NONE).getNumpyArray().flatten().item() == np.nanmedian(data, axis=None).item():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))
    #
    # print(colored('Testing nanmedian: axis = Row', 'cyan'))
    # isEven = True
    # while isEven:
    #     shapeInput = np.random.randint(20, 100, [2, ])
    #     isEven = shapeInput[0].item() % 2 == 0
    # shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    # cArray = NumCpp.NdArray(shape)
    # data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    # data = data.flatten()
    # data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    # data = data.reshape(shapeInput)
    # cArray.setArray(data)
    # if np.array_equal(NumCpp.MethodsDouble.nanmedian(cArray, NumCpp.Axis.ROW).getNumpyArray().flatten(), np.nanmedian(data, axis=0)):
    #     print(colored('\tPASS', 'green'))
    # else:
    #     print(colored('\tFAIL', 'red'))

    # print(colored('Testing nanmedian: axis = Col', 'cyan'))
    # isEven = True
    # while isEven:
    #     shapeInput = np.random.randint(20, 100, [2, ])
    #     isEven = shapeInput[1].item() % 2 == 0
    # shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    # cArray = NumCpp.NdArray(shape)
    # data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    # data = data.flatten()
    # data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    # data = data.reshape(shapeInput)
    # cArray.setArray(data)
    # if np.array_equal(NumCpp.MethodsDouble.nanmedian(cArray, NumCpp.Axis.COL).getNumpyArray().flatten(), np.nanmedian(data, axis=1)):
    #     print(colored('\tPASS', 'green'))
    # else:
    #     print(colored('\tFAIL', 'red'))

    print(colored('Testing nanmin: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if NumCpp.MethodsDouble.nanmin(cArray, NumCpp.Axis.NONE).item() == np.nanmin(data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanmin: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.nanmin(cArray, NumCpp.Axis.ROW).getNumpyArray().flatten(),
                      np.nanmin(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanmin: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.nanmin(cArray, NumCpp.Axis.COL).getNumpyArray().flatten(),
                      np.nanmin(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanpercentile: Axis = None, method = lower', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if NumCpp.MethodsDouble.nanpercentile(cArray, percentile, NumCpp.Axis.NONE, 'lower').item() == np.nanpercentile(data, percentile, axis=None,
                                                                                            interpolation='lower'):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanpercentile: Axis = None, method = higher', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if NumCpp.MethodsDouble.nanpercentile(cArray, percentile, NumCpp.Axis.NONE, 'higher').item() == np.nanpercentile(data, percentile,
                                                                                             axis=None,
                                                                                             interpolation='higher'):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanpercentile: Axis = None, method = nearest', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if NumCpp.MethodsDouble.nanpercentile(cArray, percentile, NumCpp.Axis.NONE, 'nearest').item() == np.nanpercentile(data, percentile,
                                                                                              axis=None,
                                                                                              interpolation='nearest'):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanpercentile: Axis = None, method = midpoint', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if NumCpp.MethodsDouble.nanpercentile(cArray, percentile, NumCpp.Axis.NONE, 'midpoint').item() == np.nanpercentile(data, percentile,
                                                                                               axis=None,
                                                                                               interpolation='midpoint'):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanpercentile: Axis = None, method = linear', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if NumCpp.MethodsDouble.nanpercentile(cArray, percentile, NumCpp.Axis.NONE, 'linear').item() == np.nanpercentile(data, percentile,
                                                                                             axis=None,
                                                                                             interpolation='linear'):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanpercentile: Axis = Row, method = lower', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if np.array_equal(NumCpp.MethodsDouble.nanpercentile(cArray, percentile, NumCpp.Axis.ROW, 'lower').getNumpyArray().flatten(),
                      np.nanpercentile(data, percentile, axis=0, interpolation='lower')):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanpercentile: Axis = Row, method = higher', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if np.array_equal(NumCpp.MethodsDouble.nanpercentile(cArray, percentile, NumCpp.Axis.ROW, 'higher').getNumpyArray().flatten(),
                      np.nanpercentile(data, percentile, axis=0, interpolation='higher')):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanpercentile: Axis = Row, method = nearest', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if np.array_equal(NumCpp.MethodsDouble.nanpercentile(cArray, percentile, NumCpp.Axis.ROW, 'nearest').getNumpyArray().flatten(),
                      np.nanpercentile(data, percentile, axis=0, interpolation='nearest')):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanpercentile: Axis = Row, method = midpoint', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if np.array_equal(
            np.round(NumCpp.MethodsDouble.nanpercentile(cArray, percentile, NumCpp.Axis.ROW, 'midpoint').getNumpyArray().flatten(), 10),
            np.round(np.nanpercentile(data, percentile, axis=0, interpolation='midpoint'), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanpercentile: Axis = Row, method = linear', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if np.array_equal(
            np.round(NumCpp.MethodsDouble.nanpercentile(cArray, percentile, NumCpp.Axis.ROW, 'linear').getNumpyArray().flatten(), 10),
            np.round(np.nanpercentile(data, percentile, axis=0, interpolation='linear'), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanpercentile: Axis = Col, method = lower', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if np.array_equal(NumCpp.MethodsDouble.nanpercentile(cArray, percentile, NumCpp.Axis.COL, 'lower').getNumpyArray().flatten(),
                      np.nanpercentile(data, percentile, axis=1, interpolation='lower')):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanpercentile: Axis = Col, method = higher', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if np.array_equal(NumCpp.MethodsDouble.nanpercentile(cArray, percentile, NumCpp.Axis.COL, 'higher').getNumpyArray().flatten(),
                      np.nanpercentile(data, percentile, axis=1, interpolation='higher')):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanpercentile: Axis = Col, method = nearest', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if np.array_equal(NumCpp.MethodsDouble.nanpercentile(cArray, percentile, NumCpp.Axis.COL, 'nearest').getNumpyArray().flatten(),
                      np.nanpercentile(data, percentile, axis=1, interpolation='nearest')):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanpercentile: Axis = Col, method = midpoint', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if np.array_equal(
            np.round(NumCpp.MethodsDouble.nanpercentile(cArray, percentile, NumCpp.Axis.COL, 'midpoint').getNumpyArray().flatten(), 10),
            np.round(np.nanpercentile(data, percentile, axis=1, interpolation='midpoint'), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanpercentile: Axis = Col, method = linear', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if np.array_equal(
            np.round(NumCpp.MethodsDouble.nanpercentile(cArray, percentile, NumCpp.Axis.COL, 'linear').getNumpyArray().flatten(), 10),
            np.round(np.nanpercentile(data, percentile, axis=1, interpolation='linear'), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanprod: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 10, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 15, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if NumCpp.MethodsDouble.nanprod(cArray, NumCpp.Axis.NONE).item() == np.nanprod(data, axis=None):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanprod: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 10, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 15, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.nanprod(cArray, NumCpp.Axis.ROW).getNumpyArray().flatten(), np.nanprod(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanprod: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(1, 10, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 15, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.nanprod(cArray, NumCpp.Axis.COL).getNumpyArray().flatten(), np.nanprod(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nans square', 'cyan'))
    shapeInput = np.random.randint(1, 100, [1, ]).item()
    cArray = NumCpp.MethodsDouble.nansSquare(shapeInput)
    if (cArray.shape[0] == shapeInput and cArray.shape[1] == shapeInput and
            cArray.size == shapeInput ** 2 and np.all(np.isnan(cArray))):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nans rectangle', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    cArray = NumCpp.MethodsDouble.nansRowCol(shapeInput[0].item(), shapeInput[1].item())
    if (cArray.shape[0] == shapeInput[0] and cArray.shape[1] == shapeInput[1] and
            cArray.size == shapeInput.prod() and np.all(np.isnan(cArray))):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nans Shape', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.MethodsDouble.nansShape(shape)
    if (cArray.shape[0] == shape.rows and cArray.shape[1] == shape.cols and
            cArray.size == shapeInput.prod() and np.all(np.isnan(cArray))):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanstd: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.round(NumCpp.MethodsDouble.nanstd(cArray, NumCpp.Axis.NONE).item(), 10) == np.round(np.nanstd(data), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanstd: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.nanstd(cArray, NumCpp.Axis.ROW).getNumpyArray().flatten(), 10),
                      np.round(np.nanstd(data, axis=0), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanstd: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.nanstd(cArray, NumCpp.Axis.COL).getNumpyArray().flatten(), 10),
                      np.round(np.nanstd(data, axis=1), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nansum: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if NumCpp.MethodsDouble.nansum(cArray, NumCpp.Axis.NONE).item() == np.nansum(data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nansum: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.nansum(cArray, NumCpp.Axis.ROW).getNumpyArray().flatten(), np.nansum(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nansum: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.nansum(cArray, NumCpp.Axis.COL).getNumpyArray().flatten(), np.nansum(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanvar: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.round(NumCpp.MethodsDouble.nanvar(cArray, NumCpp.Axis.NONE).item(), 9) == np.round(np.nanvar(data), 9):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanvar: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.nanvar(cArray, NumCpp.Axis.ROW).getNumpyArray().flatten(), 9),
                      np.round(np.nanvar(data, axis=0), 9)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nanvar: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    data = data.flatten()
    data[np.random.randint(0, shape.size(), [shape.size() // 10,])] = np.nan
    data = data.reshape(shapeInput)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.nanvar(cArray, NumCpp.Axis.COL).getNumpyArray().flatten(), 9),
                      np.round(np.nanvar(data, axis=1), 9)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nbytes', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(-100, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    if NumCpp.MethodsDouble.nbytes(cArray) == data.size * 8:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing newbyteorder scalar', 'cyan'))
    value = np.random.randint(1, 100, [1,]).item()
    if NumCpp.MethodsDouble.newbyteorderScalar(value, NumCpp.Endian.BIG) == np.asarray([value]).newbyteorder().item():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing newbyteorder array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArrayInt(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.newbyteorderArray(cArray, NumCpp.Endian.BIG), data.newbyteorder()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing negative array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(-100, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.negative(cArray).getNumpyArray(), 10), np.round(np.negative(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nonzero', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.nonzero(cArray).getNumpyArray().flatten(), data.flatten().nonzero()[0]):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing norm: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if NumCpp.MethodsDouble.norm(cArray, NumCpp.Axis.NONE).flatten() == np.linalg.norm(data.flatten()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing norm: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    norms = NumCpp.MethodsDouble.norm(cArray, NumCpp.Axis.ROW).getNumpyArray().flatten()
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
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    norms = NumCpp.MethodsDouble.norm(cArray, NumCpp.Axis.COL).getNumpyArray().flatten()
    allPass = True
    for idx, row in enumerate(data):
        if norms[idx] != np.linalg.norm(row):
            allPass = False
            break
    if allPass:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing not_equal', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    data2 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.not_equal(cArray1, cArray2).getNumpyArray(), np.not_equal(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing ones square', 'cyan'))
    shapeInput = np.random.randint(1, 100, [1, ]).item()
    cArray = NumCpp.MethodsDouble.onesSquare(shapeInput)
    if (cArray.shape[0] == shapeInput and cArray.shape[1] == shapeInput and
            cArray.size == shapeInput ** 2 and np.all(cArray == 1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing ones rectangle', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    cArray = NumCpp.MethodsDouble.onesRowCol(shapeInput[0].item(), shapeInput[1].item())
    if (cArray.shape[0] == shapeInput[0] and cArray.shape[1] == shapeInput[1] and
            cArray.size == shapeInput.prod() and np.all(cArray == 1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing ones Shape', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.MethodsDouble.onesShape(shape)
    if (cArray.shape[0] == shape.rows and cArray.shape[1] == shape.cols and
            cArray.size == shapeInput.prod() and np.all(cArray == 1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing ones_like', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.MethodsDouble.ones_like(cArray1)
    if (cArray2.shape().rows == shape.rows and cArray2.shape().cols == shape.cols and
            cArray2.size() == shapeInput.prod() and np.all(cArray2.getNumpyArray() == 1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing pad', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    padWidth = np.random.randint(1, 10, [1, ]).item()
    padValue = np.random.randint(1, 100, [1, ]).item()
    data = np.random.randint(1, 100, [shape.rows, shape.cols])
    cArray = NumCpp.NdArray(shape)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.pad(cArray, padWidth, padValue).getNumpyArray(), np.pad(data, padWidth, mode='constant', constant_values=padValue)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing partition: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    kthElement = np.random.randint(0, shapeInput.prod(), [1,], dtype=np.uint32).item()
    partitionedArray = NumCpp.MethodsDouble.partition(cArray, kthElement, NumCpp.Axis.NONE).getNumpyArray().flatten()
    if (np.all(partitionedArray[:kthElement] <= partitionedArray[kthElement]) and
        np.all(partitionedArray[kthElement:] >= partitionedArray[kthElement])):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing partition: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    kthElement = np.random.randint(0, shapeInput[0], [1,], dtype=np.uint32).item()
    partitionedArray = NumCpp.MethodsDouble.partition(cArray, kthElement, NumCpp.Axis.ROW).getNumpyArray().transpose()
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
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    kthElement = np.random.randint(0, shapeInput[1], [1,], dtype=np.uint32).item()
    partitionedArray = NumCpp.MethodsDouble.partition(cArray, kthElement, NumCpp.Axis.COL).getNumpyArray()
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

    print(colored('Testing percentile: Axis = None, method = lower', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if NumCpp.MethodsDouble.percentile(cArray, percentile, NumCpp.Axis.NONE, 'lower').item() == np.percentile(data, percentile, axis=None, interpolation='lower'):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing percentile: Axis = None, method = higher', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if NumCpp.MethodsDouble.percentile(cArray, percentile, NumCpp.Axis.NONE, 'higher').item() == np.percentile(data, percentile, axis=None, interpolation='higher'):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing percentile: Axis = None, method = nearest', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if NumCpp.MethodsDouble.percentile(cArray, percentile, NumCpp.Axis.NONE, 'nearest').item() == np.percentile(data, percentile, axis=None, interpolation='nearest'):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing percentile: Axis = None, method = midpoint', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if NumCpp.MethodsDouble.percentile(cArray, percentile, NumCpp.Axis.NONE, 'midpoint').item() == np.percentile(data, percentile, axis=None, interpolation='midpoint'):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing percentile: Axis = None, method = linear', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if NumCpp.MethodsDouble.percentile(cArray, percentile, NumCpp.Axis.NONE, 'linear').item() == np.percentile(data, percentile, axis=None, interpolation='linear'):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing percentile: Axis = Row, method = lower', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if np.array_equal(NumCpp.MethodsDouble.percentile(cArray, percentile, NumCpp.Axis.ROW, 'lower').getNumpyArray().flatten(),
                      np.percentile(data, percentile, axis=0, interpolation='lower')):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing percentile: Axis = Row, method = higher', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if np.array_equal(NumCpp.MethodsDouble.percentile(cArray, percentile, NumCpp.Axis.ROW, 'higher').getNumpyArray().flatten(),
                      np.percentile(data, percentile, axis=0, interpolation='higher')):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing percentile: Axis = Row, method = nearest', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if np.array_equal(NumCpp.MethodsDouble.percentile(cArray, percentile, NumCpp.Axis.ROW, 'nearest').getNumpyArray().flatten(),
                      np.percentile(data, percentile, axis=0, interpolation='nearest')):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing percentile: Axis = Row, method = midpoint', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if np.array_equal(np.round(NumCpp.MethodsDouble.percentile(cArray, percentile, NumCpp.Axis.ROW, 'midpoint').getNumpyArray().flatten(), 10),
                      np.round(np.percentile(data, percentile, axis=0, interpolation='midpoint'), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing percentile: Axis = Row, method = linear', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if np.array_equal(np.round(NumCpp.MethodsDouble.percentile(cArray, percentile, NumCpp.Axis.ROW, 'linear').getNumpyArray().flatten(), 10),
                      np.round(np.percentile(data, percentile, axis=0, interpolation='linear'), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing percentile: Axis = Col, method = lower', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if np.array_equal(NumCpp.MethodsDouble.percentile(cArray, percentile, NumCpp.Axis.COL, 'lower').getNumpyArray().flatten(),
                      np.percentile(data, percentile, axis=1, interpolation='lower')):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing percentile: Axis = Col, method = higher', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if np.array_equal(NumCpp.MethodsDouble.percentile(cArray, percentile, NumCpp.Axis.COL, 'higher').getNumpyArray().flatten(),
                      np.percentile(data, percentile, axis=1, interpolation='higher')):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing percentile: Axis = Col, method = nearest', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if np.array_equal(NumCpp.MethodsDouble.percentile(cArray, percentile, NumCpp.Axis.COL, 'nearest').getNumpyArray().flatten(),
                      np.percentile(data, percentile, axis=1, interpolation='nearest')):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing percentile: Axis = Col, method = midpoint', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if np.array_equal(np.round(NumCpp.MethodsDouble.percentile(cArray, percentile, NumCpp.Axis.COL, 'midpoint').getNumpyArray().flatten(), 10),
                      np.round(np.percentile(data, percentile, axis=1, interpolation='midpoint'), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing percentile: Axis = Col, method = linear', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    percentile = np.random.rand(1).item() * 100
    if np.array_equal(np.round(NumCpp.MethodsDouble.percentile(cArray, percentile, NumCpp.Axis.COL, 'linear').getNumpyArray().flatten(), 10),
                      np.round(np.percentile(data, percentile, axis=1, interpolation='linear'), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing power array scalar', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    exponent = np.random.randint(0, 5, [1, ]).item()
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.powerArrayScalar(cArray, exponent), 10), np.round(np.power(data, exponent), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing power array array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    cExponents = NumCpp.NdArrayInt8(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    exponents = np.random.randint(0, 5, [shape.rows, shape.cols]).astype(np.uint8)
    cArray.setArray(data)
    cExponents.setArray(exponents)
    if np.array_equal(np.round(NumCpp.MethodsDouble.powerArrayArray(cArray, cExponents), 10), np.round(np.power(data, exponents), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing prod: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 10, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 15, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    if NumCpp.MethodsDouble.prod(cArray, NumCpp.Axis.NONE).item() == data.prod():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing prod: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 10, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 15, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.prod(cArray, NumCpp.Axis.ROW).getNumpyArray().flatten(), data.prod(axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing prod: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(1, 10, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 15, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.prod(cArray, NumCpp.Axis.COL).getNumpyArray().flatten(), data.prod(axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing ptp: Axis = None', 'cyan'))
    shapeInput = np.random.randint(1, 10, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 15, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if NumCpp.MethodsDouble.ptp(cArray, NumCpp.Axis.NONE).getNumpyArray().astype(np.uint32).item() == data.ptp():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing ptp: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(1, 10, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 15, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.ptp(cArray, NumCpp.Axis.ROW).getNumpyArray().flatten().astype(np.uint32), data.ptp(axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing ptp: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(1, 10, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 15, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.ptp(cArray, NumCpp.Axis.COL).getNumpyArray().flatten().astype(np.uint32), data.ptp(axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing put', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 50, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    numIndices = np.random.randint(0, shape.size())
    indices = np.asarray(range(numIndices))
    values = np.random.randint(1, 500, [numIndices, ])
    cIndices = NumCpp.NdArrayInt(1, numIndices)
    cValues = NumCpp.NdArray(1, numIndices)
    cIndices.setArray(indices)
    cValues.setArray(values)
    NumCpp.MethodsDouble.put(cArray, cIndices, cValues)
    data.put(indices, values)
    if np.array_equal(cArray.getNumpyArray(), data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing rad2deg scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item()) * 2 * np.pi
    if np.round(NumCpp.MethodsDouble.rad2degScalar(value), 10) == np.round(np.rad2deg(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing rad2deg array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols) * 2 * np.pi
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.rad2degArray(cArray), 9), np.round(np.rad2deg(data), 9)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing reciprocal array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols) * 100
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.reciprocal(cArray).getNumpyArray(), 10), np.round(np.reciprocal(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    # numpy and cmath remainders are calculated differently, so convert for testing purposes
    print(colored('Testing remainder scalar', 'cyan'))
    values = np.random.rand(2) * 100
    values = np.sort(values)
    res = NumCpp.MethodsDouble.remainderScalar(values[1].item(), values[0].item())
    if res < 0:
        res += values[0].item()
    if np.round(res, 10) == np.round(np.remainder(values[1], values[0]), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    # numpy and cmath remainders are calculated differently, so convert for testing purposes
    print(colored('Testing remainder array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    data1 = np.random.rand(shape.rows, shape.cols) * 100 + 10
    data2 = data1 - np.random.rand(shape.rows, shape.cols) * 10
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    res = NumCpp.MethodsDouble.remainderArray(cArray1, cArray2)
    res[res < 0] = res[res < 0] + data2[res < 0]
    if np.array_equal(np.round(res, 10), np.round(np.remainder(data1, data2), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing reshape', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    newShape = NumCpp.Shape(shapeInput[1].item(), shapeInput[0].item())
    NumCpp.MethodsDouble.reshape(cArray, newShape)
    if np.array_equal(cArray.getNumpyArray(), data.reshape(shapeInput[::-1])):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing resizeFast', 'cyan'))
    shapeInput1 = np.random.randint(1, 100, [2, ])
    shapeInput2 = np.random.randint(1, 100, [2, ])
    shape1 = NumCpp.Shape(shapeInput1[0].item(), shapeInput1[1].item())
    shape2 = NumCpp.Shape(shapeInput2[0].item(), shapeInput2[1].item())
    cArray = NumCpp.NdArray(shape1)
    data = np.random.randint(1, 100, [shape1.rows, shape1.cols], dtype=np.uint32)
    cArray.setArray(data)
    NumCpp.MethodsDouble.resizeFast(cArray, shape2)
    if np.all(cArray.getNumpyArray() == 0) and cArray.shape().rows == shape2.rows and cArray.shape().cols == shape2.cols:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing resizeSlow', 'cyan'))
    shapeInput1 = np.random.randint(1, 100, [2, ])
    shapeInput2 = np.random.randint(1, 100, [2, ])
    shape1 = NumCpp.Shape(shapeInput1[0].item(), shapeInput1[1].item())
    shape2 = NumCpp.Shape(shapeInput2[0].item(), shapeInput2[1].item())
    cArray = NumCpp.NdArray(shape1)
    data = np.random.randint(1, 100, [shape1.rows, shape1.cols], dtype=np.uint32)
    cArray.setArray(data)
    NumCpp.MethodsDouble.resizeSlow(cArray, shape2)
    if cArray.shape().rows == shape2.rows and cArray.shape().cols == shape2.cols and not np.all(cArray.getNumpyArray() == 0):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing right_shift', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    bitsToShift = np.random.randint(1, 32, [1, ]).item()
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArrayInt(shape)
    data = np.random.randint(1, np.iinfo(np.uint32).max, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.right_shift(cArray, bitsToShift).getNumpyArray(), np.right_shift(data, bitsToShift)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing rint scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item()) * 2 * np.pi
    if NumCpp.MethodsDouble.rintScalar(value) == np.rint(value):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing rint array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols) * 2 * np.pi
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.rintArray(cArray), np.rint(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing roll: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    amount = np.random.randint(0, data.size, [1,]).item()
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.roll(cArray, amount, NumCpp.Axis.NONE).getNumpyArray(), np.roll(data, amount, axis=None)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing roll: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    amount = np.random.randint(0, shape.cols, [1,]).item()
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.roll(cArray, amount, NumCpp.Axis.ROW).getNumpyArray(), np.roll(data, amount, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing roll: Axis = Col', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    amount = np.random.randint(0, shape.rows, [1,]).item()
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.roll(cArray, amount, NumCpp.Axis.COL).getNumpyArray(), np.roll(data, amount, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing rot90', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    amount = np.random.randint(1, 4, [1,]).item()
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.rot90(cArray, amount).getNumpyArray(), np.rot90(data, amount)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing round scalar', 'cyan'))
    value = np.abs(np.random.rand(1).item()) * 2 * np.pi
    if NumCpp.MethodsDouble.roundScalar(value, 10) == np.round(value, 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing round array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols) * 2 * np.pi
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.roundArray(cArray, 10), np.round(data, 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing row_stack', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape1 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    shape2 = NumCpp.Shape(shapeInput[0].item() + np.random.randint(1, 10, [1,]).item(), shapeInput[1].item())
    shape3 = NumCpp.Shape(shapeInput[0].item() + np.random.randint(1, 10, [1,]).item(), shapeInput[1].item())
    shape4 = NumCpp.Shape(shapeInput[0].item() + np.random.randint(1, 10, [1,]).item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape1)
    cArray2 = NumCpp.NdArray(shape2)
    cArray3 = NumCpp.NdArray(shape3)
    cArray4 = NumCpp.NdArray(shape4)
    data1 = np.random.randint(1, 100, [shape1.rows, shape1.cols])
    data2 = np.random.randint(1, 100, [shape2.rows, shape2.cols])
    data3 = np.random.randint(1, 100, [shape3.rows, shape3.cols])
    data4 = np.random.randint(1, 100, [shape4.rows, shape4.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    cArray3.setArray(data3)
    cArray4.setArray(data4)
    if np.array_equal(NumCpp.MethodsDouble.row_stack(cArray1, cArray2, cArray3, cArray4),
                      np.row_stack([data1, data2, data3, data4])):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing setdiff1d', 'cyan'))
    shapeInput = np.random.randint(1, 10, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArrayInt(shape)
    cArray2 = NumCpp.NdArrayInt(shape)
    data1 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    data2 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.setdiff1d(cArray1, cArray2).getNumpyArray().flatten(), np.setdiff1d(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing shape array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    if cArray.shape().rows == shape.rows and cArray.shape().cols == shape.cols:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing sign scalar', 'cyan'))
    value = np.random.randn(1).item() * 100
    if NumCpp.MethodsDouble.signScalar(value) == np.sign(value):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing sign array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randn(shape.rows, shape.cols) * 100
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.signArray(cArray), np.sign(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing signbit scalar', 'cyan'))
    value = np.random.randn(1).item() * 100
    if NumCpp.MethodsDouble.signbitScalar(value) == np.signbit(value):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing signbit array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randn(shape.rows, shape.cols) * 100
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.signbitArray(cArray), np.signbit(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing sin scalar', 'cyan'))
    value = np.random.randn(1).item()
    if np.round(NumCpp.MethodsDouble.sinScalar(value), 10) == np.round(np.sin(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing sin array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randn(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.sinArray(cArray), 10), np.round(np.sin(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing sinc scalar', 'cyan'))
    value = np.random.randn(1).item()
    if np.round(NumCpp.MethodsDouble.sincScalar(value), 10) == np.round(np.sinc(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing sinc array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randn(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.sincArray(cArray), 10), np.round(np.sinc(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing sinh scalar', 'cyan'))
    value = np.random.randn(1).item()
    if np.round(NumCpp.MethodsDouble.sinhScalar(value), 10) == np.round(np.sinh(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing sinh array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randn(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.sinhArray(cArray), 10), np.round(np.sinh(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing size', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    if cArray.size() == shapeInput.prod().item():
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing sort: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    d = data.flatten()
    d.sort()
    if np.array_equal(NumCpp.MethodsDouble.sort(cArray, NumCpp.Axis.NONE).getNumpyArray().flatten(), d):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing sort: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols], dtype=np.uint32)
    cArray.setArray(data)
    pSorted = np.sort(data, axis=0)
    cSorted = NumCpp.MethodsDouble.sort(cArray, NumCpp.Axis.ROW).getNumpyArray().astype(np.uint32)
    if np.array_equal(cSorted, pSorted):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing sort: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    pSorted = np.sort(data, axis=1)
    cSorted = NumCpp.MethodsDouble.sort(cArray, NumCpp.Axis.COL).getNumpyArray().astype(np.uint32)
    if np.array_equal(cSorted, pSorted):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing sqrt scalar', 'cyan'))
    value = np.random.randint(1, 100, [1,]).item()
    if np.round(NumCpp.MethodsDouble.sqrtScalar(value), 10) == np.round(np.sqrt(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing sqrt array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.sqrtArray(cArray), 10), np.round(np.sqrt(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing square scalar', 'cyan'))
    value = np.random.randint(1, 100, [1, ]).item()
    if np.round(NumCpp.MethodsDouble.squareScalar(value), 10) == np.round(np.square(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing square array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.squareArray(cArray), 10), np.round(np.square(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing stack: Axis::ROW', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    cArray3 = NumCpp.NdArray(shape)
    cArray4 = NumCpp.NdArray(shape)
    data1 = np.random.randint(1, 100, [shape.rows, shape.cols])
    data2 = np.random.randint(1, 100, [shape.rows, shape.cols])
    data3 = np.random.randint(1, 100, [shape.rows, shape.cols])
    data4 = np.random.randint(1, 100, [shape.rows, shape.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    cArray3.setArray(data3)
    cArray4.setArray(data4)
    if np.array_equal(NumCpp.MethodsDouble.stack(cArray1, cArray2, cArray3, cArray4, NumCpp.Axis.ROW),
                      np.vstack([data1, data2, data3, data4])):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing stack: Axis::COL', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape)
    cArray2 = NumCpp.NdArray(shape)
    cArray3 = NumCpp.NdArray(shape)
    cArray4 = NumCpp.NdArray(shape)
    data1 = np.random.randint(1, 100, [shape.rows, shape.cols])
    data2 = np.random.randint(1, 100, [shape.rows, shape.cols])
    data3 = np.random.randint(1, 100, [shape.rows, shape.cols])
    data4 = np.random.randint(1, 100, [shape.rows, shape.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    cArray3.setArray(data3)
    cArray4.setArray(data4)
    if np.array_equal(NumCpp.MethodsDouble.stack(cArray1, cArray2, cArray3, cArray4, NumCpp.Axis.COL),
                      np.hstack([data1, data2, data3, data4])):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))
    return
    print(colored('Testing std: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.round(NumCpp.MethodsDouble.std(cArray, NumCpp.Axis.NONE).item(), 10) == np.round(np.std(data), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing std: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.std(cArray, NumCpp.Axis.ROW).getNumpyArray().flatten(), 10), np.round(np.std(data, axis=0), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing std: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.std(cArray, NumCpp.Axis.COL).getNumpyArray().flatten(), 10), np.round(np.std(data, axis=1), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing sum: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if NumCpp.MethodsDouble.sum(cArray, NumCpp.Axis.NONE).item() == np.sum(data):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing sum: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.sum(cArray, NumCpp.Axis.ROW).getNumpyArray().flatten(), np.sum(data, axis=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing sum: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.sum(cArray, NumCpp.Axis.COL).getNumpyArray().flatten(), np.sum(data, axis=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing swapaxes', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.swapaxes(cArray).getNumpyArray(), data.T):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing tan scalar', 'cyan'))
    value = np.random.rand(1).item() * np.pi
    if np.round(NumCpp.MethodsDouble.tanScalar(value), 10) == np.round(np.tan(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing tan array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.tanArray(cArray), 10), np.round(np.tan(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing tanh scalar', 'cyan'))
    value = np.random.rand(1).item() * np.pi
    if np.round(NumCpp.MethodsDouble.tanhScalar(value), 10) == np.round(np.tanh(value), 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing tanh array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.tanhArray(cArray), 10), np.round(np.tanh(data), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing tile rectangle', 'cyan'))
    shapeInput = np.random.randint(1, 10, [2, ])
    shapeRepeat = np.random.randint(1, 10, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    shapeR = NumCpp.Shape(shapeRepeat[0].item(), shapeRepeat[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.tileRectangle(cArray, shapeR.rows, shapeR.cols), np.tile(data, shapeRepeat)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing tile shape', 'cyan'))
    shapeInput = np.random.randint(1, 10, [2, ])
    shapeRepeat = np.random.randint(1, 10, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    shapeR = NumCpp.Shape(shapeRepeat[0].item(), shapeRepeat[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.tileShape(cArray, shapeR), np.tile(data, shapeRepeat)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing tofile bin', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    filename = r'C:\Temp\temp'
    NumCpp.MethodsDouble.tofile(cArray, filename, '')
    if os.path.exists(filename + '.bin'):
        data2 = np.fromfile(filename + '.bin', np.double).reshape(shapeInput)
        if np.array_equal(data, data2):
            print(colored('\tPASS', 'green'))
        else:
            print(colored('\tFAIL', 'red'))
        os.remove(filename + '.bin')
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing tofile txt', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    filename = r'C:\Temp\temp'
    NumCpp.MethodsDouble.tofile(cArray, filename, '\n')
    if os.path.exists(filename + '.txt'):
        data2 = np.fromfile(filename + '.txt', dtype=np.double, sep='\n').reshape(shapeInput)
        if np.array_equal(data, data2):
            print(colored('\tPASS', 'green'))
        else:
            print(colored('\tFAIL', 'red'))
        os.remove(filename + '.txt')
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing toStlVector', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    out = np.asarray(NumCpp.MethodsDouble.toStlVector(cArray))
    if np.array_equal(out, data.flatten()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing trace: Offset=Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    offset = np.random.randint(0, shape.rows, [1, ]).item()
    if np.array_equal(NumCpp.MethodsDouble.trace(cArray, offset, NumCpp.Axis.ROW), data.trace(offset, axis1=1, axis2=0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing trace: Offset=Col', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    offset = np.random.randint(0, shape.rows, [1, ]).item()
    if np.array_equal(NumCpp.MethodsDouble.trace(cArray, offset, NumCpp.Axis.COL), data.trace(offset, axis1=0, axis2=1)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing transpose', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.transpose(cArray).getNumpyArray(), np.transpose(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing trapz: Axis = None with constant dx', 'cyan'))
    shape = NumCpp.Shape(np.random.randint(10, 20, [1,]).item(), 1)
    cArray = NumCpp.NdArray(shape)
    coeffs = np.random.randint(0, 10, [2, ])
    dx = np.random.rand(1).item()
    data = np.array([x ** 2 - coeffs[0] * x + coeffs[1] for x in range(shape.size())])
    cArray.setArray(data)
    integralC = NumCpp.MethodsDouble.trapzDx(cArray, dx, NumCpp.Axis.NONE).item()
    integralPy = np.trapz(data, dx=dx)
    if np.round(integralC, 10) == np.round(integralPy, 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing trapz: Axis = Row with constant dx', 'cyan'))
    shape = NumCpp.Shape(np.random.randint(10, 20, [1,]).item(), np.random.randint(10, 20, [1,]).item())
    cArray = NumCpp.NdArray(shape)
    coeffs = np.random.randint(0, 10, [2, ])
    dx = np.random.rand(1).item()
    data = np.array([x ** 2 - coeffs[0] * x - coeffs[1] for x in range(shape.size())]).reshape(shape.rows, shape.cols)
    cArray.setArray(data)
    integralC = NumCpp.MethodsDouble.trapzDx(cArray, dx, NumCpp.Axis.ROW).flatten()
    integralPy = np.trapz(data, dx=dx, axis=0)
    if np.array_equal(np.round(integralC, 8), np.round(integralPy, 8)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing trapz: Axis = Col with constant dx', 'cyan'))
    shape = NumCpp.Shape(np.random.randint(10, 20, [1,]).item(), np.random.randint(10, 20, [1,]).item())
    cArray = NumCpp.NdArray(shape)
    coeffs = np.random.randint(0, 10, [2, ])
    dx = np.random.rand(1).item()
    data = np.array([x ** 2 - coeffs[0] * x - coeffs[1] for x in range(shape.size())]).reshape(shape.rows, shape.cols)
    cArray.setArray(data)
    integralC = NumCpp.MethodsDouble.trapzDx(cArray, dx, NumCpp.Axis.COL).flatten()
    integralPy = np.trapz(data, dx=dx, axis=1)
    if np.array_equal(np.round(integralC, 8), np.round(integralPy, 8)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing trapz: Axis = None with variable dx', 'cyan'))
    shape = NumCpp.Shape(1, np.random.randint(10, 20, [1,]).item())
    cArrayY = NumCpp.NdArray(shape)
    cArrayX = NumCpp.NdArray(shape)
    coeffs = np.random.randint(0, 10, [2, ])
    dx = np.random.rand(shape.rows, shape.cols)
    data = np.array([x ** 2 - coeffs[0] * x + coeffs[1] for x in range(shape.size())])
    cArrayY.setArray(data)
    cArrayX.setArray(dx)
    integralC = NumCpp.MethodsDouble.trapz(cArrayY, cArrayX, NumCpp.Axis.NONE).item()
    integralPy = np.trapz(data, x=dx)
    if np.round(integralC, 10) == np.round(integralPy, 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing trapz: Axis = Row with variable dx', 'cyan'))
    shape = NumCpp.Shape(np.random.randint(10, 20, [1,]).item(), np.random.randint(10, 20, [1,]).item())
    cArrayY = NumCpp.NdArray(shape)
    cArrayX = NumCpp.NdArray(shape)
    coeffs = np.random.randint(0, 10, [2, ])
    dx = np.random.rand(shape.rows, shape.cols)
    data = np.array([x ** 2 - coeffs[0] * x + coeffs[1] for x in range(shape.size())]).reshape(shape.rows, shape.cols)
    cArrayY.setArray(data)
    cArrayX.setArray(dx)
    integralC = NumCpp.MethodsDouble.trapz(cArrayY, cArrayX, NumCpp.Axis.ROW).flatten()
    integralPy = np.trapz(data, x=dx, axis=0)
    if np.array_equal(np.round(integralC, 8), np.round(integralPy, 8)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing trapz: Axis = Col with variable dx', 'cyan'))
    shape = NumCpp.Shape(np.random.randint(10, 20, [1,]).item(), np.random.randint(10, 20, [1,]).item())
    cArrayY = NumCpp.NdArray(shape)
    cArrayX = NumCpp.NdArray(shape)
    coeffs = np.random.randint(0, 10, [2, ])
    dx = np.random.rand(shape.rows, shape.cols)
    data = np.array([x ** 2 - coeffs[0] * x + coeffs[1] for x in range(shape.size())]).reshape(shape.rows, shape.cols)
    cArrayY.setArray(data)
    cArrayX.setArray(dx)
    integralC = NumCpp.MethodsDouble.trapz(cArrayY, cArrayX, NumCpp.Axis.COL).flatten()
    integralPy = np.trapz(data, x=dx, axis=1)
    if np.array_equal(np.round(integralC, 8), np.round(integralPy, 8)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing tril: square', 'cyan'))
    squareSize = np.random.randint(10, 100, [1, ]).item()
    offset = np.random.randint(0, squareSize, [1, ]).item()
    if np.array_equal(NumCpp.MethodsDouble.trilSquare(squareSize, offset), np.tri(squareSize, k=offset)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing tril: rectangle', 'cyan'))
    shapeInput = np.random.randint(10, 100, [2, ])
    offset = np.random.randint(0, squareSize, [1, ]).item()
    if np.array_equal(NumCpp.MethodsDouble.trilRect(shapeInput[0].item(), shapeInput[1].item(), offset),
                      np.tri(shapeInput[0].item(), shapeInput[1].item(), k=offset)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing triu: square', 'cyan'))
    squareSize = np.random.randint(10, 100, [1, ]).item()
    offset = np.random.randint(0, squareSize, [1, ]).item()
    if np.array_equal(NumCpp.MethodsDouble.triuSquare(squareSize, offset), np.tri(squareSize, k=offset).T):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing triu: rectangle', 'cyan'))
    shapeInput = np.random.randint(10, 100, [2, ])
    offset = np.random.randint(0, squareSize, [1, ]).item()
    if np.array_equal(NumCpp.MethodsDouble.triuRect(shapeInput[0].item(), shapeInput[1].item(), offset),
                      np.tri(shapeInput[0].item(), shapeInput[1].item(), k=offset).T):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing trim_zeros: "f"', 'cyan'))
    numElements = np.random.randint(50, 100, [1, ]).item()
    offsetBeg = np.random.randint(0, 10, [1, ]).item()
    offsetEnd = np.random.randint(10, numElements, [1, ]).item()
    shape = NumCpp.Shape(1, numElements)
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols])
    data[0, :offsetBeg] = 0
    data[0, -offsetEnd:] = 0
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.trim_zeros(cArray, 'f').getNumpyArray().flatten(),
                      np.trim_zeros(data.flatten(), 'f')):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing trim_zeros: "b"', 'cyan'))
    numElements = np.random.randint(50, 100, [1, ]).item()
    offsetBeg = np.random.randint(0, 10, [1, ]).item()
    offsetEnd = np.random.randint(10, numElements, [1, ]).item()
    shape = NumCpp.Shape(1, numElements)
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols])
    data[0, :offsetBeg] = 0
    data[0, -offsetEnd:] = 0
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.trim_zeros(cArray, 'b').getNumpyArray().flatten(),
                      np.trim_zeros(data.flatten(), 'b')):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing trim_zeros: "fb"', 'cyan'))
    numElements = np.random.randint(50, 100, [1, ]).item()
    offsetBeg = np.random.randint(0, 10, [1, ]).item()
    offsetEnd = np.random.randint(10, numElements, [1, ]).item()
    shape = NumCpp.Shape(1, numElements)
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(1, 100, [shape.rows, shape.cols])
    data[0, :offsetBeg] = 0
    data[0, -offsetEnd:] = 0
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.trim_zeros(cArray, 'fb').getNumpyArray().flatten(),
                      np.trim_zeros(data.flatten(), 'fb')):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing trunc scalar', 'cyan'))
    value = np.random.rand(1).item() * np.pi
    if NumCpp.MethodsDouble.truncScalar(value) == np.trunc(value):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing trunc array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.truncArray(cArray), np.trunc(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing union1d', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArrayInt(shape)
    cArray2 = NumCpp.NdArrayInt(shape)
    data1 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    data2 = np.random.randint(1, 100, [shape.rows, shape.cols]).astype(np.uint32)
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    if np.array_equal(NumCpp.MethodsDouble.union1d(cArray1, cArray2).getNumpyArray().flatten(), np.union1d(data1, data2)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing unique array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    if np.array_equal(NumCpp.MethodsDouble.unique(cArray).getNumpyArray().flatten(), np.unique(data)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing unwrap scalar', 'cyan'))
    value = np.random.randn(1).item() * 3 * np.pi
    if value < 0:
        pValue = value + 2 * np.pi
    elif value >= 2 * np.pi:
        pValue = value - 2 * np.pi
    else:
        pValue = value
    if np.round(NumCpp.MethodsDouble.unwrapScalar(value), 10) == np.round(pValue, 10):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing unwrap array', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.rand(shape.rows, shape.cols)
    cArray.setArray(data)
    data[data < 0] = data[data < 0] + 2 * np.pi
    data[data > 2 * np.pi] = data[data > 2 * np.pi] - 2 * np.pi
    if np.array_equal(np.round(NumCpp.MethodsDouble.unwrapArray(cArray), 10), np.round(data, 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing var: Axis = None', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols])
    cArray.setArray(data)
    if np.round(NumCpp.MethodsDouble.var(cArray, NumCpp.Axis.NONE).item(), 9) == np.round(np.var(data), 9):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing var: Axis = Row', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.var(cArray, NumCpp.Axis.ROW).getNumpyArray().flatten(), 9), np.round(np.var(data, axis=0), 9)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing var: Axis = Column', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.NdArray(shape)
    data = np.random.randint(0, 100, [shape.rows, shape.cols]).astype(np.double)
    cArray.setArray(data)
    if np.array_equal(np.round(NumCpp.MethodsDouble.var(cArray, NumCpp.Axis.COL).getNumpyArray().flatten(), 9), np.round(np.var(data, axis=1), 9)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing vstack', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape1 = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    shape2 = NumCpp.Shape(shapeInput[0].item() + np.random.randint(1, 10, [1,]).item(), shapeInput[1].item())
    shape3 = NumCpp.Shape(shapeInput[0].item() + np.random.randint(1, 10, [1,]).item(), shapeInput[1].item())
    shape4 = NumCpp.Shape(shapeInput[0].item() + np.random.randint(1, 10, [1,]).item(), shapeInput[1].item())
    cArray1 = NumCpp.NdArray(shape1)
    cArray2 = NumCpp.NdArray(shape2)
    cArray3 = NumCpp.NdArray(shape3)
    cArray4 = NumCpp.NdArray(shape4)
    data1 = np.random.randint(1, 100, [shape1.rows, shape1.cols])
    data2 = np.random.randint(1, 100, [shape2.rows, shape2.cols])
    data3 = np.random.randint(1, 100, [shape3.rows, shape3.cols])
    data4 = np.random.randint(1, 100, [shape4.rows, shape4.cols])
    cArray1.setArray(data1)
    cArray2.setArray(data2)
    cArray3.setArray(data3)
    cArray4.setArray(data4)
    if np.array_equal(NumCpp.MethodsDouble.vstack(cArray1, cArray2, cArray3, cArray4),
                      np.vstack([data1, data2, data3, data4])):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing zeros square', 'cyan'))
    shapeInput = np.random.randint(1, 100, [1, ]).item()
    cArray = NumCpp.MethodsDouble.zerosSquare(shapeInput)
    if (cArray.shape[0] == shapeInput and cArray.shape[1] == shapeInput and
            cArray.size == shapeInput ** 2 and np.all(cArray == 0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing zeros rectangle', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    cArray = NumCpp.MethodsDouble.zerosRowCol(shapeInput[0].item(), shapeInput[1].item())
    if (cArray.shape[0] == shapeInput[0] and cArray.shape[1] == shapeInput[1] and
            cArray.size == shapeInput.prod() and np.all(cArray == 0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing zeros Shape', 'cyan'))
    shapeInput = np.random.randint(20, 100, [2, ])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    cArray = NumCpp.MethodsDouble.zerosShape(shape)
    if (cArray.shape[0] == shape.rows and cArray.shape[1] == shape.cols and
            cArray.size == shapeInput.prod() and np.all(cArray == 0)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

####################################################################################
if __name__ == '__main__':
    doTest()
