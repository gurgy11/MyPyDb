import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
	name="MyPyDb_GURGY11",
	version="0.0.1",
	author="Gregory Bockus",
	author_email="gregory.bockus@gmail.com",
	description="A small MySQL database helper package for making databases, tables, and columns.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/gurgy11/"
)