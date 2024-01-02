from distutils.core import setup, Extension


setup(name='herofuncs', 
      version='1.0',
      ext_modules=[Extension('herofuncs', sources=['herofuncs.c', 'heros.c'])])

