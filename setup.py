from setuptools import setup, find_packages
setup(
    name = "pullup",
    version = "0.1",
    description = "Resolve pull requests cleanly for git-svn",
    author = "Kyle Conroy",
    author_email = "kyle+pullup@twilio.com",
    url = "http://github.com/derferman/pullup",
    keywords = ["git-svn","git","pull requests"],
    packages = find_packages(),
    entry_points={
        'console_scripts': [
            'pullup = pullup:main',]},
    classifiers = [
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    )
