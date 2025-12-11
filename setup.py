from setuptools import setup, find_packages

setup(
    name='noseeum',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'noseeum': [
            'data/*.json',
            'homoglyph_registry.json',
            'nfkc_map.json',
            'config.json',
        ],
    },
    install_requires=[
        'click',
        'requests',
        'importlib-resources; python_version<"3.9"',
    ],
    extras_require={
        'dev': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'noseeum = noseeum.cli:main',
        ],
    },
)
