from setuptools import find_packages, setup

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="dbmanager",
    version="0.0.1",
    author="yupix",
    author_email="yupi0982@outlook.jp",
    description="sqlalchemyのcommitを楽に行います",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yupix/db-commit",
    packages=find_packages(where='db_manager'),
    package_dir={'': 'db_manager'},
    license="BSL-1.0",
    install_requires=["sqlalchemy"],
    python_requires='>=3.7',
)
