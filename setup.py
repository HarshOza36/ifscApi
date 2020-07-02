from setuptools import setup,find_namespace_packages,find_packages
setup(name='ifscApi',
      version='0.0.1',
      description='Api for Ifsc',
      author='harsh',
      author_email='harshoza3636@gmail.com',
      license='MIT',
      install_requires=[
          'flask',
          'flask-restful'
      ],url="https://github.com/ceddlyburge/python_world",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
  )
#       packages=find_namespace_packages(include=['ifscApi.*']),
#       zip_safe=False)
# ['ifscApi']
