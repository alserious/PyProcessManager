import setuptools

setuptools.setup(
    name="pyProcessManager",
    version="0.0.1",
    author="alserious",
    author_email="seriousalsir@gmail.com",
    maintainer="alserious",
    maintainer_email="seriousalsir@gmail.com",
    url="https://github.com/alserious/process_manager",
    download_url="https://github.com/alserious/process_manager/releases",
    description="py process manager",
    long_description="py process manager",
    python_requires="2.7, 3.6, 3.7, 3.8, 3.9, 3.10",
    classifiers=[
        "Programming Language :: Python :: 2.7, 3.6, 3.7, 3.8, 3.9, 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Linux",
    ],
    platforms=["Linux"],
    keywords=["py process manager"],
    license="MIT License",
    packages=setuptools.find_packages(),
    install_requires=["psutil==5.9.1"],
    zip_safe=False,
)
