from importtools import find_packages, setup

setup(
    name='PyGi',
    packages=find_packages(include=['pygi']),
    version='0.1.0',
    description='Python Git/Github Utilities',
    author='DralrinResthal',
    license='MIT',
    install_requires=[
        'GitPython>=3.1.13',
        'PyGithub>=1.54.1',
        'python-dotenv>=0.15.0'
    ],
    setup_requires=['pytest-runner>=5.3.0'],
    test_requires=['pytest>=6.2.2'],
    test_suite='tests',
)