echo [⬇️] Clonig git...
git clone https://github.com/electron/electron-quick-start.git
echo [✅] Cloned Electron Quick Start!
cd electron-quick-start
echo [⬇️] Installing electron...
npm i --save-dev electron
echo [✅] Installed Electron!
echo [⬇️] Installing electron-packager...
npm i --save-dev electron-packager
echo [✅] Installed Electron Packager!
cd ../
echo [ℹ️] Starting Python
python3 main.py