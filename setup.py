try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='instascope',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    py_modules=[
        'libs/horoscope',
        'libs/meme',
        'libs/pic'
    ],
    entry_points={
        'console_scripts':  ['main = main: main'],
    },
)
