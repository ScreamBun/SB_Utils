from setuptools import setup, find_packages

version = dict(
    major=0,
    minor=1,
    bugfix=0
)

setup(
    name='ScreamingBunny Utils',

    version='{major}.{minor}.{bugfix}'.format(**version),

    description='ScreamingBunny Utils',
    # long_description="ScreamingBunny Utils",

    # author='G2-Inc.',
    # author_email='screaming-bunny@g2-inc.com',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utility :: Translation'
    ],

    packages=find_packages(),

    install_requires=[d.replace('\n', '') for d in open('requirements.txt', 'r').readlines()],

    # Python 3.6+ but not 4
    python_requires='>=3.6, <4',

    package_data={
        'SB_Utils': [
            './sb_utils/*',
        ]
    }
)
