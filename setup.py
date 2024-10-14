from setuptools import setup, find_packages

setup(
    name='ml-nexus',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy==2.1.1',
        'pandas==2.0.3',
        'scikit-learn==1.3.0',
        'matplotlib==3.7.1',
        'seaborn==0.12.0',
        'pytest==7.3.1',
        'flask==2.3.2',
        'fastapi==0.99.0',
        'uvicorn==0.23.0',
        'docker==6.0.1',
        'requests==2.31.0',
    ]
)
