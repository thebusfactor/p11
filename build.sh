cd ..
rm -rf Bus-Factor-Release
mkdir Bus-Factor-Release
mkdir Bus-Factor-Release/src
mkdir Bus-Factor-Release/cfg
mkdir Bus-Factor-Release/venv
mkdir Bus-Factor-Release/bin

cp -r Bus-Factor/src Bus-Factor-Release
cp -r Bus-Factor/cfg Bus-Factor-Release
cp -r Bus-Factor/venv Bus-Factor-Release
cp -r Bus-Factor/bin Bus-Factor-Release
cp Bus-Factor/run.sh Bus-Factor-Release
