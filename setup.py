'''
Created on Jan 10, 2012

@author: Mike_Edwards
'''
from distutils.core import setup

setup(name='django-savvy',
      version='0.0.1',
      description='Lesson, group, and achievment management educational software for Django',
      long_description=open('README.rst').read(),
      author='Mike Edwards',
      author_email='mike@onearmedman.copm',
      url='http://distlearn.org/',
      license='GPLv3+',
      packages=['savvy', 
                'savvy.lessons',
                'savvy.assemblies',
                'savvy.achievements',
                'savvy.lessons.migrations',
                'savvy.assemblies.migrations',
                'savvy.achievements.migrations'],
      package_data={'savvy.lessons':['templates/lessons/*.html','static/lessons/css/*.css']},
      include_package_data=True,
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Education',
      ]
     )