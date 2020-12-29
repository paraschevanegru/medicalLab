from setuptools import setup

setup(
    name="medical_lab",
    version="0.1.0",
    license="MIT",
    author="Balan Alexandru-Eduard, Negru Parascheva",
    author_email="",
    description="Encryption and uploading tool.",
    long_description="",
    packages=["medical_lab"],
    entry_points={"console_scripts": ["medicalgui=medical_lab.__main__:main"]},
    platforms="any",
    classifiers=[
        "Development Status :: 0",
        "Intended Audience :: Education",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7.7",
    ],
    install_requires=["cx_Oracle"],
)