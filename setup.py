import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="static-code-checker-app",
    version="1.0.0",
    description="Test code against each other for classes",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/gadzygadz/CodeChecker",
    author="Jake Gadaleta",
    author_email="jake.gads@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["SRC"],
    include_package_data=True,
    install_requires= [],
    entry_points={
        "console_scripts": [
            "code_checker=code_checker.__main__:main",
        ]
    },
)