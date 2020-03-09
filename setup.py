from setuptools import setup

setup(name='tinypulsepy',
      version='0.2.0',
      description='API client for TinyPulse API V1.',
      url='https://github.com/pabloriveracelerity/tinypulsepy/',
      author='Pablo Rivera',
      author_email='privera@celerity.com',
      license='MIT',
      packages=['tinypulsepy'],
      install_requires=['requests==2.22.0', 'mock==3.0.5'],
      zip_safe=False,
      download_url="https://github.com/pabloriveracelerity/tinypulsepy/archive/0.2.0.tar.gz",
      keywords=["Tiny Pulse", "Tiny Pulse API", "API", "Celerity"],
      classifiers=[
          "License :: OSI Approved :: MIT License",
          ],
      )
