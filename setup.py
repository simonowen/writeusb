import os
from setuptools import setup

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename), encoding='utf-8').read()

setup(name='mgtwriteusb',
      version='0.9.2',
      author='Simon Owen',
      author_email='simon@simonowen.com',
      description='Write SAM Coupé disk images to USB floppy drive',
      long_description=read('ReadMe.md'),
      long_description_content_type = 'text/markdown',
      license='MIT',
      keywords='mgt disk sam coupe usb floppy',
      url='https://github.com/simonowen/writeusb',
      packages=['mgtwriteusb'],
      include_package_data=True,
      install_requires=[
          'mgtdisklib',
          'pywin32;platform_system=="Windows"'],
      classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: System :: Filesystems",
        "Environment :: Console",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
      ],
      entry_points={
        "console_scripts":[
            'writeusb=mgtwriteusb.writeusb:main'
        ]
      },
)
