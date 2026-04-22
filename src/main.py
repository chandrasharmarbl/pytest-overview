import asyncio
import argparse
import json
from typing import List
from src.client import ApiClient
from src.models import University
from src.processor import Processor, DomainUtils

async def fetch_all_countries(countries: List[str]) -> List[University]:
    """
    Fetches universities for multiple countries concurrently.
    Flattens the results into a single list of University objects.
    """
    # Create a list of awaitable tasks for each country
    tasks = [ApiClient.fetch_universities(country) for country in countries]
    
    # Run them concurrently
    results = await asyncio.gather(*tasks)
    
    # We flatten it into a single list
    flattened_results = [uni for sublist in results for uni in sublist]
    return flattened_results

def _generate_report_data(universities: List[University]) -> List[dict]:
    """
    Transforms a list of University objects into a list of dictionaries suitable for JSON reporting.
    Standardizes the domain for each entry.
    """
    report = []
    for uni in universities:
        clean_domain = DomainUtils.clean(uni.web_pages[0])
        report.append({
            "name": uni.name,
            "country": uni.country,
            "clean_domain": clean_domain,
            "original_urls": uni.web_pages
        })
    return report

def _save_report(report_data: List[dict], output_file: str) -> None:
    """
    Saves the report data to a JSON file.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, indent=2, ensure_ascii=False)

async def run_cli(countries: List[str], output_file: str):
    print(f"Fetching data for {len(countries)} countries: {', '.join(countries)}...")
    universities = await fetch_all_countries(countries)
    print(f"Fetched {len(universities)} total universities.")
    
    print("Filtering out institutions without websites...")
    valid_universities = Processor.filter_valid(universities)
    print(f"Kept {len(valid_universities)} universities with valid websites.")
    
    print("Standardizing domains and generating report...")
    report_data = _generate_report_data(valid_universities)
    
    _save_report(report_data, output_file)
    
    print(f"Success! Summary report saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="UniStream: Asynchronous University Data Aggregator")
    parser.add_argument("countries", nargs="+", help="List of countries to fetch (e.g. 'Canada' 'United States')")
    parser.add_argument("-o", "--output", default="report.json", help="Output JSON file name (default: report.json)")
    
    args = parser.parse_args()
    
    try:
        # Start the asyncio event loop
        asyncio.run(run_cli(args.countries, args.output))
    except Exception as e:
        print(f"Fatal Error: {e}")

if __name__ == "__main__":
    main()
