# Copyright 2017 Taylor DeHaan
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(
        name='cmd-tree',
        version='1.0.1',
        author='Taylor DeHaan',
        author_email='tdehaan93@gmail.com',
        url='http://github.com/tdeh/py-tree',
        description='A command line tool for generating text-based representations of file hierarchies.',
        keywords='tree directory files hierarchy',
        license='Apache',
        packages=find_packages(where="src"),
        package_dir={"": "src"},
        entry_points={
          'console_scripts': ['py-tree=fs_tree.command_line:command_line_runner'],
        },
        zip_safe=False,
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
            'Operating System :: POSIX :: Linux',
            'Topic :: Utilities',
        ],
    )
