from setuptools import setup, find_packages
import os

# Read the contents of your README file 
this_directory = os.path.dirname(os.path.realpath(__file__))
readme_path = os.path.join(this_directory, "docs", "README.md") 
 
# Read the contents of the README file
with open(readme_path, encoding="utf-8") as f:
    long_description = f.read()

# Get requirements from requirements.txt to a list
with open(os.path.join(this_directory, "requirements.txt"), encoding="utf-8") as f:
    install_requires = f.read().splitlines()
requirements = []
for reqs in install_requires:
    if "--" not in reqs and ":" not in reqs and "#" not in reqs:
        requirements.append(reqs)
# Get version from version file in zenni/version
with open(os.path.join(this_directory, "zenni/version"), encoding="utf-8") as f:
    version = f.read().strip()

setup(
    name="zenni",
    version=version,
    description="An Artificial Intelligence Automation Platform. AI Instruction management from various providers, has an adaptive memory, and a versatile plugin system with many commands including web browsing. Supports many AI providers and models and growing support every day.",
    long_description=long_description,
    long_description_content_type="text/markdown",  # This should match the format of your README
    author="zenni",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=requirements,
)





