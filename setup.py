import os

from setuptools import setup, find_packages

VERSION = '0.1a1'

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''
try:
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    CHANGES = ''

requires = [
    'kotti',
    ]

setup(name='kotti_sharethis',
      version=VERSION,
      license='http://koansys.com/license.txt',

      description='An addon that adds the ShareThis widget to your Kotti site.',
      long_description=README + '\n\n' + CHANGES,

      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],

      author='Koansys, LLC',
      author_email='info@koansys.com',
      url='https://github.com/koansys/kotti_sharethis',

      keywords='web pyramid pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="kotti_sharethis",
      entry_points="""\
      [paste.app_factory]
      main = kotti_sharethis:main
      """,
)
