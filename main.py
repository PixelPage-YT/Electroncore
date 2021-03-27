import json
import os
print("[❌] Removing README.md...")
os.remove("electron-quick-start/README.md")
with open("electron-quick-start/package.json", "r") as file:
    package = json.load(file)
print("[*️⃣] Rewriting Package.")
package["scripts"]["dist"] = "electron-packager ./ exampleapp --platform=win32 --icon=icon.icns"
print("[ℹ️] Build type set to win32")
with open("electron-quick-start/package.json", "w") as file:
    json.dump(package, file)
print("[✅] Rewrited Package!")
print("[✔️] Done!")
