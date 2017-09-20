# Package meta-data.
# From https://github.com/kennethreitz/setup.py/blob/master/setup.py

NAME = 'textedit'
DESCRIPTION = 'A simple Python text editor for Victorian authors who just want to write.  '
URL = 'https://github.com/veekaybee/textedit'
EMAIL = 'vickiboykis@gmail.com'
AUTHOR = 'Vicki Boykis'


# What packages are required for this module to be executed?
REQUIRED = [
    # 'requests', 'maya', 'records',
]

# Sets the path of execution to the top level of the package 
here = os.path.abspath(os.path.dirname(__file__))

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
    
)