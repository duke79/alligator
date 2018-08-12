from setuptools import setup, find_packages

setup(
    name='Alligator',
    version='0.0.1',
    # license='Creative Commons Attribution-Noncommercial-Share Alike license',
    author='Pulkit Singh, Ankit Singh',
    author_email='pulkitsingh01@gmail.com, casbaliyan@gmail.com',
    description='New aggregator but called alligator',
    long_description=open('readme.md').read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask'],
)
