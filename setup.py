from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='multitaperpy',
      version='0.2.0',
      description='Multitaper Frequency-Domain Analysis in Python',
      long_description=readme(),
      long_description_content_type="text/markdown",
      classifiers=[
        'License :: GNU GPL v 2.0 License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics'
      ],
      url='http://github.com/lootie/multitaperpy',
      keywords='time series spectrum analysis coherence coherency phase',
      author='Charlotte Haley and Christopher Geoga',
      author_email='contact@juliadiffeq.org',
      license='GNU GPL v 2.0',
      packages=['multitaperpy'],
      install_requires=['julia>=0.2'],
      include_package_data=True,
      zip_safe=False)
