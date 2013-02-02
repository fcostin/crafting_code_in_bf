# 1  BYTE FOR BLOCK TYPE
# 15 BYTES FOR DATA
# N BYTES FOR COMPILER-ALLOCATED STACK VARIABLES

# this number of N=48 is totally magical.
# it needs to be at least 16 + the max width of the stack the
# macro compiler decides this program needs when compiled to
# brainfuck (yes, utter madness)

DEF_MACRO('cursor_right')(
    GROW_STACK(INT_CONSTANT(48))
)

DEF_MACRO('cursor_left')(
    SHRINK_STACK(INT_CONSTANT(48))
)

DEF_MACRO('clear_block')(
    CLEAR(STACK_ADDRESS(-1)),
    CLEAR(STACK_ADDRESS(-2)),
    CLEAR(STACK_ADDRESS(-3)),
    CLEAR(STACK_ADDRESS(-4)),
    CLEAR(STACK_ADDRESS(-5)),
    CLEAR(STACK_ADDRESS(-6)),
    CLEAR(STACK_ADDRESS(-7)),
    CLEAR(STACK_ADDRESS(-8)),
    CLEAR(STACK_ADDRESS(-9)),
    CLEAR(STACK_ADDRESS(-10)),
    CLEAR(STACK_ADDRESS(-11)),
    CLEAR(STACK_ADDRESS(-12)),
    CLEAR(STACK_ADDRESS(-13)),
    CLEAR(STACK_ADDRESS(-14)),
    CLEAR(STACK_ADDRESS(-15)),
    CLEAR(STACK_ADDRESS(-16)),
)

DEF_MACRO('is_not_equal', 'const', 'src', 'dst')(
    COPY('src', 'dst'),
    CONSTANT_SUB('const', 'dst'),
)

DEF_MACRO('is_not_equal_stack', 'left', 'right', 'dst')(
    COPY('right', 'dst'),
    STACK_SUB('left', 'dst'),
)

DEF_MACRO('set_true', 'x')(
    CLEAR('x'),
    CONSTANT_ADD(INT_CONSTANT(1), 'x'),
)

DEF_MACRO('is_equal', 'const', 'src', 'dst')(
    LOCAL('temp'),
    COPY('src', 'temp'),
    CONSTANT_SUB('const', 'temp'),
    LOGICAL_NOT('temp', 'dst'),
)


DEF_MACRO('set_block_type_free')(
    CLEAR(STACK_ADDRESS(-16)),
)

DEF_MACRO('set_block_type_start')(
    CLEAR(STACK_ADDRESS(-16)),
    CONSTANT_ADD(INT_CONSTANT(1), STACK_ADDRESS(-16)),
)

DEF_MACRO('set_block_type_end')(
    CLEAR(STACK_ADDRESS(-16)),
    CONSTANT_ADD(INT_CONSTANT(2), STACK_ADDRESS(-16)),
)

DEF_MACRO('set_block_type_data')(
    CLEAR(STACK_ADDRESS(-16)),
    CONSTANT_ADD(INT_CONSTANT(3), STACK_ADDRESS(-16)),
)

DEF_MACRO('get_block_type_free', 'x')(
    CALL('is_equal', INT_CONSTANT(0), STACK_ADDRESS(-16), 'x'),
)

DEF_MACRO('get_block_type_start', 'x')(
    CALL('is_equal', INT_CONSTANT(1), STACK_ADDRESS(-16), 'x'),
)

DEF_MACRO('get_block_type_end', 'x')(
    CALL('is_equal', INT_CONSTANT(2), STACK_ADDRESS(-16), 'x'),
)

DEF_MACRO('get_block_type_data', 'x')(
    CALL('is_equal', INT_CONSTANT(3), STACK_ADDRESS(-16), 'x'),
)


