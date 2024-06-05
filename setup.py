from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_discription = f.read()

setup(
    name='mpllegends',
    version='0.0.1',
    author='Jonas Freißmann',
    author_email='jonas.freissmann@hs-flensburg.de',
    description='Customizable standalone matplotlib legends.',
    long_discription_content_type='text/markdown',
    long_discription=long_discription,
    url='https://github.com/jfreissmann/mpllegends',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License'
        ],
    py_modules=['mpllegends'],
    package_dir={'': 'src'},
    python_requires='>=3.9',
    install_requires=['matplotlib>=3.8.0']
)