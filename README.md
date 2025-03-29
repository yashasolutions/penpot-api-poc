# Penpot API Proof of Concept

This is a proof of concept (POC) for interacting with the Penpot API using Python. 
The POC demonstrates how to read data from a file and make API requests to the Penpot API and list the text component of the file.

## Prerequisites

- Python installed on your machine
- A Penpot account and API token

## Setup

1. Clone this repository to your local machine.

2. Create a virtual environment (optional but recommended) and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # For Unix/Linux
   venv\Scripts\activate.bat  # For Windows
   ```

3. Install the required dependencies by running the following command in the project directory:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and provide the following environment variables:
   ```
   PENPOT_URL=<your_penpot_api_url>
   PENPOT_TOKEN=<your_penpot_api_token>
   ```
   Replace `<your_penpot_api_url>` with the URL of the Penpot API and `<your_penpot_api_token>` with your Penpot API token.

## Usage

   ```
   python penpot.py
   ```
   
## Results

   [](./var/screenshot.png)
   

## Documentation

For more information on the Penpot API and its usage, refer to the official documentation:
[https://design.penpot.app/api/_doc?type=js](https://design.penpot.app/api/_doc?type=js)

## License

This POC is released under the [MIT License](LICENSE).

Feel free to modify and adapt the code to suit your specific requirements.