DEF_MACRO('write_data_char', 'c', 'i')(
    # you may note that this is not a very high-level language
    LOCAL('x'),
    CALL('is_equal', INT_CONSTANT(1), 'i', 'x'),
    IF('x')(
        COPY('c', STACK_ADDRESS(-1)),
    ),
    CALL('is_equal', INT_CONSTANT(2), 'i', 'x'),
    IF('x')(
        COPY('c', STACK_ADDRESS(-2)),
    ),
    CALL('is_equal', INT_CONSTANT(3), 'i', 'x'),
    IF('x')(
        COPY('c', STACK_ADDRESS(-3)),
    ),
    CALL('is_equal', INT_CONSTANT(4), 'i', 'x'),
    IF('x')(
        COPY('c', STACK_ADDRESS(-4)),
    ),
    CALL('is_equal', INT_CONSTANT(5), 'i', 'x'),
    IF('x')(
        COPY('c', STACK_ADDRESS(-5)),
    ),
    CALL('is_equal', INT_CONSTANT(6), 'i', 'x'),
    IF('x')(
        COPY('c', STACK_ADDRESS(-6)),
    ),
    CALL('is_equal', INT_CONSTANT(7), 'i', 'x'),
    IF('x')(
        COPY('c', STACK_ADDRESS(-7)),
    ),
    CALL('is_equal', INT_CONSTANT(8), 'i', 'x'),
    IF('x')(
        COPY('c', STACK_ADDRESS(-8)),
    ),
    CALL('is_equal', INT_CONSTANT(9), 'i', 'x'),
    IF('x')(
        COPY('c', STACK_ADDRESS(-9)),
    ),
    CALL('is_equal', INT_CONSTANT(10), 'i', 'x'),
    IF('x')(
        COPY('c', STACK_ADDRESS(-10)),
    ),
    CALL('is_equal', INT_CONSTANT(11), 'i', 'x'),
    IF('x')(
        COPY('c', STACK_ADDRESS(-11)),
    ),
    CALL('is_equal', INT_CONSTANT(12), 'i', 'x'),
    IF('x')(
        COPY('c', STACK_ADDRESS(-12)),
    ),
    CALL('is_equal', INT_CONSTANT(13), 'i', 'x'),
    IF('x')(
        COPY('c', STACK_ADDRESS(-13)),
    ),
    CALL('is_equal', INT_CONSTANT(14), 'i', 'x'),
    IF('x')(
        COPY('c', STACK_ADDRESS(-14)),
    ),
    CALL('is_equal', INT_CONSTANT(15), 'i', 'x'),
    IF('x')(
        COPY('c', STACK_ADDRESS(-15)),
    ),
)

DEF_MACRO('get_data_char', 'i', 'out')(
    LOCAL('x'),
    CALL('is_equal', INT_CONSTANT(1), 'i', 'x'),
    IF('x')(
        COPY(STACK_ADDRESS(-1), 'out')
    ),
    CALL('is_equal', INT_CONSTANT(2), 'i', 'x'),
    IF('x')(
        COPY(STACK_ADDRESS(-2), 'out')
    ),
    CALL('is_equal', INT_CONSTANT(3), 'i', 'x'),
    IF('x')(
        COPY(STACK_ADDRESS(-3), 'out')
    ),
    CALL('is_equal', INT_CONSTANT(4), 'i', 'x'),
    IF('x')(
        COPY(STACK_ADDRESS(-4), 'out')
    ),
    CALL('is_equal', INT_CONSTANT(5), 'i', 'x'),
    IF('x')(
        COPY(STACK_ADDRESS(-5), 'out')
    ),
    CALL('is_equal', INT_CONSTANT(6), 'i', 'x'),
    IF('x')(
        COPY(STACK_ADDRESS(-6), 'out')
    ),
    CALL('is_equal', INT_CONSTANT(7), 'i', 'x'),
    IF('x')(
        COPY(STACK_ADDRESS(-7), 'out')
    ),
    CALL('is_equal', INT_CONSTANT(8), 'i', 'x'),
    IF('x')(
        COPY(STACK_ADDRESS(-8), 'out')
    ),
    CALL('is_equal', INT_CONSTANT(9), 'i', 'x'),
    IF('x')(
        COPY(STACK_ADDRESS(-9), 'out')
    ),
    CALL('is_equal', INT_CONSTANT(10), 'i', 'x'),
    IF('x')(
        COPY(STACK_ADDRESS(-10), 'out')
    ),
    CALL('is_equal', INT_CONSTANT(11), 'i', 'x'),
    IF('x')(
        COPY(STACK_ADDRESS(-11), 'out')
    ),
    CALL('is_equal', INT_CONSTANT(12), 'i', 'x'),
    IF('x')(
        COPY(STACK_ADDRESS(-12), 'out')
    ),
    CALL('is_equal', INT_CONSTANT(13), 'i', 'x'),
    IF('x')(
        COPY(STACK_ADDRESS(-13), 'out')
    ),
    CALL('is_equal', INT_CONSTANT(14), 'i', 'x'),
    IF('x')(
        COPY(STACK_ADDRESS(-14), 'out')
    ),
    CALL('is_equal', INT_CONSTANT(15), 'i', 'x'),
    IF('x')(
        COPY(STACK_ADDRESS(-15), 'out')
    ),
)


