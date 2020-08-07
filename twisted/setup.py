from setuptools import setup


def requirements():
    with open('requirements.txt', 'r') as f:
        return [l.strip() for l in f.readlines()]


version = dict(
    major=0,
    minor=2,
    bugfix=0
)

setup(
    name='ScreamingBunny Utils.Twisted',
    version='{major}.{minor}.{bugfix}'.format(**version),
    package_data={
        'SB_Utils': [
            './sb_utils/*',
        ]
    },
    include_package_data=True,
    install_requires=requirements()
)
