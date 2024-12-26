# neovide-fix.py

This python utility fixes the main problem of neovide.
Before fix:
❯ neovide <file_to_edit>
Opens another window of neovide, but your terminal is still there,
even if u try to close terminal your neovide will be closed too
(because it's runned by terminal)
With my fix:
❯ neovide <file_to_edit>
Closes terminal, opens neovide, after you close nevide,
you can see your terminal opened in the directory you were in,
before closing it.
![Check this video to get into it](./.github/202412260407.mp4)

## Contents

- [Installation 󰇚](#installation)

## Installation

- **Arch Linux**

```
sudo pacman -S python-psutil
git clone https://github.com/Kur9an5kiy/neovide-fix.py.git
```

- **Ubuntu**

```
sudo apt-install python-psutil
git clone https://github.com/Kur9an5kiy/neovide-fix.py.git
```
