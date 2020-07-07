from setuptools import setup, find_namespace_packages, find_packages
# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(name='ifscApi',
      version='0.1',
      description='Api for Ifsc',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Harsh Oza',
      author_email='harshoza3636@gmail.com',
      license='MIT',
      install_requires=[
          'flask',
          'flask-restful'
      ],
      url="https://github.com/HarshOza36/ifsc_api",
      download_url='https://github.com/HarshOza36/ifscApi/archive/v_01.tar.gz',
      keywords=['IFSC Code', 'IFSC', 'Bank IFSC Codes'],
      packages=find_packages(),
      include_package_data=True,
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Topic :: Software Development :: Build Tools",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.7",
          "Operating System :: OS Independent",
      ],
      )
