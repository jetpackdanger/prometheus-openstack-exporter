import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="prometheus_swift_exporter",
    version="0.0.4",
    author="Jacek Nykis",
    description="Exposes high level OpenStack Swift metrics to Prometheus.",
    license="GPLv3",
    keywords=["prometheus", "openstack", "swift", "exporter"],
    url="https://github.com/jetpackdanger/prometheus-swift-account-exporter",
    scripts=["prometheus-swift-account-exporter"],
    install_requires=["prometheus_client"],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: System :: Networking :: Monitoring",
        "License :: OSI Approved :: "
            "GNU General Public License v3 or later (GPLv3+)",
    ],
)
