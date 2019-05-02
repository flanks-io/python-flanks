import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Flanks Client",
    version="0.0.1",
    author="Flanks Team",
    author_email="hello@flanks.io",
    description="Small client for FlanksAPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/flanks-io/python-flanks",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)