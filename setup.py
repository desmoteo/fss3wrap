from distutils.core import setup
setup(
  name = 'fss3wrap',
  packages = ['fss3wrap'],
  version = '0.1',
  license='MIT',
  description = 'A python class to wrap fs and fs-s3fs (WIP)',
  author = 'Carlo Perassi',
  author_email = 'carlo.perassi@kiwifarm.it',
  url = 'https://github.com/carlok/fss3wrap',
  download_url = 'https://github.com/carlok/fss3wrap/archive/v_01.tar.gz',
  keywords = ['fs', 's3', 'wrapper'],
  install_requires=[
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',  # "3 - Alpha", "4 - Beta", "5 - Production/Stable"
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
  ],
)

install_requires=[
    'fs',
    'fs-s3fs',
],