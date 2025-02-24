from setuptools import setup, find_packages

setup(
    name="StreetFighterRL",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "gym",
        "torch",
        "numpy",
        "opencv-python",
        "stable-baselines3",
        "retro"
    ]
)
