## Table of contents
* [General info](#general-info)
* [Introduction](#introduction)
* [Technologies](#technologies)
* [Download](#download)
* [Run](#run)
* [Roadmap](#roadmap)

## General info
8-bit RGB (also known as 3-3-2 bit RGB and 8-8-4 bit RGB)

The 3-3-2 bit RGB use 3 bits for each of the red and green color components, and 2 bits for the blue component, due to the eyes having lesser sensitivity to blue. This results in an 8×8×4 = 256-color palette

This palette is used by

* The MSX2 series of personal computers.
* Palette 4 of the IBM PGC (palette 2 gives 2-3-3 bit RGB and palette 3 gives 3-2-3 bit RGB).
* Enterprise Computer.
* Vector-06C, a home computer from the USSR.
* VGA built-in output of the Digilent Inc. NEXYS 2, NEXYS 3 and BASYS2 FPGA boards.
* The Uzebox gaming console
* SGI Indy 8-bit XL graphics
* The Tiki 100 personal computer (only 16 colors can be displayed simultaneously)
* Wear OS smartwatches with ambient displays (only 16 colors can be displayed simultaneously)

Source: https://en.wikipedia.org/wiki/List_of_monochrome_and_RGB_color_formats

## Introduction

This is an education project, so it isn't for commercial use. It isn't only about taking a course from the internet when learning programming, so I created this project to try python in practice. That would be great if my program was useful to someone! In creating my program, I used external sources such as the most popular "Stack Overflow" or, more generally, the Internet. Hence, if you decide to copy my code, you can do whatever you like with it. As I said from the begin, project was created only for education and to learn Python programming.

## Technologies
Project is create with:
* Vscode: _1.67.2_
* Python version: _3.10.4_ 
* Pillow (PIL Fork): _9.2.0_
* Tkinter Tk GUI toolkit: _0.1.0_

## Download

The RGB332 (8-bit RGB) converter program in python.
To run it you just need download project to your machine. To do that please use link below:

```
$ git clone https://github.com/Applegammer/rgb332converter-python-education.git
```
## Run

To run is required: 
* Python version: _3.x.x (recommended 3.10.4)_ 
* Pillow library: _9.2.0 or higher_
* tkinter library: _0.1.0_

**Linux:**
```
$ python ./converter_rgb332.py
```
**OR**
```
$ python3 ./converter_rgb332.py
```
**Windows:**
```
$ py converter_rgb332.py
```
## Roadmap

Basically information about project roadmap, what steps I want realize on the project

### First release with new features
* ~~Create basic interface for program (non-GUI)~~
* ~~Having a choice to load an image from your computer~~
* ~~Having a choice to save your output to file, anywhere you want on your computer~~
* ~~Fix small bugs~~
* Support for most popular images extension formats (eg. ~~PNG~~, JPG, BMP, GIF)
### Build basic GUI
* Create a GUI for program to make much better user-friendly
### Extra feature
* ~~Built app for Windows (Support)~~ 
* Add function to draw/convert image form 24-bit to 8-bit 
