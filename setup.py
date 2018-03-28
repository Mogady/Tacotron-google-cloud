from setuptools import find_packages
from setuptools import setup
REQUIRED_PACKAGES = [
  'tensorflow-gpu==1.4',
  'inflect==0.2.5',
  'Unidecode==1.0.22',
  'librosa==0.5.1',
  'tqdm==4.11.2',
  'matplotlib==2.0.2',
  'falcon==1.2.0',
  'numpy==1.13.0',
  'scipy==0.19.0'
  
]
setup(name='trainer',
      version='0.1',
      install_requires=REQUIRED_PACKAGES,
      include_package_data=True,
      description='blah',
      packages=find_packages()
)
