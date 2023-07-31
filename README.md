SuperAGI Alpaca Toolkit

The SuperAGI Alpaca Toolkit provides a set of Python-based tools for interacting with the Alpaca API to execute trading operations. This toolkit is a part of the larger SuperAGI project.

Installation

Before you begin, make sure you have Python 3.7 or later installed.

1. Clone this repository.

git clone <repository-url>

2. Navigate into the cloned repository.

cd superagi_alpaca_toolkit

3. Install the required Python packages.

pip install -r requirements.txt

Usage

The toolkit consists of several Python files, each providing a specific functionality related to trading with the Alpaca API. Here's a brief overview of the main files:

- trader.py: This is the main file that contains the Trader class. The Trader class provides methods to interact with the Alpaca API for various trading operations.

- alpaca_close_trade_tool.py: This file provides a tool to close a trade on Alpaca.

- alpaca_get_day_percent_change_tool.py: This file provides a tool to get the day's percent change for a specific stock.

- alpaca_get_positions_tool.py: This file provides a tool to get the current positions.

For each tool, there's an associated input class in the same file. This class defines the inputs required for the tool.

Contributing

Contributions are welcome! Please read our contributing guidelines to get started.

License

This project is licensed under the terms of the MIT license. See the LICENSE file for the full license text.
 
