sudo apt update
sudo apt-get update
sudo apt upgrade -y
sudo apt install git curl unzip tar make sudo vom wget -y
git clone https://github.com/phi-ra/kg-app.git

sudo apt install python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip install streamlit
