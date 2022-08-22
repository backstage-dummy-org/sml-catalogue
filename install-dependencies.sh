echo "install pipenv"
pip install pipenv
echo "Make virtual environment"
python3 -m venv venv
source venv/bin/activate
echo "Pipenv sync"
pipenv sync --dev
echo "Install terraform"
apt-get install terraform