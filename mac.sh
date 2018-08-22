pip3 install --user virtualenv
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements-mac.txt
git clone https://github.com/thtrieu/darkflow.git
cd darkflow
pip install .
cd -
rm -rf darkflow