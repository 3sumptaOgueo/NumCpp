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
#include"Shape.hpp"
#include"NdArray.hpp"

#include"boost/random.hpp"

namespace NumC
{
	//================================Random Namespace=============================
	namespace Random
	{
		//============================================================================
		// Method Description: 
		//						Seeds the random number generator
		//		
		// Inputs:
		//				seed
		// Outputs:
		//				None
		//
		void seed(uint32 inSeed)
		{

		}

		//============================================================================
		// Method Description: 
		//						Create an array of the given shape and populate it with 
		//						random samples from a uniform distribution over [0, 1).
		//		
		// Inputs:
		//				None
		// Outputs:
		//				None
		//
		template<typename dtype>
		NdArray<dtype> rand(const Shape& inShape)
		{

		}

		//============================================================================
		// Method Description: 
		//						Return random integers from low (inclusive) to high (exclusive), 
		//						with the given shape
		//		
		// Inputs:
		//				None
		// Outputs:
		//				None
		//
		template<typename dtype>
		NdArray<dtype> randint(dtype inLow, dtype inHigh, const Shape& inShape)
		{

		}

		//============================================================================
		// Method Description: 
		//						Create an array of the given shape and populate it with 
		//						random samples from the �standard normal� distribution.
		//		
		// Inputs:
		//				None
		// Outputs:
		//				None
		//
		template<typename dtype>
		NdArray<dtype> randn(const Shape& inShape)
		{

		}
	}
}