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
        'agents': [
            'config.yaml',
            'config_sample.yaml',
        ],
    },
    install_requires=[
        'click>=8.0.0',
        'requests>=2.31.0',
        'anthropic>=0.40.0',
        'mistralai>=1.0.0',
        'pyyaml>=6.0',
        'pytest>=7.4.0',
        'pytest-asyncio>=0.21.0',
        'importlib-resources; python_version<"3.9"',
    ],
    extras_require={
        'dev': [
            'pytest>=7.4.0',
            'pytest-asyncio>=0.21.0',
            'semgrep>=1.45.0',
            'bandit>=1.7.0',
            'pylint>=3.0.0',
            'mypy>=1.7.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'noseeum = noseeum.cli:main',
        ],
    },
)
