from setuptools import setup

setup(
        name="markdown blog",
        version="0.1",
        long_description="Markdown blogging platform",
        packages=["mdblog"],
        zip_safe=False,
        include_package_data=True,
        install_requires=[
            "celery==4.1.1",
            "Flask==0.12.2",
            "Flask-SQLAlchemy==2.3.2",
            "Flask-WTF==0.14.2"
            ]
)
