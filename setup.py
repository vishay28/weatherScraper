import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="weatherScraper",
    package_dir={"": "scraper"},
    packages=setuptools.find_packages(where="scraper"),
    python_requires=">=3.6",
)
