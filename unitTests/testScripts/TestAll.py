import TestShape
import TestSlice
import TestTimer
import TestNdArray
import TestMethods
import TestConstants
import TestLinalg
import TestRandom

#################################################################################
def doTest():
    TestShape.doTest()
    TestSlice.doTest()
    TestTimer.doTest()
    TestNdArray.doTest()
    TestMethods.doTest()
    TestConstants.doTest()
    TestLinalg.doTest()
    TestRandom.doTest()

#################################################################################
if __name__ == '__main__':
    doTest()