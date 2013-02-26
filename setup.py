from setuptools import setup, find_packages

version = '1.0dev'

long_description = (
    open('README.rst').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(
    name='cosent.guruscan',
    version=version,
    description="Plone integration for GuruScan",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
    ],
    keywords='zope, plone, guruscan',
    author='Guido Stevens',
    author_email='guido.stevens@cosent.net',
    url='http://github.com/cosent/cosent.guruscan',
    license='gpl',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['cosent'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
    ],
    extras_require={'test': ['plone.app.testing']},
    entry_points="""
      # -*- Entry points: -*-
  	  [z3c.autoinclude.plugin]
  	  target = plone
      """,
)
