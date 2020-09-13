# cliassist
The cliassist is an open source library, build upon the PyDoc library to help different users with different types of questions regarding python packages, including the query based on human understandable format

# This is the example JSON that we generate out of the program

Parameters: 
----------
a : array_like
Array containing numbers whose mean is desired. If `a` is not an
array, a conversion is attempted.
axis : None or int or tuple of ints, optional
Axis or axes along which the means are computed. The default is to
compute the mean of the flattened array.
.. versionadded:: 1.7.0
If this is a tuple of ints, a mean is performed over multiple axes,
instead of a single axis or all the axes as before.
dtype : data-type, optional
Type to use in computing the mean.  For integer inputs, the default
is `float64`; for floating point inputs, it is the same as the
input dtype.
out : ndarray, optional
Alternate output array in which to place the result.  The default
is ``None``; if provided, it must have the same shape as the
expected output, but the type will be cast if necessary.
See `ufuncs-output-type` for more details.
keepdims : bool, optional
If this is set to True, the axes which are reduced are left
in the result as dimensions with size one. With this option,
the result will broadcast correctly against the input array.
If the default value is passed, then `keepdims` will not be
passed through to the `mean` method of sub-classes of
`ndarray`, however any non-default value will be.  If the
sub-class' method does not implement `keepdims` any
exceptions will be raised.

Returns: 
-------
m : ndarray, see dtype parameter above
If `out=None`, returns a new array containing the mean values,
otherwise a reference to the output array is returned.

See Also: 
--------
average : Weighted average
std, var, nanmean, nanstd, nanvar

Notes: 
-----
The arithmetic mean is the sum of the elements along the axis divided
by the number of elements.
Note that for floating-point input, the mean is computed using the
same precision the input has.  Depending on the input data, this can
cause the results to be inaccurate, especially for `float32` (see
example below).  Specifying a higher-precision accumulator using the
`dtype` keyword can alleviate this issue.
By default, `float16` results are computed using `float32` intermediates
for extra precision.

Examples: 
--------
>>> a = np.array([[1, 2], [3, 4]])
>>> np.mean(a)
2.5
>>> np.mean(a, axis=0)
array([2., 3.])
>>> np.mean(a, axis=1)
array([1.5, 3.5])
In single precision, `mean` can be inaccurate:
>>> a = np.zeros((2, 512*512), dtype=np.float32)
>>> a[0, :] = 1.0
>>> a[1, :] = 0.1
>>> np.mean(a)
0.54999924
Computing the mean in float64 is more accurate:
>>> np.mean(a, dtype=np.float64)
0.55000000074505806 # may vary

