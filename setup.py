from setuptools import setup

readme  = open('README.md').read()
history = open('CHANGELOG.md').read()

setup(
    name = 'quantumpy',
    version = '0.3.0',
    description = 'An ultra simple wrapper for the Socialmetrix Quantum API',
    author = 'Gustavo Arjones (originally Gustavo Machado)',
    author_email = 'info@socialmetrix.com',
    url = 'https://github.com/socialmetrix/quantumpy',
    packages = ['quantumpy'],
    install_requires = ['requests >= 0.8', 'six >= 1.6'],
    classifiers = [
		'Development Status :: 2 - Pre-Alpha',
		'Intended Audience :: Developers',
		'Programming Language :: Python',
		'Natural Language :: English',
		'License :: OSI Approved :: Apache Software License',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Topic :: Software Development :: Libraries',
        'Operating System :: OS Independent'
    ]
)
