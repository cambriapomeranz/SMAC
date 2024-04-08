from setuptools import setup, find_packages

package_name = 'inchworm_control'

setup(
    name=package_name,
    version='0.0.0',
    # packages=[package_name],

    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'motor_controller = inchworm_control.motor_controller:main'
            'step_publisher = inchworm_control.step_publisher:main'            
        ],
    },
)

