python -m pip install virtualenv
python -m virtualenv venv
source venv/Scripts/activate
pip install -r requirements-windows.txt
git clone https://github.com/thtrieu/darkflow.git
cd darkflow
pip install .
cd -
rm -rf darkflow
