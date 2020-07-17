import setuptools

setuptools.setup(
    name="helpers",
    version="0.0.1",
    author="Ben Lewis",
    author_email="phyisisblue@gmail.com",
    description="helper functions for project euler problems",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/Phyisis/Problems/tree/master/src/helpers",
    packages= setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "psutil",
        "numpy"
    ],
    python_requires='>=3.8',
)