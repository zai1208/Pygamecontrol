import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Pygame-control", # Replace with your own username
    version="0.0.1",
    author="Zain Khan",
    author_email="zainkh1432@outlook.com",
    description="Some code to be able to control pygame objects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zai1208/Pygamecontrol",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
