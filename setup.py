from steptools import setup, find_packages

setup(
    name='error_decoder',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'friendly_traceback',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A library to decode error messages into more readable text',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/error_messages/error_decoder',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
