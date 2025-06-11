from setuptools import setup, find_packages

setup(
    name="fsm_mod_n",
    version="1.0.0",
    description="FSM-based mod-N calculator supporting custom alphabets",
    author="Aman Singh",
    author_email="amansingh940330@gmail.com",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "fsm-cli = fsm_mod_n.cli:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
