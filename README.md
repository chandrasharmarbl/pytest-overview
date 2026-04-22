# UniStream

UniStream is an asynchronous Python CLI tool that aggregates university data from the [HipoLabs Open API](http://universities.hipolabs.com/search). It efficiently fetches, standardizes, filters, and summarizes university information across multiple countries using modern async capabilities.

## Features

- **Asynchronous Fetching**: Utilizes `httpx` and `asyncio.gather` for blazing-fast, concurrent API requests.
- **Robust Filtering**: Automatically filters out institutions that lack valid websites.
- **Domain Standardization**: Powered by `tldextract` to intelligently strip out subdomains, `http/https`, and `www` prefixes to produce a pristine base domain.
- **Strict TDD Pipeline**: Built from the ground up using 100% strict Test-Driven Development (TDD) resulting in a highly robust test suite.
- **SOLID Architecture**: Designed with decoupled, single-responsibility layers (Models, Clients, Processors, and Orchestrators).

## Getting Started

### Prerequisites
- Python 3.9+
- `pip`

### Installation
1. Clone the repository and navigate into the project directory.
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the project in editable mode along with testing dependencies:
   ```bash
   pip install -e ".[test]"
   ```

## Usage

Run the CLI tool by passing a list of countries you want to query.

```bash
python src/main.py "Canada" "United States" "Mexico" -o summary_report.json
```

**Options:**
- `countries`: A space-separated list of country names. **Note**: Use quotes for multi-word names (e.g., `"United States"`).
- `-o, --output`: The name of the output JSON file. (Default: `report.json`)

### Example Output
```text
Fetching data for 2 countries: Canada, United States...
Fetched 3584 total universities.
Filtering out institutions without websites...
Kept 3491 universities with valid websites.
Standardizing domains and generating report...
Success! Summary report saved to summary_report.json
```

## Running the Test Suite

This project is a showcase of strict Test-Driven Development. To run the tests and view the output:

```bash
# Run all tests with verbosity
pytest -v

# Run the test suite and generate a coverage report
pytest --cov=src
```

## Project Structure

```text
pytest-overview/
├── src/
│   ├── client.py      # Async HTTP client & Error handling
│   ├── main.py        # CLI entry point, orchestrator, and File I/O
│   ├── models.py      # Dataclasses and object instantiation
│   └── processor.py   # Domain cleaning and logic filtering
├── tests/
│   ├── conftest.py    # Pytest fixtures and mock data
│   ├── test_client.py # Mocks httpx to test the API Client
│   ├── test_main.py   # Mocks I/O and orchestration logic
│   ├── test_models.py
│   └── test_processor.py
└── pyproject.toml     # Project metadata and dependencies
```
