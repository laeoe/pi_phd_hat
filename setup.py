from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='pi_phd_hat',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'pi_phd_hat': ['assets/key_samples/*']
    },
    install_requires=required,
    # entry_points={
    #     'console_scripts': [
    #         'my_midi_project=my_midi_project.__main__:main',  # If you have a main script
    #     ],
    # },
    # Additional metadata
    author='Leo Walz',
    author_email='laeoes.spam@gmail.com',
    description='Phd hat project that includes a midi keyboard and a rasberry pi',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/laeoe/pi_phd_hat.git',
    # More metadata
)
