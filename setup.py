from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
        name='gxconfig',  # package name
        version='0.0.1',  # version
        description="A Global config tools created by gawainx",
        author='gawainx',
        author_email='liangyi@bupt.edu.cn',
        install_requires=['toml'],
        long_description=long_description,
        long_description_content_type="text/markdown",
        classifiers=[
            "Programming Language :: Python :: 3.7",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        packages=setuptools.find_packages(),
)
