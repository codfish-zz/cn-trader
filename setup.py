#!/usr/bin/env python
# coding=utf-8
# Copyright 2020-present, BigFish (huui1998@163.com).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from codecs import open
from os import path
from setuptools import setup, find_packages

basedir = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(basedir, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="cn-trader",
    version="1.0.1",
    url="https://github.com/codfish-zz/cn-trader",
    license=" Apache-2.0",
    author="BigFish",
    author_email="huui1998@163.com",
    description="Back testing system for China market",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["trading", "development"],
    platforms="any",
    packages=find_packages(exclude=["docs", "docs2", "static", "samples"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "akshare",
        "backtrader",
        "matplotlib",
        "prompt-toolkit",
        "rich",
    ],
    classifiers=[
        # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Software Development",
        "Topic :: Office/Business :: Financial",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": ["cn-trader-ui=cn_trader.ui:main"],
    },
)
