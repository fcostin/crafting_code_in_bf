# get abfc from https://github.com/fcostin/abfc_hs
MACRO_TO_BF := ./bin/abfc

sorted_key_list.bf:	sorted_key_list.py
	cat $^ | $(MACRO_TO_BF) > $@
