N_LEFT_CONTEXT = 7
N_RIGHT_CONTEXT = 7
N_INPUT_FRAME = N_LEFT_CONTEXT + N_RIGHT_CONTEXT + 1
WIDTH = N_INPUT_FRAME
HEIGHT = 40

# timit
# NUM_CLASS = 1944

# rm
# NUM_CLASS = 1504

# wsj
# NUM_CLASS = 3480

# libri tri5b
# NUM_CLASS = 4162

# libri tri6b
NUM_CLASS = 5704

INPUT_DIM = WIDTH * HEIGHT
OUTPUT_DIM = NUM_CLASS


