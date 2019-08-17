import fasttext
import os

PATH_TO_MODEL = ''

model = fasttext.load_model(os.path.join(PATH_TO_MODEL,'fasttext_raw.bin'))

word_inv = 'running'
word_oov = 'runnnnnnnnnnnning'

if word_oov in model:
    print('This word is in the vocabulary: {}'.format(word_oov))
else:
    print('This word is NOT in the vocabulary: {}'.format(word_oov))

print('The vector for the the word {} is:'.format(word_oov))
print(model[word_oov])