DEF_MACRO('read_words')(
    GROW_STACK(INT_CONSTANT(16)),
    CALL('clear_block'),
    CALL('set_block_type_start'),
    CALL('cursor_right'),
    LOCAL('got_input'),
    CALL('set_true', 'got_input'),
    LOCAL('c'),
    WHILE('got_input')(
        CALL('clear_block'),
        CALL('set_block_type_data'),
        # read word into data buffer
        LOCAL('got_word'),
        CALL('set_true', 'got_word'),
        LOCAL('n_chars'),
        CLEAR('n_chars'),
        LOCAL('inside_key'),
        CALL('set_true', 'inside_key'),
        WHILE('got_word')(
            CLEAR('c'),
            GET_CHAR('c'),
            LOCAL('is_space'),
            LOCAL('is_newline'),
            LOCAL('end_of_word'),
            CLEAR('end_of_word'),
            LOCAL('is_key_value_delimiter'),
            CALL('is_equal', CHAR_CONSTANT(' '), 'c', 'is_space'),
            CALL('is_equal', CHAR_CONSTANT('\n'), 'c', 'is_newline'),
            CALL('is_equal', CHAR_CONSTANT(':'), 'c', 'is_key_value_delimiter'),
            IF('is_key_value_delimiter')(
                CLEAR('inside_key'),
            ),
            LOGICAL_OR('is_space', 'is_newline', 'end_of_word'),
            # support a couple of EOF conventions
            LOCAL('is_zero'),
            LOGICAL_NOT('c', 'is_zero'),
            LOCAL('is_eof'),
            CALL('is_equal', INT_CONSTANT(255), 'c', 'is_eof'),
            LOCAL('eof'),
            LOGICAL_OR('is_zero', 'is_eof', 'eof'),
            IF('eof')(
                CALL('set_true', 'end_of_word'),
                CLEAR('got_input'),
            ),
            IF('end_of_word')(
                CLEAR('got_word'),
            ),
            IF('got_word')(
                IF('inside_key')(
                    CONSTANT_ADD(INT_CONSTANT(1), 'n_chars'),
                    CALL('write_data_char', 'c', 'n_chars'),
                )
            ),
        ),
        LOCAL('non_blank'),
        COPY('n_chars', 'non_blank'),
        IF('non_blank')(
            # pad rest of fixed-width string with 0s
            CLEAR('c'),
            LOCAL('unfilled_word'),
            CALL('is_not_equal', INT_CONSTANT(15), 'n_chars', 'unfilled_word'),
            WHILE('unfilled_word')(
                CONSTANT_ADD(INT_CONSTANT(1), 'n_chars'),
                CALL('write_data_char', 'c', 'n_chars'),
                CALL('is_not_equal', INT_CONSTANT(15), 'n_chars', 'unfilled_word'),
            ),
            CALL('cursor_right'),
        )
    ),
    CALL('clear_block'),
    CALL('set_block_type_end'),
)

DEF_MACRO('rewind_to_start')(
    LOCAL('is_start'),
    LOCAL('is_not_start'),
    CALL('get_block_type_start', 'is_start'),
    LOGICAL_NOT('is_start', 'is_not_start'),
    WHILE('is_not_start')(
        CALL('cursor_left'),
        CALL('get_block_type_start', 'is_start'),
        LOGICAL_NOT('is_start', 'is_not_start'),
    )
)

