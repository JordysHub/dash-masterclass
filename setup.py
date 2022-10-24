from setuptools import setup, find_packages

setup(name='Dash Masterclass',
      version='1.0.0',
      packages=find_packages(),
         install_requires=[
            'PyYAML',
            'pandas==0.23.3',
            'numpy>=1.14.5'
        ],
)