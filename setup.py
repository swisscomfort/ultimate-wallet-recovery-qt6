# setup.py - Ultimate Wallet Recovery Tool Installation Script

from setuptools import setup, find_packages
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="wallet-recovery-ultimate",
    version="3.0.0",
    author="Ultimate Wallet Recovery Team",
    author_email="support@walletrecovery.ultimate",
    description="Ultimate All-in-One Wallet Recovery Tool with AI-powered features",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ultimate-wallet-recovery/wallet-recovery-ultimate",
    project_urls={
        "Bug Tracker": "https://github.com/ultimate-wallet-recovery/wallet-recovery-ultimate/issues",
        "Documentation": "https://docs.walletrecovery.ultimate",
        "Source Code": "https://github.com/ultimate-wallet-recovery/wallet-recovery-ultimate",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business :: Financial",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.11",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.5.0",
            "pytest-cov>=4.1.0",
        ],
        "enterprise": [
            "matplotlib>=3.8.0",
            "plotly>=5.17.0",
            "pandas>=2.1.0",
            "openpyxl>=3.1.0",
            "python-telegram-bot>=20.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "wallet-recovery-ultimate=wallet_recovery_ultimate:main",
        ],
        "gui_scripts": [
            "wallet-recovery-gui=wallet_recovery_ultimate:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.json", "*.md", "*.txt", "assets/*", "docs/*"],
    },
    zip_safe=False,
    keywords=[
        "wallet", "recovery", "cryptocurrency", "bitcoin", "ethereum", 
        "blockchain", "seed", "mnemonic", "bip39", "ai", "security"
    ],
    platforms=["any"],
)

