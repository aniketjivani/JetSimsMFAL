There are some `*.cfg` files in here prefixed with Old, they are different versions of roughly the same config for LoFi that we have used earlier, with only minor changes between them (mesh file path, output write frequency etc) - these can be checked with a diff tool like `tkdiff`

For the current jet sims with active learning, we will not use any of these, but rather the LoFi and HiFi template files without the "old" prefix, which now use an inlet BC file rather than specifying a single `MARKER`. Other changes to keywords as may be needed by newer versions of SU2 may also follow.
