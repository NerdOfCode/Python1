rm -rf Python1
rm -rf AI
shopt -s extglob
git clone https://github.com/NerdOfCode/Python1.git
rm -rf Python1/!(AI) 
mv Python1/AI .
rm -rf Python1
