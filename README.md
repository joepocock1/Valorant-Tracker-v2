# JP Valorant Tracker v2

A desktop application built with Python and CustomTkinter to track Valorant player stats, ranks, match history, and leaderboards using the [HenrikDev API](https://henrikdev.xyz/).

---

## Features

- Search Valorant players by name, tag, and region
- Display current rank with local rank icons
- Show recent match history (last 5 matches)
- View regional leaderboards (top 10 players)
- Dark mode UI with a clean tabbed interface

---

## Project Structure

VALORANT-TRACKER-V2/
├── .venv/ # Python virtual environment (ignored by git)
├── assets/ # Rank images and other static assets
├── .env.example # Template for environment variables
├── main.py # Main application entry point
├── requirements.txt # Python dependencies
├── tracker.ico # App icon
└── README.md # This file

---

## Getting Started

Follow these instructions to get the app running locally.

### Prerequisites

- Python 3.8 or higher
- Git (optional, for cloning the repo)
- An API key from HenrikDev (see below)

---

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/VALORANT-TRACKER-V2.git
cd VALORANT-TRACKER-V2
Create and activate a virtual environment

bash
python -m venv .venv

# Windows
.\.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
Install dependencies

bash
pip install -r requirements.txt
Setup environment variables

Copy .env.example to .env:

bash
cp .env.example .env
Open .env and replace the placeholder with your actual HenrikDev API key:

env
HENRIK_API_KEY=your_real_api_key_here
Important: Do NOT commit your .env file. It contains sensitive information.

Usage
Run the application:

bash
python main.py
Use the Home tab to search for a player by name, tag, and region.

View detailed rank info in the Rank tab.

Check recent match history in the Match History tab.

Browse the top 10 leaderboard players in the Leaderboard tab.

Obtaining an API Key
To use this app, you need an API key from HenrikDev:

Visit https://henrikdev.xyz/

Register or log in.

Generate a Valorant API key.

Place your key in the .env file as shown above.

Contributing
Contributions are welcome! Feel free to:

Open issues for bugs or feature requests.

Submit pull requests with improvements or fixes.

Please ensure your code follows Python best practices and includes clear commit messages.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Thanks to HenrikDev for providing the Valorant API.

Built with CustomTkinter for a modern UI.

If you have any questions or need help, please open an issue or contact me directly.

Happy tracking! 🎯
