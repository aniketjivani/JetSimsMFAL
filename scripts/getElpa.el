; Following these instructions from Stack Exchange to enable ELPA MELPA etc on Emacs versions less than 26.2? https://emacs.stackexchange.com/a/53142
(require 'package)
(setq package-check-signature nil)
(add-to-list 'load-path "~/.emacs.d/lisp")
(load "gnu-elpa-keyring-update")
(package-refresh-contents)
(setq package-check-signature "allow-unsigned")


