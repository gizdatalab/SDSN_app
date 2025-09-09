import setuptools


install_requires=[
        "st-annotated-text==4.0.0",
        "markdown==3.4.1",
        "streamlit-aggrid==0.3.4",
        "streamlit_option_menu==0.3.12",
]


setuptools.setup(
        name='appstore',
        version='1.0.2',
        description='Climate Policy Analysis Machine',
        author='Data Service Center GIZ',
        author_email='prashant.singh@giz.de',
        package_dir={"": "src"},
        packages=setuptools.find_packages(where='src'),  
        install_requires=install_requires, #external packages as dependencies
        )
