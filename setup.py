from setuptools import setup, find_packages

setup(
    name='ru_python',
    version='0.1',
    packages=find_packages(),
    description='Библиотека для написания Python-кода на русском языке',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/ru_python',
    author='Your Name',
    author_email='your.email@example.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='Apache License 2.0',
)
