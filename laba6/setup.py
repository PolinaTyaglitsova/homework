from setuptools import setup, find_packages

setup(
    name = "laba6",
    version = "0.1",
    author = "Полина Тяглицова",
    author_email = "polinka.nya_nya@mail.ru",
    description = "Проект содержит в себе  функции для решения Лаборотрной работы №2",
    packages = find_packages(),
    install_requires = [
        "requests >= 2.20.0",
        "numpy >= 1.18.0"
    ],
    entry_points = {
        "console_scripts": [
            "my_project = my_project.main:main",
        ],
    },
)