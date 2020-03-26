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
    install_requires=['python-telegram-bot==12.4.2', 'Pillow==7.0.0', 'saya==0.3.2', 'beautifulsoup4', 'aiohttp',
                      'async-timeout', 'attrs', 'certifi', 'cffi', 'chardet', 'click',
                      'cryptography', 'decorator', 'future', 'idna', 'idna-ssl', 'mkdir==2019.4.13',
                      'multidict==4.7.5', 'orderdict==2019.9.25', 'public==2019.4.13', 'pycparser==2.20',
                      'regex==2020.2.20', 'requests==2.23.0', 'setupcfg==2019.4.13', 'setuppy-generator==2019.10.24',
                      'six==1.14.0', 'soupsieve==2.0', 'tornado==6.0.4', 'typing-extensions==3.7.4.1',
                      'urllib3==1.25.8', 'values==2019.4.13', 'websocket-client==0.57.0', 'wincertstore==0.2',
                      'wincertstore==0.2', 'write==2019.4.13', 'yarl==1.4.2']
)
