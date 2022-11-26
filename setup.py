#!/usr/bin/env python
from setuptools import find_namespace_packages, setup

package_name = "dbt-risingwave"
# make sure this always matches dbt/adapters/{adapter}/__version__.py
package_version = "1.3.0"
description = """The RisingWave adapter plugin for dbt"""

setup(
    name=package_name,
    version=package_version,
    description=description,
    long_description=description,
    author="Floris Smit",
    author_email="florissmit10@gmail.com",
    url="https://github.com/florissmit10/dbt-risingwave",
    packages=find_namespace_packages(include=["dbt", "dbt.*"]),
    include_package_data=True,
    install_requires=[
        "dbt-core~=1.3.0.",
    ],
)
