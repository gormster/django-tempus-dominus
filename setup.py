from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="django-tempus-dominus",
    version="5.1.2.6.post1",
    description="A Django widget for the Tempus Dominus Bootstrap 4 DateTime picker.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tim Allen",
    author_email="tallen@wharton.upenn.edu",
    url="https://github.com/FlipperPA/django-tempus-dominus",
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=["django"],
)
