from setuptools import setup, find_packages

setup(
    name='nbdt',
    version='0.1',
    author='Subhankar Panda',
    author_email='subhankarpanda556@example.com',
    description='nbdt library for recommending authors, papers, and journals',
    packages=find_packages(),
    install_requires=[
        'arxiv',
        'pandas',
    ],
)

