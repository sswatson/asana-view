
from setuptools import setup

setup(name='asana-view',
      version='0.1',
      description='View Asana Events across Workspaces',
      url='http://github.com/sswatson/asana-view',
      author='Samuel S. Watson',
      author_email='samuel.s.watson@gmail.com',
      license='MIT',
      packages=['asanaview'],
      install_requires = [
            'asana',
      ],
      include_package_data=True,
      zip_safe=False)