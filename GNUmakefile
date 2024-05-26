.DEFAULT_GOAL := build
dram_opts_extra ?=
dramopts ?= -s zsh $(dram_opts_extra)
dram_root ?= dram
dram_path ?= $(dram_root)

prefix   ?= /usr/local
libdir   ?= $(DESTDIR)$(prefix)/lib
bindir   ?= $(DESTDIR)$(prefix)/bin
mandir   ?= $(DESTDIR)$(prefix)/share/man/man1

brootdir   = _build
blibdir    = $(brootdir)/lib
bbindir    = $(brootdir)/bin
bmandir    = $(brootdir)/man/man1

dirs = $(blibdir) $(bbindir)

cmds = $(patsubst src/cnb/%.sh,%,$(wildcard src/cnb/*))
mans = $(patsubst Documentation/cnb/%.rst,cnb-%.1,$(wildcard Documentation/cnb/*))

bcmds = $(bbindir)/cnb   $(addprefix $(bbindir)/cnb-,$(cmds))
bmans = $(bmandir)/cnb.1 $(addprefix $(bmandir)/,$(mans))

icmds = $(bindir)/cnb    $(addprefix $(bindir)/cnb-,$(cmds))
imans = $(mandir)/cnb.1  $(addprefix $(mandir)/,$(mans))

.PHONY: build
build: $(bcmds) $(bmans)

$(bbindir)/cnb-%: src/cnb/%.sh

	install -m755 -D $< $@

$(bbindir)/cnb: src/cnb.sh

	install -m755 -D $< $@

$(bmandir):

	install -d $@

$(bmandir)/cnb-%.1: Documentation/cnb/%.rst $(bmandir)

	rst2man $< $@

$(bmandir)/%.1: Documentation/$(subst cnb-,cnb/,%).rst $(bmandir)

	rst2man $< $@


.PHONY: install
install: $(icmds) $(imans)

$(bindir)/%: $(bbindir)/%

	install -m755 -D $< $@

$(mandir)/%: $(bmandir)/%

	install -m644 -D $< $@


.PHONY: clean
clean:

	$(RM) -r $(brootdir)


.PHONY: check
check: build

	mkdir -p $(brootdir)/fakeroot
	DESTDIR=$(brootdir)/fakeroot $(MAKE) install
	PATH="$(shell pwd)/$(brootdir)/fakeroot$(prefix)/bin:$(PATH)" dram $(dramopts) $(dram_path)

.PHONY: syscheck
syscheck:

	dram $(dramopts) $(dram_path)
