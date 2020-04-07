from setuptools import setup, find_packages

setup(
    name="tableauweb_sniffer-chazeon",
    version="0.0.1",
    author="Chazeon",
    author_email="chazeon@gmail.com",
    description="Tools and gears for scraping websites created with Tableau",
    url="https://github.com/chazeon/tableauweb-sniffer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'munch'
    ],
    python_requires='>=3.6',
)