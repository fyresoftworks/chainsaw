
![chainsaw(tradermark)](https://github.com/user-attachments/assets/e44ee9dc-a1b3-4641-8e51-e6f7d7152864)

a small, simple command-line tool manager with a growing library of portable tools.

---

## installation

run this single PowerShell command to download and run the installer with admin rights:

irm "https://raw.githubusercontent.com/fyresoftworks/chainsaw/main/installer.bat" `
  | Out-File "$env:TEMP\chainsaw_installer.bat"; Start-Process "$env:TEMP\chainsaw_installer.bat" -Verb RunAs

or

- manually download and run `installer.bat` from the repo, or  
- download `chainsaw.py` and add it to your system PATH yourself

---

## usage example

run any tool available in the chainsaw tools repo by typing:

chainsaw run calculator

replace `calculator` with the name of any supported tool.

---

## notes

- the installer automatically adds chainsaw to your user PATH  
- tools can be Python scripts (`.py`) or Windows executables (`.exe`)  
- tools are fetched and cached locally on demand

---

