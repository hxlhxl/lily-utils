from setuptools import setup, find_packages
 
setup(
    name = 'lilyutils',
    version = '0.1',
    keywords = ('lily', 'utils'),
    description = 'lilyzt utils',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
      ],
    license = 'MIT License',
    install_requires = ['requests==2.20.0'],
 
    author = 'hxlhxl',
    author_email = 'huaxiongcool@gmail.com',
    url = 'https://github.com/hxlhxl/lily-utils',
    
    packages = find_packages(),
    platforms = 'any',
)
