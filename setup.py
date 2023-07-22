import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ ="0.0.0"

REPO_NAME= "Text-Summarization"
AUTHOR_USER_NAME = "siddhantv45"
SRC_REPO = "Text-Summarization"
AUTHOR_EMAIL= "siddhantv45@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
        description="Text Summarization",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/siddhantv45/Text-Summarization",
    project_urls={
        "Bug Tracker": f"https://github.com/siddhantv45/Text-Summarization/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)

