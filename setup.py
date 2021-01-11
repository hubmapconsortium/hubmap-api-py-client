import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("VERSION", "r") as fh:
    version = fh.read()

setuptools.setup(
    name="hubmap-api-py-client",
    version=version,
    install_requires=[
        # Keep in sync with requirements-lower-bound.txt:
        'requests>=2.0.0'
    ],
    # scripts=[],
    author="Chuck McCallum",
    author_email="mccallucc+cells_client@gmail.com",
    description="Client for the HuBMAP Cells API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hubmapconsortium/hubmap-api-py-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # Keep in sync with .travis.yml:
    python_requires='>=3.6',
    # f-strings aren't available in 3.5.
)
