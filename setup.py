import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="solax",
    use_scm_version=True,
    author="Robin Wohlers-Reichel",
    author_email="me@robinwr.com",
    description="solax inverter API client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/japeral/solax",
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        "aiohttp>=3.5.4, <4",
        "voluptuous>=0.11.5",
        "importlib_metadata>=3.6; python_version<'3.10'",
        "typing_extensions>=4.1.0; python_version<'3.11'",
    ],
    setup_requires=[
        "setuptools_scm",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    entry_points={
        "solax.inverter": [
            "x1_boost = solax.inverters.x1_boost:X1Boost",
        ],
    },
)
