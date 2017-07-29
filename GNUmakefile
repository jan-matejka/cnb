.DEFAULT_GOAL := build
CXX ?= c++
CRAMOPTS ?= --shell=/usr/bin/zsh
CRAM_ROOT ?= cram
CRAM_PATH ?= $(CRAM_ROOT)

PREFIX   ?= /usr/local
LIBDIR   ?= $(DESTDIR)$(PREFIX)/lib
BINDIR   ?= $(DESTDIR)$(PREFIX)/bin
MANDIR   ?= $(DESTDIR)$(PREFIX)/man/man1

CHECK_PATH = $(PWD)/$(BROOTDIR)/fakeroot/usr/local/bin:/bin:/usr/bin:/usr/local/bin

BROOTDIR   = _build
BLIBDIR    = $(BROOTDIR)/lib
BBINDIR    = $(BROOTDIR)/bin
BMANDIR    = $(BROOTDIR)/man/man1

DIRS = $(BLIBDIR) $(BBINDIR)

CMDS = $(patsubst src/cnb/%.sh,%,$(wildcard src/cnb/*))
MANS = $(patsubst Documentation/cnb/%.rst,cnb-%.1,$(wildcard Documentation/cnb/*))

BCMDS = $(BBINDIR)/cnb   $(addprefix $(BBINDIR)/cnb-,$(CMDS))
BMANS = $(BMANDIR)/cnb.1 $(addprefix $(BMANDIR)/,$(MANS))

ICMDS = $(BINDIR)/cnb    $(addprefix $(BINDIR)/cnb-,$(CMDS))
IMANS = $(MANDIR)/cnb.1  $(addprefix $(MANDIR)/,$(MANS))

.PHONY: build
build: $(BCMDS) $(BMANS)

$(BBINDIR)/cnb-%: src/cnb/%.sh

	install -m755 -D $< $@

$(BBINDIR)/cnb: src/cnb.sh

	install -m755 -D $< $@

$(BMANDIR):

	install -d $@

$(BMANDIR)/cnb-%.1: Documentation/cnb/%.rst $(BMANDIR)

	rst2man $< $@

$(BMANDIR)/%.1: Documentation/$(subst cnb-,cnb/,%).rst $(BMANDIR)

	rst2man $< $@


.PHONY: install
install: $(ICMDS) $(IMANS)

$(BINDIR)/%: $(BBINDIR)/%

	install -m755 -D $< $@

$(MANDIR)/%: $(BMANDIR)/%

	install -m644 -D $< $@


.PHONY: clean
clean:

	$(RM) -r $(BROOTDIR) $(CRAM_ROOT)/*.t.err


.PHONY: check
check: build

	mkdir -p $(BROOTDIR)/fakeroot
	DESTDIR=$(BROOTDIR)/fakeroot $(MAKE) install
	env -i PATH=$(CHECK_PATH) cram $(CRAMOPTS) $(CRAM_PATH)
