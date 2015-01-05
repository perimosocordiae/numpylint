import os.path
import tempfile
from argparse import ArgumentParser
from rope.base.project import Project
from rope.base import libutils
from rope.refactor.restructure import Restructure

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
}


def lint(filepath, proj, orig_path, opts):
  mod = proj.get_file(filepath)
  if not libutils.is_python_file(proj, mod):
    if opts.verbose:
      print filepath, 'is not a Python file'
    return
  # proj.validate(mod)
  # libutils.analyze_module(proj, mod)
  for desc, bits in LINTBITS.iteritems():
    changes = []
    for pattern, goal, args in bits:
      r = Restructure(proj, pattern, goal, args=args)
      try:
        c = r.get_changes(resources=(mod,))
        if opts.overwrite:
          proj.do(c)
      except:  # Assume it's some syntax rope can't handle.
        break
      changes.extend(c.changes)
    if changes:
      print '%s: %s' % (orig_path, desc)
      if opts.verbose:
        print '\n'
        for c in changes:
          print c.get_description()


def main():
  ap = ArgumentParser()
  ap.add_argument('-v', '--verbose', action='store_true')
  ap.add_argument('--overwrite', action='store_true')
  ap.add_argument('files', metavar='FILE', nargs='+', help='File(s) to lint')
  args = ap.parse_args()
  tmpdir = tempfile.mkdtemp()
  proj = Project(tmpdir, ropefolder=None)
  for f in args.files:
    lint(os.path.relpath(f, start=tmpdir), proj, f, args)
  proj.close()

if __name__ == '__main__':
  main()