DEF_MACRO('print_block_tag')(
    LOCAL('match'),
    CLEAR('match'),
    CALL('get_block_type_free', 'match'),
    IF('match')(
        PUT_STRING_CONSTANT(STRING_CONSTANT('F')),
    ),
    CLEAR('match'),
    CALL('get_block_type_start', 'match'),
    IF('match')(
        PUT_STRING_CONSTANT(STRING_CONSTANT('S')),
    ),
    CLEAR('match'),
    CALL('get_block_type_end', 'match'),
    IF('match')(
        PUT_STRING_CONSTANT(STRING_CONSTANT('E')),
    ),
    CLEAR('match'),
    CALL('get_block_type_data', 'match'),
    IF('match')(
        PUT_STRING_CONSTANT(STRING_CONSTANT('D')),
    ),
)

DEF_MACRO('print_data_block')(
    LOCAL('c'),
    COPY(STACK_ADDRESS(-1), 'c'),
    IF('c')(
        PUT_CHAR('c'),
    ),
    COPY(STACK_ADDRESS(-2), 'c'),
    IF('c')(
        PUT_CHAR('c'),
    ),
    COPY(STACK_ADDRESS(-3), 'c'),
    IF('c')(
        PUT_CHAR('c'),
    ),
    COPY(STACK_ADDRESS(-4), 'c'),
    IF('c')(
        PUT_CHAR('c'),
    ),
    COPY(STACK_ADDRESS(-5), 'c'),
    IF('c')(
        PUT_CHAR('c'),
    ),
    COPY(STACK_ADDRESS(-6), 'c'),
    IF('c')(
        PUT_CHAR('c'),
    ),
    COPY(STACK_ADDRESS(-7), 'c'),
    IF('c')(
        PUT_CHAR('c'),
    ),
    COPY(STACK_ADDRESS(-8), 'c'),
    IF('c')(
        PUT_CHAR('c'),
    ),
    COPY(STACK_ADDRESS(-9), 'c'),
    IF('c')(
        PUT_CHAR('c'),
    ),
    COPY(STACK_ADDRESS(-10), 'c'),
    IF('c')(
        PUT_CHAR('c'),
    ),
    COPY(STACK_ADDRESS(-11), 'c'),
    IF('c')(
        PUT_CHAR('c'),
    ),
    COPY(STACK_ADDRESS(-12), 'c'),
    IF('c')(
        PUT_CHAR('c'),
    ),
    COPY(STACK_ADDRESS(-13), 'c'),
    IF('c')(
        PUT_CHAR('c'),
    ),
    COPY(STACK_ADDRESS(-14), 'c'),
    IF('c')(
        PUT_CHAR('c'),
    ),
    COPY(STACK_ADDRESS(-15), 'c'),
    IF('c')(
        PUT_CHAR('c'),
    ),
)

DEF_MACRO('print_all_blocks')(
    CALL('rewind_to_start'),
    LOCAL('got_blocks'),
    CALL('set_true', 'got_blocks'),
    WHILE('got_blocks')(
        CALL('print_block_tag'),
        LOCAL('tmp'),
        CALL('get_block_type_data', 'tmp'),
        IF('tmp')(
            PUT_STRING_CONSTANT(STRING_CONSTANT('{')),
            CALL('print_data_block'),
            PUT_STRING_CONSTANT(STRING_CONSTANT('}')),
        ),
        PUT_STRING_CONSTANT(STRING_CONSTANT(';')),
        CALL('get_block_type_end', 'tmp'),
        LOGICAL_NOT('tmp', 'got_blocks'),
        IF('got_blocks')(
            CALL('cursor_right'),
        ),
    ),
    PUT_STRING_CONSTANT(STRING_CONSTANT('\n')),
)

DEF_MACRO('debug_print_all_blocks')(
    #CALL('print_all_blocks'), # uncomment this for debugging output
)

