# GAMS package for Sublime Text 2

Provides syntax highlighting for `.gms` and `.inc` files and shortcuts for running GAMS models.

## Installation

**Using Sublime Package Control** (recommended): If you have installed [Sublime Package Control](http://wbond.net/sublime_packages/package_control), you can easily install the GAMS Language package via the `Package Control: Install Package` menu item (shortcut: **CTRL+SHIFT+P**). Search for `GAMS Language` in the list.

**Without Git:** Download the latest source zip from [github](https://github.com/lolow/sublime-gams/tarball/master) and extract the files to your Sublime Text "Packages" directory, into a new directory named *GAMS*.

**With Git:** Clone the repository in your Sublime Text "Packages" directory:

    git clone git://github.com/lolow/sublime-gams.git GAMS

The "Packages" directory is located at:

* OS X:
    `~/Library/Application Support/Sublime Text 2/Packages/`
* Linux:
    `~/.Sublime Text 2/Packages/`
* Windows:
    `%APPDATA%/Sublime Text 2/Packages/`

You can access it through the menu in `Preferences` > `Browse Packages...`

## GAMS language

The General Algebraic Modeling System (GAMS) is a high-level modeling system for mathematical programming and optimization. It consists of a language compiler and a stable of integrated high-performance solvers. GAMS is tailored for complex, large scale modeling applications, and allows you to build large maintainable models that can be adapted quickly to new situations.

GAMS is the property of GAMS Software GmbH (http://www.gams.com).

## Features

You need _gams_ or _gams.exe_ in your PATH. Please update your environment variable PATH.

To launch gams, open your _file.gms_ and type **CTRL+B** (Build).

Type **CTRL+SHIFT+G** to switch between the code _file.gms_ and the listing _file.lst_.

In the GAMS listing, _file.lst_, type **CTRL+R** (Goto Symbol) to list and jump to the error statements.

## GAMS Comments

In GAMS, by default, block comments are delineated by **$ONTEXT**/**$OFFTEXT**, 
and line comments are started by a star **\***.

This package also adds the comment highlighting for end of line **#** and **//**,
and the inline comments delineated by curly brackets: **{** **}** or in C-style with **/\*\* \*\*/**.

In order to GAMS to process these new comment conventions,
you need to add in your code some of these commands:

	$eolcom //
	$eolcom #
	$inlinecom {}
	$inlinecom /* */

## Support

Any remarks, suggestion about the syntax highlighting have to be adressed to the author `Laurent Drouet`.
