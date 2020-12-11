"""
Copyright 2020 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import setuptools
import subprocess
from distutils.command.build import build as _build


class build(_build):
  sub_commands = _build.sub_commands + [('CustomCommands', None)]


COMMANDS = [
          #['apt-get', 'install', '-y', 'wget'],
          ['wget', 'https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh'],
          ['bash', './Miniconda3-latest-Linux-x86_64.sh', '-b', '-f', '-p', '/usr/local'],
          ['conda', 'install', '-q', '-y', '-c', 'conda-forge', 'rdkit'],
]

class CustomCommands(setuptools.Command):

  def initialize_options(self):
    pass
  def finalize_options(self):
    pass

  def run_command(self, cmd):
    subprocess.run(cmd, check=True)

  def run(self):
    for cmd in COMMANDS:
      self.run_command(cmd)


setuptools.setup(
    name='bigquery-indexer-worker',
    version='0.0.1',
    description='BigQuery column indexing Google Cloud Dataflow package.',
    install_requires=[], # Other pip packages if needed.
    packages=setuptools.find_packages(),
    cmdclass={
        # Command class instantiated and run during pip install scenarios.
        'build': build,
        # This gets run on each worker.
        'CustomCommands': CustomCommands,
    })

