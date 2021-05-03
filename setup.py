from fileinput import FileInput
from setuptools import setup, find_namespace_packages
from pathlib import Path


here = Path(__file__).parent.resolve()

requirements = (here / "requirements.txt").read_text(encoding="utf8")
long_description = (here / 'README.md').read_text(encoding='utf-8')


setup(name='synthetic_data',
      description='Synthetic data generation methods with different synthesization methods.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Mithun Ghosh',
      author_email='2018id04605@wilp.bits-pilani.ac.in',
      keywords='data science pysynthetic',
      url='',
      license="",
      python_requires=">=3.6, <3.9",
      packages=find_namespace_packages('pysynthetic'),
      package_dir={'':'pysynthetic'},
      include_package_data=True,
      options={"bdist_wheel": {"universal": True}},
      install_requires=requirements)