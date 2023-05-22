from setuptools import setup, find_packages

setup(name='tinypulsepy',
      version='0.5.0',
      description='API client for TinyPulse API V1.',
      url='https://github.com/pabloriveracelerity/tinypulsepy/',
      author='Pablo Rivera',
      author_email='privera@celerity.com',
      license='MIT',
      packages=find_packages(),
      install_requires=['requests==2.31.0', 'mock==3.0.5'],
      zip_safe=False,
      download_url="https://github.com/pabloriveracelerity/tinypulsepy/archive/0.2.0.tar.gz",
      keywords=["Tiny Pulse", "Tiny Pulse API", "API", "Celerity"],
      classifiers=[
          "License :: OSI Approved :: MIT License",
          ],
      )
