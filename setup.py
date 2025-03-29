from setuptools import setup, find_packages
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def read_requirements():
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

setup(
    name="martian_crud",
    version="0.1.0",
    description="The Martian CRUD - CI/CD pipeline for automating the build, test" +
                " and deployment of Mission Control CRUD",
    author="Ioanna Vougiatzi",
    author_email="t8220020@aueb.gr",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "martian-compiler=martian_crud.main:main",
        ],
    },
    python_requires=">=3.6",
)
