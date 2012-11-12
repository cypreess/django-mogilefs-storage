from distutils.core import setup

setup(
    name='django-mogilefs-storage',
    version='0.2.1',
    packages=['mogilefs_storage'],
    url='https://github.com/cypreess/django-mogilefs-storage',
    license='MIT',
    author='Krzysztof Dorosz',
    author_email='cypreess@gmail.com',
    description='Django MogileFS file backend storage using pymogile client',
    install_requires=['django'],
    dependency_links=['git+https://github.com/insom/pymogile.git@2d47f017e4adc0b283aadb2312f7d434b39e59b4'],
)
