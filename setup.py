import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='minitelebot',  
    version='0.1',
    scripts=['minitelebot'] ,
    author="Deepak Kumar",
    author_email="realPittman@gmail.com",
    description="A Mini lib for Telegram Bot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/realPittman/minitelebot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)