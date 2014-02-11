; A Script-Fu to fill the selection with TV static.

(define (cable-out image drawable)
    (plug-in-randomize-hurl 1 image drawable 70 1 TRUE 0)
    (gimp-desaturate-full drawable 1)
    (gimp-brightness-contrast drawable 0 127)
    (gimp-displays-flush)
)

(script-fu-register
    "cable-out"
    "Cable Out"
    "Fills the selection with TV static-style noise."
    "wohanley"
    "copyright 2013, William O'Hanley"
    "February 11, 2013"
    "RGB*"
    SF-IMAGE "image" 0
    SF-DRAWABLE "drawable" 0
)
(script-fu-menu-register "cable-out" "<Image>/Filters/Noise")
