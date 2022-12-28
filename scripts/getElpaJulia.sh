#!/bin/bash

# create personal elisp lib dir
mkdir -p ~/.emacs.d/lisp

# move keyring update file to elisp lib dir
cp gnu-elpa-keyring-update.el ~/.emacs.d/lisp

# run keyring update
emacs --script getElpa.el

# create .emacs file 
FILE=~/.emacs
if test -f "$FILE"; then
    echo "$FILE exists."
else
    touch $FILE
    echo "(require 'package)
(add-to-list 'package-archives '(\"melpa\" . \"https://melpa.org/packages/\") t)
;; Comment/uncomment this line to enable MELPA Stable if desired.  See package-archive-priorities
;; and package-pinned-packages. Most users will not need or want to do this.
;;(add-to-list 'package-archives '(\"melpa-stable\" . \"https://stable.melpa.org/packages/\") t)
(package-initialize)" >> $FILE
fi

# get julia mode emacs
cd $HOME
git clone https://github.com/JuliaEditorSupport/julia-emacs.git

echo "(add-to-list 'load-path \"$HOME/julia-emacs\")
(require 'julia-mode)" >> $FILE
						
