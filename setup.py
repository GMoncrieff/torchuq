from setuptools import setup, find_packages

setup(
    name="torchuq",
    version="0.1",
    packages=find_packages(),    
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'torch ',
        'pandas',
        'torchvision ',
        'seaborn',
        'h5py',
        'scikit-learn',
        ],
)
