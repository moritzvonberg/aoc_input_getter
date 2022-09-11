import setuptools

setuptools.setup(
    name='aoc_input_getter',
    version='0.1.0',
    author='Moritz von Berg'
    author_email='moritzvonberg@gmail.com',
    description='Gets input for Advent of Code problems',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    include_package_data=True,
    package_data={'': ['data/']}
)