from setuptools import setup
setup(name='ifscApi',
      version='0.1',
      description='Api for Ifsc',
      url='#',
      author='harsh',
      author_email='harshoza36@gmail.com',
      license='MIT',
      install_requires=[
          'flask',
          'flask-restful'
      ],
      packages=find_namespace_packages(include=['mynamespace.*']),
      zip_safe=False)
['ifscApi']
