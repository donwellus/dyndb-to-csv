from setuptools import setup

setup(
    name='dyndb2csv',
    version='0.1',
    py_modules=['dyndb2csv'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        dyndb2csv=dyndb2csv:cli
    ''',
)