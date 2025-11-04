#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="linux-user-manager",
    version="1.0.0",
    description="A user-friendly command-line tool for managing Linux users",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "typing;python_version<'3.5'"
    ],
    entry_points={
        'console_scripts': [
            'linux-user-manager=user_manager:main',
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: System :: Systems Administration",
    ],
    python_requires=">=3.6",
)