DEF_MACRO('get_prev_block_type_data', 'x')(
    CALL('cursor_left'),
    CALL('get_block_type_data', 'x'),
    CALL('cursor_right'),
)

DEF_MACRO('get_prev_block_type_free', 'x')(
    CALL('cursor_left'),
    CALL('get_block_type_free', 'x'),
    CALL('cursor_right'),
)

DEF_MACRO('char_greater_than', 'a', 'b', 'result')(
    LOCAL('x'),
    LOCAL('y'),
    COPY('a', 'x'),
    COPY('b', 'y'),
    LOCAL('temp'),
    LOGICAL_AND('x', 'y', 'temp'),
    WHILE('temp')(
        CONSTANT_SUB(INT_CONSTANT(1), 'x'),
        CONSTANT_SUB(INT_CONSTANT(1), 'y'),
        LOGICAL_AND('x', 'y', 'temp'),
    ),
    COPY('x', 'result'),
)

DEF_MACRO('compare_data_blocks', 'out_compare')(
    # out_compare : 0 means eq; 1 means lt; 2 means gt
    CLEAR('out_compare'),
    LOCAL('i'),
    CLEAR('i'),
    CONSTANT_ADD(INT_CONSTANT(1), 'i'),
    LOCAL('x'),
    LOCAL('y'),
    LOCAL('working'),
    CALL('set_true', 'working'),
    WHILE('working')(
        CALL('cursor_left'),
        CALL('get_data_char', 'i', 'x'),
        CALL('cursor_right'),
        CALL('get_data_char', 'i', 'y'),
        LOCAL('neq'),
        CALL('is_not_equal_stack', 'x', 'y', 'neq'),
        IF('neq')(
            LOCAL('gt'),
            CALL('char_greater_than', 'x', 'y', 'gt'),
            CONSTANT_ADD(INT_CONSTANT(1), 'out_compare'),
            IF('gt')(
                CONSTANT_ADD(INT_CONSTANT(1), 'out_compare'),
            ),
            CLEAR('working'),
        ),
        IF('working')(
            CONSTANT_ADD(INT_CONSTANT(1), 'i'),
            CALL('is_not_equal', INT_CONSTANT(16), 'i', 'working'),
        ),
    )
)

DEF_MACRO('data_block_less_than', 'out')(
    LOCAL('temp'),
    CALL('compare_data_blocks', 'temp'),
    CALL('is_equal', INT_CONSTANT(1), 'temp', 'out'),
)

DEF_MACRO('data_block_greater_than', 'out')(
    LOCAL('temp'),
    CALL('compare_data_blocks', 'temp'),
    CALL('is_equal', INT_CONSTANT(2), 'temp', 'out'),
)

DEF_MACRO('data_block_equal', 'out')(
    LOCAL('temp'),
    CALL('compare_data_blocks', 'temp'),
    CALL('is_equal', INT_CONSTANT(0), 'temp', 'out'),
)

DEF_MACRO('swap_data_blocks')(
    LOCAL('i'),
    CLEAR('i'),
    CONSTANT_ADD(INT_CONSTANT(1), 'i'),
    LOCAL('x'),
    LOCAL('y'),
    LOCAL('working'),
    CALL('set_true', 'working'),
    WHILE('working')(
        CALL('get_data_char', 'i', 'y'),
        CALL('cursor_left'),
        CALL('get_data_char', 'i', 'x'),
        CALL('write_data_char', 'y', 'i'),
        CALL('cursor_right'),
        CALL('write_data_char', 'x', 'i'),
        CONSTANT_ADD(INT_CONSTANT(1), 'i'),
        CALL('is_not_equal', INT_CONSTANT(16), 'i', 'working'),
    )
)

