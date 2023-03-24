from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in wp_integration/__init__.py
from wp_integration import __version__ as version

setup(
	name="wp_integration",
	version=version,
	description="Whatsapp integration for Frappe/ERPNext, using the Whatsapp Cloud API",
	author="Mohamed Abdulsalam",
	author_email="moha2016it@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
