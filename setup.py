  
from setuptools import find_packages, setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='st1-kafka-api',
    version='0.0.1',
    description='A Python interface for Kafka RESTful APIs.',
    author='Stone Sommers',
    author_email='enots227@gmail.com',
    include_package_data=True,
    packages=find_packages(
        exclude=['tests.*', 'tests']
    ),
    install_requires=[]
)

