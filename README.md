# Twitter word embeddings 
This repository contains a description of the Word2vec and FastText Twitter embeddings I have trained.
I wrote [a full blog post](https://fredericgodin.com/research/twitter-word-embeddings/) containing a summary of the results I obtained for PoS tagging and NER.

When used in combination with a Convolutional Neural Network, the FastText embeddings obtain a SOTA results on two different PoS tagging datasets

![alt text](images/pos_tagging_wordvec_fasttext.png "Influence of word embedding for PoS tagging of Twitter microposts using a CNN.")


# Download
The Twitter Word2vec embeddings can be downloaded [here](https://drive.google.com/open?id=1lw5Hr6Xw0G0bMT1ZllrtMqEgCTrM7dzc).
The Twitter FastText embeddings can be downloaded [here](https://drive.google.com/open?id=15zXlbO3bxSYTPt71Fon5-0-oCB8iMSno).

# Citation
If you like this repository and use the embeddings, please cite the following publication:

```
@phdthesis{godin2019,
     title    = {Improving and Interpreting Neural Networks for Word-Level Prediction Tasks in Natural Language Processing},
     school   = {Ghent University, Belgium},
     author   = {Godin, Fr\'{e}deric},
     year     = {2019},
 }
```