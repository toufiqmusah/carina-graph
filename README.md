Here’s a brief README for your project:

---

# Carina-Graph v3 Dashboard

This project is a Streamlit-based dashboard for analyzing Uniswap v3 pools using data fetched from The Graph.

## Project Structure

- **`subgraph.py`**: Contains the core logic for querying data from The Graph.
- **`app.py`**: Implements the Streamlit dashboard, allowing users to interact with the data.

## Features

- **Pagination Strategy Selection**: Users can choose between `ShallowStrategy` and `LegacyStrategy` for pagination, affecting how data is queried.
- **Top Pools Analysis**: Displays the top 10 pools by total value locked (USD).
- **Fee Analysis**: Provides an overview of fee tiers, volume, and fees in USD.
- **Comparative Analysis**: Calculates and displays the volume-to-liquidity ratio for a better understanding of pool efficiency.

## Prerequisites

- Python 3.x
- Required Python libraries: `streamlit`, `subgrounds`, `python-dotenv`

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Create a `.env` file in the root directory.
   - Add your API key for The Graph in the `.env` file:
     ```
     API_KEY=your_graph_api_key_here
     ```

4. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

## Usage

- **Select Pagination Strategy:** Use the dropdown to select either `ShallowStrategy` or `LegacyStrategy`.
- **View Top Pools:** The dashboard will display the top pools by total value locked.
- **Analyze Fees:** Examine the fee tiers, volumes, and fees of the top pools.
- **Compare Liquidity:** Analyze the volume-to-liquidity ratio for comparative insights.
