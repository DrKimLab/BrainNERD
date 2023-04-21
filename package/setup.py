from setuptools import setup, find_packages

setup(
    name='BrainNerd',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy==1.20.2',
        'pandas==1.2.4',
        'matplotlib==3.4.2'
    ],
    extras_require={
        'dev': [
            'pytest==6.2.4',
            'flake8==3.9.2'
        ]
    }
)
