# Importing setuptools package for packaging Python projects
import setuptools

# Reading the contents of README.md file into a variable called long_description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Defining the version of the package
__version__ = "0.0.0"

# Defining metadata for the package
REPO_NAME = "End_to_end_ml"
AUTHOR_USER_NAME = "atharva"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "atharvapatil000@gmail.com"  # Corrected missing opening quote

# Setting up package using setuptools
setuptools.setup(
    # Package name
    name=SRC_REPO,
    # Package version
    version=__version__,
    # Author name
    author=AUTHOR_USER_NAME,
    # Author email
    author_email=AUTHOR_EMAIL,
    # Short package description
    description="A small python package for ml app",
    # Long package description
    long_description=long_description,
    # Indicating that long description is in markdown format
    long_description_content="text/markdown",  # Corrected quotation marks
    # URL of the package homepage
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    # URLs for project-related pages like the bug tracker
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    # Specifying package directory
    package_dir={"": "src"},
    # Automatically finding packages within the 'src' directory
    packages=setuptools.find_packages(where="src")
)
