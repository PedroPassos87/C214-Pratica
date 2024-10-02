from setuptools import setup, find_packages

setup(
    name='C214-Pratica',
    version='0.1.0',
    author='Pedro Henrique',
    author_email='peagacarreira@gmail.com',
    description='Um pacote para testar o uso de gitActions na disciplina DevOps',
    long_description_content_type='text/markdown',
    url='https://github.com/pedropassos07/C214-Pratica',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'wheel',
        'pytest',
    ],
)