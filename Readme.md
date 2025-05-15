# How to Run:

## Step 0 -
### Install uv
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Step 1 -
### Clone the repository
```bash
git clone https://github.com/sourav-bhowal/DAP-LAB-CODES.git
```

## Step 2 -
### Change directory to the desired directory
```bash
cd path/to/your/directory
```

## Step 3 -
### Create & activate the virtual environment and install dependencies
```bash
uv venv
```
```bash
.venv\Scripts\activate
```
```bash
uv pip install -r requirements.txt
```

## Step 4 -
### Run the desired file
```bash
python file_name.py
```