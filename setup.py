from setuptools import setup

exec (open('dash_flexbox_grid/version.py').read())

setup(
    name='dash_flexbox_grid',
    version=__version__,
    author='pikhovkin',
    packages=['dash_flexbox_grid'],
    include_package_data=True,
    license='MIT',
    description='Wrapper around react-flexbox-grid',
    install_requires=[]
)
