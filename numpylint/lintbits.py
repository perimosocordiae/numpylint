# Dict of all the patterns with their replacements.
# Structure:
#   name of replacement -> list of (pattern, replacement, kwargs) tuples

LINTBITS = {
    'diagonal matrix dot product': [
        # diag(x).dot(y)
        ('${diag}(${x}).dot(${y})', '((${x}) * (${y}).T).T',
         dict(diag='name=numpy.diag')),
        # dot(diag(x), y)
        ('${dot}(${diag}(${x}), ${y})', '((${x}) * (${y}).T).T',
         dict(diag='name=numpy.diag', dot='name=numpy.dot')),
        # x.dot(diag(y))
        ('${x}.dot(${diag}(${y}))', '((${x}) * (${y}))',
         dict(diag='name=numpy.diag')),
        # dot(x, diag(y))
        ('${dot}(${x}, ${diag}(${y}))', '((${x}) * (${y}))',
         dict(diag='name=numpy.diag', dot='name=numpy.dot')),
    ],
    'inverting result of in1d': [
        # ~np.in1d(x, y)
        ('~${in1d}(${x}, ${y})', '${in1d}(${x}, ${y}, invert=True)',
         dict(in1d='name=numpy.in1d')),
        # ~np.in1d(x, y, assume_unique=z)
        ('~${in1d}(${x}, ${y}, assume_unique=${z})',
         '${in1d}(${x}, ${y}, assume_unique=${z}, invert=True)',
         dict(in1d='name=numpy.in1d')),
    ],
    'in-place transpose': [
        # x += x.T
        ('${x} += ${x}.T', '${x} = ${x} + ${x}.T', dict()),
        # x += x.transpose()
        ('${x} += ${x}.transpose()', '${x} = ${x} + ${x}.T', dict()),
    ],
}
