from setuptools import setup, find_packages

setup(
    name="ml-nexus",
    version="0.1.0",
    author="Shilpa Musale",
    author_email="ishishiv3012@gmail.com",
    description="A comprehensive machine learning repository showcasing algorithms from scratch and deployment.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ishi3012/ml-nexus",
    packages=find_packages(),
    install_requires=[
        "numpy==1.23.5",
        "pandas==2.0.3",
        "scikit-learn==1.3.0",
        "matplotlib==3.7.1",
        "seaborn==0.12.0",
        "pytest==7.3.1",
        "flask==2.3.2",
        "fastapi==0.99.0",
        "uvicorn==0.23.0",
        "docker==6.0.1",
        "requests==2.31.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
