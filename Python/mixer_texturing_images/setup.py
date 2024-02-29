from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mixer-texturing-images",
    version="1.0.0",
    author="Your Name",
    author_email="harmonia251251@gmail.com",
    description="A Python package for blending textures onto images and applying transformations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/your-project",
    project_urls={
        "Bug Tracker": "https://github.com/your-username/your-project/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "opencv-python",
        "matplotlib",
        "requests",
    ],
)
