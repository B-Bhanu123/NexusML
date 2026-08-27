from setuptools import setup, find_packages

setup(
    name="nexusml",
    version="1.0.0",
    description="Enterprise End-to-End Machine Learning & MLOps Platform",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="NexusML Engineering Team",
    author_email="engineering@nexusml.io",
    url="https://github.com/B-Bhanu123/NexusML",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "numpy>=1.22.0",
        "scipy>=1.8.0",
        "pandas>=1.4.0",
        "fastapi>=0.95.0",
        "uvicorn>=0.20.0",
        "pydantic>=2.0.0",
        "pytest>=7.0.0",
        "pyyaml>=6.0"
    ],
    entry_points={
        "console_scripts": [
            "nexusml=nexusml.utilities.cli:main",
        ],
    },
)
