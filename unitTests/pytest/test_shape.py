import numpy as np
import os
import sys
if sys.platform == 'linux':
    sys.path.append(r'../lib')
else:
    sys.path.append(os.path.abspath('../build/x64/Release'))
import NumCpp


####################################################################################
def test_shape():
    """Tests the NumCpp Shape class"""

    shape = NumCpp.Shape()
    assert shape.rows == 0 and shape.cols == 0

    shapeInput = np.random.randint(0, 100, [1,]).item()
    shape = NumCpp.Shape(shapeInput)
    assert shape.rows == shapeInput
    assert shape.cols == shapeInput

    shapeInput = np.random.randint(0, 100, [2,])
    shape = NumCpp.Shape(shapeInput[0].item(), shapeInput[1].item())
    assert shape.rows == shapeInput[0]
    assert shape.cols == shapeInput[1]

    shape2 = NumCpp.Shape(shape)
    assert shape2.rows == shape.rows
    assert shape2.cols == shape.cols

    shape = NumCpp.Shape()
    shapeInput = np.random.randint(0, 100, [2, ])
    shape.rows = shapeInput[0].item()
    shape.cols = shapeInput[1].item()
    assert shape.rows == shapeInput[0]
    assert shape.cols == shapeInput[1]

    shape.print()
