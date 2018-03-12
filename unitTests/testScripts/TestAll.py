import TestShape
import TestSlice
import TestTimer
import TestNdArray
import TestMethods
import TestConstants
import TestLinalg
import TestRandom
import TestPolynomial
import TestFFT
import TestUtils
import TestDtypeInfo

#################################################################################
def doTest():
    TestShape.doTest()
    TestSlice.doTest()
    TestTimer.doTest()
    TestUtils.doTest()
    TestDtypeInfo.doTest()
    TestNdArray.doTest()
    TestMethods.doTest()
    TestConstants.doTest()
    TestLinalg.doTest()
    TestRandom.doTest()
    TestPolynomial.doTest()
    TestFFT.doTest()

#################################################################################
if __name__ == '__main__':
    doTest()