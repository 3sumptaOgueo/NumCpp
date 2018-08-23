import numpy as np
from termcolor import colored
import sys
sys.path.append(r'../build/x64/Release')
import NumCpp

####################################################################################
def doTest():
    print(colored('Testing Utils', 'magenta'))
    print(colored('Testing num2str', 'cyan'))
    value = np.random.randint(1, 100, [1, ], dtype=np.int8).item()
    if NumCpp.UtilsInt8.num2str(value) == str(value):
        print(colored('\tPASS int8', 'green'))
    else:
        print(colored('\tFAIL int8', 'red'))

    value = np.random.randint(1, 100, [1, ], dtype=np.int16).item()
    if NumCpp.UtilsInt16.num2str(value) == str(value):
        print(colored('\tPASS int16', 'green'))
    else:
        print(colored('\tFAIL int16', 'red'))

    value = np.random.randint(1, 100, [1, ], dtype=np.int32).item()
    if NumCpp.UtilsInt32.num2str(value) == str(value):
        print(colored('\tPASS int32', 'green'))
    else:
        print(colored('\tFAIL int32', 'red'))

    value = np.random.randint(1, 100, [1, ], dtype=np.int64).item()
    if NumCpp.UtilsInt64.num2str(value) == str(value):
        print(colored('\tPASS int64', 'green'))
    else:
        print(colored('\tFAIL int64', 'red'))

    value = np.random.randint(1, 100, [1, ], dtype=np.uint8).item()
    if NumCpp.UtilsUint8.num2str(value) == str(value):
        print(colored('\tPASS uint8', 'green'))
    else:
        print(colored('\tFAIL uint8', 'red'))

    value = np.random.randint(1, 100, [1, ], dtype=np.uint16).item()
    if NumCpp.UtilsUint16.num2str(value) == str(value):
        print(colored('\tPASS uint16', 'green'))
    else:
        print(colored('\tFAIL uint16', 'red'))

    value = np.random.randint(1, 100, [1, ], dtype=np.uint32).item()
    if NumCpp.UtilsUint32.num2str(value) == str(value):
        print(colored('\tPASS uint32', 'green'))
    else:
        print(colored('\tFAIL uint32', 'red'))

    value = np.random.randint(1, 100, [1, ], dtype=np.uint64).item()
    if NumCpp.UtilsUint64.num2str(value) == str(value):
        print(colored('\tPASS uint64', 'green'))
    else:
        print(colored('\tFAIL uint64', 'red'))

    # value = np.random.randint(1, 100, [1, ]).astype(np.double).item()
    # if NumCpp.UtilsDouble.num2str(value) == str(value):
    #     print(colored('\tPASS double', 'green'))
    # else:
    #     print(colored('\tFAIL double', 'red'))
    #
    # value = np.random.randint(1, 100, [1, ]).astype(np.float32).item()
    # if NumCpp.UtilsFloat.num2str(value) == str(value):
    #     print(colored('\tPASS float', 'green'))
    # else:
    #     print(colored('\tFAIL float', 'red'))

    print(colored('Testing sqr', 'cyan'))
    value = np.random.randint(1, 12, [1, ], dtype=np.int8).item()
    if NumCpp.UtilsInt8.sqr(value) == value ** 2:
        print(colored('\tPASS int8', 'green'))
    else:
        print(colored('\tFAIL int8', 'red'))

    value = np.random.randint(1, 100, [1, ], dtype=np.int16).item()
    if NumCpp.UtilsInt16.sqr(value) == value ** 2:
        print(colored('\tPASS int16', 'green'))
    else:
        print(colored('\tFAIL int16', 'red'))

    value = np.random.randint(1, 100, [1, ], dtype=np.int32).item()
    if NumCpp.UtilsInt32.sqr(value) == value ** 2:
        print(colored('\tPASS int32', 'green'))
    else:
        print(colored('\tFAIL int32', 'red'))

    value = np.random.randint(1, 100, [1, ], dtype=np.int64).item()
    if NumCpp.UtilsInt64.sqr(value) == value ** 2:
        print(colored('\tPASS int64', 'green'))
    else:
        print(colored('\tFAIL int64', 'red'))

    value = np.random.randint(1, 15, [1, ], dtype=np.uint8).item()
    if NumCpp.UtilsUint8.sqr(value) == value ** 2:
        print(colored('\tPASS uint8', 'green'))
    else:
        print(colored('\tFAIL uint8', 'red'))

    value = np.random.randint(1, 100, [1, ], dtype=np.uint16).item()
    if NumCpp.UtilsUint16.sqr(value) == value ** 2:
        print(colored('\tPASS uint16', 'green'))
    else:
        print(colored('\tFAIL uint16', 'red'))

    value = np.random.randint(1, 100, [1, ], dtype=np.uint32).item()
    if NumCpp.UtilsUint32.sqr(value) == value ** 2:
        print(colored('\tPASS uint32', 'green'))
    else:
        print(colored('\tFAIL uint32', 'red'))

    value = np.random.randint(1, 100, [1, ], dtype=np.uint64).item()
    if NumCpp.UtilsUint64.sqr(value) == value ** 2:
        print(colored('\tPASS uint64', 'green'))
    else:
        print(colored('\tFAIL uint64', 'red'))

    value = np.random.randint(1, 100, [1, ]).astype(np.double).item()
    if NumCpp.UtilsDouble.sqr(value) == value ** 2:
        print(colored('\tPASS double', 'green'))
    else:
        print(colored('\tFAIL double', 'red'))

    value = np.random.randint(1, 100, [1, ]).astype(np.float32).item()
    if NumCpp.UtilsFloat.sqr(value) == value ** 2:
        print(colored('\tPASS float', 'green'))
    else:
        print(colored('\tFAIL float', 'red'))

    print(colored('Testing cube', 'cyan'))
    value = np.random.randint(1, 6, [1, ], dtype=np.int8).item()
    if NumCpp.UtilsInt8.cube(value) == value ** 3:
        print(colored('\tPASS int8', 'green'))
    else:
        print(colored('\tFAIL int8', 'red'))

    value = np.random.randint(1, 32, [1, ], dtype=np.int16).item()
    if NumCpp.UtilsInt16.cube(value) == value ** 3:
        print(colored('\tPASS int16', 'green'))
    else:
        print(colored('\tFAIL int16', 'red'))

    value = np.random.randint(1, 100, [1, ], dtype=np.int32).item()
    if NumCpp.UtilsInt32.cube(value) == value ** 3:
        print(colored('\tPASS int32', 'green'))
    else:
        print(colored('\tFAIL int32', 'red'))

    value = np.random.randint(1, 100, [1, ], dtype=np.int64).item()
    if NumCpp.UtilsInt64.cube(value) == value ** 3:
        print(colored('\tPASS int64', 'green'))
    else:
        print(colored('\tFAIL int64', 'red'))

    value = np.random.randint(1, 7, [1, ], dtype=np.uint8).item()
    if NumCpp.UtilsUint8.cube(value) == value ** 3:
        print(colored('\tPASS uint8', 'green'))
    else:
        print(colored('\tFAIL uint8', 'red'))

    value = np.random.randint(1, 41, [1, ], dtype=np.uint16).item()
    if NumCpp.UtilsUint16.cube(value) == value ** 3:
        print(colored('\tPASS uint16', 'green'))
    else:
        print(colored('\tFAIL uint16', 'red'))

    value = np.random.randint(1, 100, [1, ], dtype=np.uint32).item()
    if NumCpp.UtilsUint32.cube(value) == value ** 3:
        print(colored('\tPASS uint32', 'green'))
    else:
        print(colored('\tFAIL uint32', 'red'))

    value = np.random.randint(1, 100, [1, ], dtype=np.uint64).item()
    if NumCpp.UtilsUint64.cube(value) == value ** 3:
        print(colored('\tPASS uint64', 'green'))
    else:
        print(colored('\tFAIL uint64', 'red'))

    value = np.random.randint(1, 100, [1, ]).astype(np.double).item()
    if NumCpp.UtilsDouble.cube(value) == value ** 3:
        print(colored('\tPASS double', 'green'))
    else:
        print(colored('\tFAIL double', 'red'))

    value = np.random.randint(1, 100, [1, ]).astype(np.float32).item()
    if NumCpp.UtilsFloat.cube(value) == value ** 3:
        print(colored('\tPASS float', 'green'))
    else:
        print(colored('\tFAIL float', 'red'))

    print(colored('Testing power', 'cyan'))
    value = np.random.randint(1, 4, [1, ], dtype=np.int8).item()
    power = np.random.randint(1, 4, dtype=np.uint8).item()
    if NumCpp.UtilsInt8.power(value, power) == value ** power:
        print(colored('\tPASS int8', 'green'))
    else:
        print(colored('\tFAIL int8', 'red'))

    value = np.random.randint(1, 10, [1, ], dtype=np.int16).item()
    if NumCpp.UtilsInt16.power(value, power) == value ** power:
        print(colored('\tPASS int16', 'green'))
    else:
        print(colored('\tFAIL int16', 'red'))

    value = np.random.randint(1, 10, [1, ], dtype=np.int32).item()
    if NumCpp.UtilsInt32.power(value, power) == value ** power:
        print(colored('\tPASS int32', 'green'))
    else:
        print(colored('\tFAIL int32', 'red'))

    value = np.random.randint(1, 10, [1, ], dtype=np.int64).item()
    if NumCpp.UtilsInt64.power(value, power) == value ** power:
        print(colored('\tPASS int64', 'green'))
    else:
        print(colored('\tFAIL int64', 'red'))

    value = np.random.randint(1, 4, [1, ], dtype=np.uint8).item()
    if NumCpp.UtilsUint8.power(value, power) == value ** power:
        print(colored('\tPASS uint8', 'green'))
    else:
        print(colored('\tFAIL uint8', 'red'))

    value = np.random.randint(1, 10, [1, ], dtype=np.uint16).item()
    if NumCpp.UtilsUint16.power(value, power) == value ** power:
        print(colored('\tPASS uint16', 'green'))
    else:
        print(colored('\tFAIL uint16', 'red'))

    value = np.random.randint(1, 10, [1, ], dtype=np.uint32).item()
    if NumCpp.UtilsUint32.power(value, power) == value ** power:
        print(colored('\tPASS uint32', 'green'))
    else:
        print(colored('\tFAIL uint32', 'red'))

    value = np.random.randint(1, 10, [1, ], dtype=np.uint64).item()
    if NumCpp.UtilsUint64.power(value, power) == value ** power:
        print(colored('\tPASS uint64', 'green'))
    else:
        print(colored('\tFAIL uint64', 'red'))

    value = np.random.randint(1, 10, [1, ]).astype(np.double).item()
    if NumCpp.UtilsDouble.power(value, power) == value ** power:
        print(colored('\tPASS double', 'green'))
    else:
        print(colored('\tFAIL double', 'red'))

    value = np.random.randint(1, 10, [1, ]).astype(np.float32).item()
    if NumCpp.UtilsFloat.power(value, power) == value ** power:
        print(colored('\tPASS float', 'green'))
    else:
        print(colored('\tFAIL float', 'red'))

####################################################################################
if __name__ == '__main__':
    doTest()
