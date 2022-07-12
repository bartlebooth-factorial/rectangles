# Introduction

A python turtle game about filling the screen with as many colorful rectangles
as possible before running out of space.

# Installation

Ensure that you have the following dependencies:
* python 3
* turtle

Clone the repository, and run `setup.sh`, which will create the high score
file that the program will look for. Then, run `python3 rectangles.py` to play.

If you would like to play rectangles from any directory, add this function
to your shell rc file:

```sh
rectangles() {
	cd location/of/rectangles/repo;
	python3 rectangles.py;
	cd $OLDPWD;
}
```
# Controls

The game is controlled by left-clicking to draw rectangles.

