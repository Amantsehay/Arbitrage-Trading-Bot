Triangular Arbitrage Trading Bot
Overview

This project focuses on developing a triangular arbitrage bot that leverages price differences across three cryptocurrency exchanges. The bot will automate profitable trades by identifying arbitrage opportunities and executing trades based on predefined conditions.
Features (Planned)

    Multi-exchange support: Works with exchanges that integrate with the CCXT library.
    Real-time price monitoring and alerts: Offers both manual and automatic trading options. Users can choose to approve trades manually or allow the bot to trade automatically.
    Automated arbitrage execution: The bot will automatically execute triangular arbitrage trades if the potential profit exceeds a set minimum percentage return.

Getting Started
Prerequisites

    Python 3.8+
    API keys for exchanges (e.g., Binance, Kraken, etc.)

Installation

    Clone the repository:

    bash

git clone https://github.com/Amantsehay/Arbitrage-Trading-Bot.git
cd Arbitrage-Trading-Bot

Install dependencies:

bash

    pip install -r requirements.txt

Project Structure

    main.py: The bot's main entry point.
    config.py: Stores API keys and trading pair configurations.
    utils/: Contains helper scripts and utility functions.

