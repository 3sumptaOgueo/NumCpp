/// @file
/// @author David Pilger <dpilger26@gmail.com>
/// [GitHub Repository](https://github.com/dpilger26/NumCpp)
///
/// License
/// Copyright 2018-2023 David Pilger
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
/// Description
/// Functions for working with NdArrays
///
#pragma once

#include "NumCpp/Core/Slice.hpp"
#include "NumCpp/Core/Types.hpp"
#include "NumCpp/NdArray.hpp"

namespace nc
{
    //============================================================================
    // Method Description:
    /// Insert values along the given axis before the given indices.
    ///
    /// NumPy Reference: https://numpy.org/doc/stable/reference/generated/numpy.insert.html
    ///
    /// @param arr: input array.
    /// @param index: index to insert the value before in the flattened
    /// @param value: value to insert
    /// @return index: index before which values are inserted.
    ///
    template<typename dtype>
    NdArray<dtype> insert(const NdArray<dtype>& arr, int32 index, const dtype& value)
    {
        return {};
    }

    //============================================================================
    // Method Description:
    /// Insert values along the given axis before the given indices.
    ///
    /// NumPy Reference: https://numpy.org/doc/stable/reference/generated/numpy.insert.html
    ///
    /// @param arr: input array.
    /// @param index: index to insert the values before in the flattened
    /// @param values: value to insert
    /// @return index: index before which values are inserted.
    ///
    template<typename dtype>
    NdArray<dtype> insert(const NdArray<dtype>& arr, int32 index, const NdArray<dtype>& values)
    {
        return {};
    }

    //============================================================================
    // Method Description:
    /// Insert values along the given axis before the given indices.
    ///
    /// NumPy Reference: https://numpy.org/doc/stable/reference/generated/numpy.insert.html
    ///
    /// @param arr: input array.
    /// @param index: index to insert the values before
    /// @param value: value to insert
    /// @param axis: axis along which to insert values
    /// @return index: index before which values are inserted.
    ///
    template<typename dtype>
    NdArray<dtype> insert(const NdArray<dtype>& arr, int32 index, const dtype& value, Axis axis)
    {
        switch (axis)
        {
            case Axis::NONE:
            {
                return insert(arr, index, value);
            }
            case Axis::ROW:
            {
                return {};
            }
            case Axis::COL:
            {
                return {};
            }
            default:
            {
                // get rid of compiler warning
                return {};
            }
        }
    }

    //============================================================================
    // Method Description:
    /// Insert values along the given axis before the given indices.
    ///
    /// NumPy Reference: https://numpy.org/doc/stable/reference/generated/numpy.insert.html
    ///
    /// @param arr: input array.
    /// @param index: index to insert the values before
    /// @param values: values to insert
    /// @param axis: axis along which to insert values
    /// @return index: index before which values are inserted.
    ///
    template<typename dtype>
    NdArray<dtype> insert(const NdArray<dtype>& arr, int32 index, const NdArray<dtype>& values, Axis axis)
    {
        switch (axis)
        {
            case Axis::NONE:
            {
                return insert(arr, index, values);
            }
            case Axis::ROW:
            {
                return {};
            }
            case Axis::COL:
            {
                return {};
            }
            default:
            {
                // get rid of compiler warning
                return {};
            }
        }
    }

    //============================================================================
    // Method Description:
    /// Insert values along the given axis before the given indices.
    ///
    /// NumPy Reference: https://numpy.org/doc/stable/reference/generated/numpy.insert.html
    ///
    /// @param arr: input array.
    /// @param indices: indices to insert the values before
    /// @param value: value to insert
    /// @param axis: axis along which to insert values
    /// @return index: index before which values are inserted.
    ///
    template<typename dtype, typename Indices, type_traits::ndarray_int_concept<Indices> = 0>
    NdArray<dtype> insert(const NdArray<dtype>& arr, const Indices& indices, const dtype& value, Axis axis = Axis::NONE)
    {
        return {};
    }

    //============================================================================
    // Method Description:
    /// Insert values along the given axis before the given indices.
    ///
    /// NumPy Reference: https://numpy.org/doc/stable/reference/generated/numpy.insert.html
    ///
    /// @param arr: input array.
    /// @param slice: slice to insert the values before
    /// @param value: values to insert
    /// @param axis: axis along which to insert values
    /// @return index: index before which values are inserted.
    ///
    template<typename dtype>
    NdArray<dtype> insert(const NdArray<dtype>& arr, Slice slice, const dtype& value, Axis axis = Axis::NONE)
    {
        auto sliceIndices = slice.toIndices(arr.dimSize(axis));
        return insert(arr, NdArray<uint32>(sliceIndices.data(), sliceIndices.size(), false), value, axis);
    }

    //============================================================================
    // Method Description:
    /// Insert values along the given axis before the given indices.
    ///
    /// NumPy Reference: https://numpy.org/doc/stable/reference/generated/numpy.insert.html
    ///
    /// @param arr: input array.
    /// @param indices: indices to insert the values before
    /// @param values: values to insert
    /// @param axis: axis along which to insert values
    /// @return index: index before which values are inserted.
    ///
    template<typename dtype, typename Indices, type_traits::ndarray_int_concept<Indices> = 0>
    NdArray<dtype>
        insert(const NdArray<dtype>& arr, const Indices& indices, const NdArray<dtype>& values, Axis axis = Axis::NONE)
    {
        return {};
    }

    //============================================================================
    // Method Description:
    /// Insert values along the given axis before the given indices.
    ///
    /// NumPy Reference: https://numpy.org/doc/stable/reference/generated/numpy.insert.html
    ///
    /// @param arr: input array.
    /// @param slice: slice to insert the values before
    /// @param values: values to insert
    /// @param axis: axis along which to insert values
    /// @return index: index before which values are inserted.
    ///
    template<typename dtype>
    NdArray<dtype> insert(const NdArray<dtype>& arr, Slice slice, const NdArray<dtype>& values, Axis axis = Axis::NONE)
    {
        auto sliceIndices = slice.toIndices(arr.dimSize(axis));
        return insert(arr, NdArray<uint32>(sliceIndices.data(), sliceIndices.size(), false), values, axis);
    }
} // namespace nc
