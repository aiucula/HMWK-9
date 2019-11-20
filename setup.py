import setuptools

packaging_tutorial/
  Assignment10_pkg/
  setup.py
  LICENSE
  README.md

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aiucula”
    version="0.0.1",
    author="Anthony Iuculano”,
    author_email = “iuculano.anthony@gmail.com",
    description="Clustering the Iris Dataset”,
    long_description=long_description,
    long_description_content_type="Clustering the Iris dataset to determine what classification of Iris a new data point would be”,
    url=" https://github.com/aiucula/HMWK-9",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
