from setuptools import setup, find_packages

install_requires = [
    'numpy',
    'pytest',
    'scipy',
    'torch',
    'pytorch-lightning',
    'torchdiffeq',
    'torchsde',
    'matplotlib',
    'seaborn',
    'pytorchts',
    'gluonts==0.9.*',
    'wget',
]

with open('README.md', 'r') as f:
    long_description = f.read()

setup(name='tsdiff',
      version='0.2.0',
      description='Time series diffusion',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='',
      author='Marin Bilos',
      author_email='marin.bilos@tum.de',
      packages=find_packages(),
      install_requires=install_requires,
      python_requires='>=3.7',
      zip_safe=False,
)
