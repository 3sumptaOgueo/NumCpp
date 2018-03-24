// Copyright 2018 David Pilger
//
// Permission is hereby granted, free of charge, to any person obtaining a copy of this
// software and associated documentation files(the "Software"), to deal in the Software 
// without restriction, including without limitation the rights to use, copy, modify, 
// merge, publish, distribute, sublicense, and/or sell copies of the Software, and to 
// permit persons to whom the Software is furnished to do so, subject to the following 
// conditions :
//
// The above copyright notice and this permission notice shall be included in all copies 
// or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
// INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
// PURPOSE AND NONINFRINGEMENT.IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE 
// FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
// OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
// DEALINGS IN THE SOFTWARE.

#pragma once

#include"Types.hpp"
#include"NdArray.hpp"

namespace NumC
{
	//================================Linalg Namespace=============================
	namespace Linalg
	{
		//============================================================================
		// Method Description: 
		//						vector hat operator
		//		
		// Inputs:
		//				x
		//				y
		//				z
		// Outputs:
		//				3x3 NdArray
		//
		template<typename dtype>
		NdArray<dtype> hat(dtype inX, dtype inY, dtype inZ)
		{
			NdArray<dtype> returnArray(3);
			returnArray(0, 0) = 0.0;
			returnArray(0, 1) = -inZ;
			returnArray(0, 2) = inY;
			returnArray(1, 0) = inZ;
			returnArray(1, 1) = 0.0;
			returnArray(1, 2) = -inX;
			returnArray(2, 0) = -inY;
			returnArray(2, 1) = inX;
			returnArray(2, 2) = 0.0;

			return std::move(returnArray);
		}

		//============================================================================
		// Method Description: 
		//						vector hat operator
		//		
		// Inputs:
		//				NdArray 3x1, or 1x3 cartesian vector
		// Outputs:
		//				3x3 NdArray
		//
		template<typename dtype>
		NdArray<dtype> hat(const NdArray<dtype>& inVec)
		{
			if (inVec.size() != 3)
			{
				throw std::invalid_argument("ERROR: Linalg::hat: input vector must be a length 3 cartesian vector.");
			}

			return std::move(hat(inVec[0], inVec[1], inVec[2]));
		}
	}
}