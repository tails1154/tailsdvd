# tailsdvd
A DVD burner in python
## Instructions
you NEED a linux device. This WILL NOT work on windows unless the SLIGHT chance it works under WSL.
but anyway, this is what we have tested it on:
1. Arch Linux
Now, let's get to using this!
1. run `git clone https://github.com/tails1154/tailsdvd/tailsdvd.git` in your terminal
2. `cd tailsdvd`
3. `./installer.sh`
4. We HAVE NOT tested this on DEBIAN (or debian based devices) but you need
1. `mkisofs`
and
2. `cdrecord`
If you want to run it again without using `installer.sh` (to install the deps)
1. `cd src`
2. `python3 tailsdvd.py`
## Windows Support
I have no plans for windows support in the near future. If you want to add it, feel free to open a PR!