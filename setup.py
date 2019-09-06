from setuptools import setup
setup(name='Evolution',
	version='1.1.1',
	description='Library for apply theories of evolution to modify binary dna.',
	url='https://www.github.com/pmp47/Evolution',
	author='pmp47',
	author_email='phil@zeural.com',
	license='MIT',
	packages=['evolution'],
	install_requires=['dictableobject @ git+https://github.com/pmp47/DictableObject@master#egg=DictableObject==1.1.1','numpyextension @ git+https://github.com/pmp47/NumpyExtension@master#egg=NumpyExtension==1.1.1','numpy==1.17.1'],
	zip_safe=False,
	include_package_data=True,
	python_requires='>=3.6',

	package_data={'': ['data/*.*']}
)
