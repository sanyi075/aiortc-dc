import os.path

import setuptools

root_dir = os.path.abspath(os.path.dirname(__file__))
readme_file = os.path.join(root_dir, 'README.rst')
with open(readme_file, encoding='utf-8') as f:
    long_description = f.read()

install_requires = [
    'aioice>=0.6.13,<0.7.0',
    'attrs',
    'crc32c',
    'cryptography>=2.2',
    'pyee',
    'pylibsrtp>=0.5.6',
    'pyopenssl',
    'websockets>=7.0'
]

setuptools.setup(
    name='aiortc-dc',
    version='0.5.4',
    description='data channel feature only version of aiortc which implements WebRTC and ORTC',
    long_description_content_type="text/markdown",
    long_description=long_description,
    url='https://github.com/ryogrid/aiortc-dc',
    author='Jeremy Lainé and Ryo Kanbayashi',
    author_email='ryo.contact@gmail.com',
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=['aiortcdc', 'aiortcdc.contrib'],
    setup_requires=[],
    install_requires=install_requires,
)