DEF_MACRO('bubble_sort')(
    LOCAL('working'),
    CALL('set_true', 'working'),
    WHILE('working')(
        CALL('debug_print_all_blocks'),
        LOCAL('no_swaps'),
        CALL('set_true', 'no_swaps'),
        CALL('rewind_to_start'),
        LOCAL('got_blocks'),
        CALL('set_true', 'got_blocks'),
        WHILE('got_blocks')(
            LOCAL('match'),
            CALL('get_block_type_data', 'match'),
            IF('match')(
                LOCAL('match2'),
                CALL('get_prev_block_type_data', 'match2'),
                IF('match2')(
                    LOCAL('should_swap'),
                    CALL('data_block_greater_than', 'should_swap'),
                    IF('should_swap')(
                        CALL('swap_data_blocks'),
                        CLEAR('no_swaps'),
                    ),
                ),
            ),
            CALL('get_block_type_end', 'match'),
            LOGICAL_NOT('match', 'got_blocks'),
            IF('got_blocks')(
                CALL('cursor_right'),
            ),
        ),
        IF('no_swaps')(
            CLEAR('working'),
        ),
    )
)


DEF_MACRO('merge_duplicates')(
    LOCAL('working'),
    CALL('set_true', 'working'),
    WHILE('working')(
        CALL('debug_print_all_blocks'),
        LOCAL('no_merges'),
        CALL('set_true', 'no_merges'),
        CALL('rewind_to_start'),
        LOCAL('got_blocks'),
        CALL('set_true', 'got_blocks'),
        # pass 0: look for first merge
        WHILE('got_blocks')(
            LOCAL('match'),
            CALL('get_block_type_data', 'match'),
            IF('match')(
                LOCAL('match2'),
                CALL('get_prev_block_type_data', 'match2'),
                IF('match2')(
                    LOCAL('should_merge'),
                    CALL('data_block_equal', 'should_merge'),
                    IF('should_merge')(
                        CALL('clear_block'),
                        CLEAR('no_merges'),
                    ),
                ),
            ),
            CALL('get_block_type_end', 'match'),
            LOGICAL_NOT('match', 'got_blocks'),
            LOCAL('temp'),
            LOGICAL_AND('got_blocks', 'no_merges', 'temp'),
            COPY('temp', 'got_blocks'),
            IF('got_blocks')(
                CALL('cursor_right'),
            ),
        ),

        # pass 1: compact
        CALL('set_true', 'got_blocks'),
        WHILE('got_blocks')(
            LOCAL('hit_end'),
            CALL('get_block_type_end', 'hit_end'),
            LOCAL('is_free'),
            CALL('get_prev_block_type_free', 'is_free'),
            IF('is_free')(
                # swap blocks including tag
                LOCAL('block_type'),
                COPY(STACK_ADDRESS(-16), 'block_type'),
                CALL('cursor_left'),
                COPY('block_type', STACK_ADDRESS(-16)),
                CALL('cursor_right'),
                CALL('set_block_type_free'),
                CALL('swap_data_blocks'),
            ),
            LOGICAL_NOT('hit_end', 'got_blocks'),
            IF('got_blocks')(
                CALL('cursor_right'),
            ),
        ),

        IF('no_merges')(
            CLEAR('working'),
        ),
    )
)

DEF_MACRO('write_words')(
    CALL('rewind_to_start'),
    LOCAL('got_blocks'),
    CALL('set_true', 'got_blocks'),
    LOCAL('not_first'),
    CLEAR('not_first'),
    WHILE('got_blocks')(
        LOCAL('tmp'),
        CALL('get_block_type_data', 'tmp'),
        IF('tmp')(
            IF('not_first')(
                PUT_STRING_CONSTANT(STRING_CONSTANT(', ')),
            ),
            CALL('print_data_block'),
            CALL('set_true', 'not_first'),
        ),
        CALL('get_block_type_end', 'tmp'),
        LOGICAL_NOT('tmp', 'got_blocks'),
        IF('got_blocks')(
            CALL('cursor_right'),
        ),
    ),
    LOCAL('no_words_there'),
    LOGICAL_NOT('not_first', 'no_words_there'),
    IF('no_words_there')( #bf-ing thing sucks
        PUT_STRING_CONSTANT(STRING_CONSTANT('<none>')),
    ),
    PUT_STRING_CONSTANT(STRING_CONSTANT('\n')),
)

DEF_MACRO('main')(
    CALL('read_words'),
    CALL('bubble_sort'),
    CALL('merge_duplicates'),
    CALL('write_words'),
)

