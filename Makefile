TOPLEVEL_LANG := vhdl

SIM := ghdl
SIM_BUILD := build

TOPLEVEL := alu
COCOTB_TEST_MODULES := tests.test_alu

VHDL_SOURCES := $(PWD)/rtl/alu.vhd

include $(shell cocotb-config --makefiles)/Makefile.sim