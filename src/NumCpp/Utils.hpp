/// @file
/// @author David Pilger <dpilger26@gmail.com>
/// [GitHub Repository](https://github.com/dpilger26/NumCpp)
/// @version 1.0
///
/// @section License
/// Copyright 2018 David Pilger
///
/// Permission is hereby granted, free of charge, to any person obtaining a copy of this
/// software and associated documentation files(the "Software"), to deal in the Software 
/// without restriction, including without limitation the rights to use, copy, modify, 
/// merge, publish, distribute, sublicense, and/or sell copies of the Software, and to 
/// permit persons to whom the Software is furnished to do so, subject to the following 
/// conditions :
///
/// The above copyright notice and this permission notice shall be included in all copies 
/// or substantial portions of the Software.
///
/// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
/// INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
/// PURPOSE AND NONINFRINGEMENT.IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE 
/// FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
/// OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
/// DEALINGS IN THE SOFTWARE.
///
/// @section Description
/// Usefull utility type functions
///
#pragma once

#include"NumCpp/DtypeInfo.hpp"

#include<string>

namespace NC
{
    namespace Utils
    {
        //============================================================================
        ///						tests that 2 floating point values are "essentially equal"
        ///		
        /// @param      inValue1
        /// @param      inValue2
        /// @param      inEpsilon
        ///
        /// @return     bool
        ///
        template<typename dtype>
        bool essentiallyEqual(dtype inValue1, dtype inValue2, dtype inEpsilon = DtypeInfo<dtype>::epsilon())
        {
            return fabs(inValue1 - inValue2) <= ((fabs(inValue1) > fabs(inValue2) ? fabs(inValue2) : fabs(inValue1)) * inEpsilon);
        }

        //============================================================================
        ///						Converts the number into a string
        ///		
        /// @param      inNumber
        ///
        /// @return     std::string
        ///
        template<typename dtype>
        static std::string num2str(dtype inNumber)
        {
            return std::to_string(inNumber);
        }

        //============================================================================
        ///						Squares in input value
        ///		
        /// @param      inValue
        ///
        /// @return     squared value
        ///
        template<typename dtype>
        static dtype sqr(dtype inValue)
        {
            return inValue * inValue;
        }

        //============================================================================
        ///						Cubes in input value
        ///		
        /// @param      inValue
        ///
        /// @return     cubed value
        ///
        template<typename dtype>
        static dtype cube(dtype inValue)
        {
            return inValue * inValue * inValue;
        }

        //============================================================================
        ///						Raises the input value to a power
        ///		
        /// @param      inValue
        /// @param      inPower
        ///
        /// @return     inValue raised to inPower
        ///
        template<typename dtype>
        static dtype power(dtype inValue, uint8 inPower)
        {
            if (inPower == 0)
            {
                return static_cast<dtype>(1);
            }

            dtype returnVal = inValue;
            for (uint8 exponent = 1; exponent < inPower; ++exponent)
            {
                returnVal *= inValue;
            }
            return returnVal;
        }

        //============================================================================
        ///						Returns the linear interpolation between two points
        ///		
        /// @param      inValue1
        /// @param      inValue2
        /// @param      inPercent
        ///
        /// @return     linear interpolated point
        ///
        template<typename dtype>
        static double interp(dtype inValue1, dtype inValue2, double inPercent)
        {
            return static_cast<double>(inValue1) * (1.0 - inPercent) + static_cast<double>(inValue2) * inPercent;
        }
    }
}
