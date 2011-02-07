from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='ckanext-deliverance',
      version=version,
      description="CKAN Deliverance Proxy",
      long_description="""Allow using CKAN to proxy CMS content""",
      keywords='ckan plugin cms deliverance proxy content pages',
      author='Open Knowledge Foundation',
      author_email='info@okfn.org',
      url='http://www.okfn.org',
      license='http://www.apache.org/licenses/LICENSE-2.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      namespace_packages=['ckanext'],
      zip_safe=False,
      install_requires=[
          'swiss>=0.3',
          'Deliverance>=0.3'
      ],
      entry_points="""
      # -*- Entry points: -*-
      [ckan.plugins]
      deliverance = ckanext.deliverance:DeliveranceRoutes
      """,
      )
