import numpy as np
import numpy
from numpy import diag

foo = np.random.random((5,5))
bar = np.arange(5)

ways = [
    np.diag(bar+1).dot(foo*2),
    diag(bar+1).dot(foo*2),
    numpy.diag(bar+1).dot(foo*2),
    np.dot(np.diag(bar+1), foo*2),
    ((bar+1) * (foo*2).T).T,
]

for i in xrange(len(ways)):
  for j in xrange(i+1,len(ways)):
    assert np.allclose(ways[i], ways[j])

ways = [
    (foo*2).dot(np.diag(bar+1)),
    (foo*2) * (bar+1),
]
for i in xrange(len(ways)):
  for j in xrange(i+1,len(ways)):
    assert np.allclose(ways[i], ways[j])

foo += foo.T
foo += foo.T.dot(foo)
