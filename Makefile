sorted_key_list.bf:	sorted_key_list.py
	cat $^ | $(MACRO_TO_BF) > $@
