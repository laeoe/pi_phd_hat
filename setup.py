from setuptools import setup, find_packages

setup(
    name='pi_phd_hat',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'mido', 
        'numpy',
        'pyaudio',
        'wave',
        'concurrent',
        'scipy',  
    ],
    # entry_points={
    #     'console_scripts': [
    #         'my_midi_project=my_midi_project.__main__:main',  # If you have a main script
    #     ],
    # },
    # Additional metadata
    author='Leo Walz',
    author_email='your.email@example.com',
    description='Phd hat project that includes a midi keyboard and a rasberry pi',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/laeoe/pi_phd_hat.git',
    # More metadata
)
