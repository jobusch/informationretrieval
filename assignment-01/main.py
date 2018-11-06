#! /usr/bin/python
# -*- coding: utf-8 -*-


"""Rank sentences based on cosine similarity and a query."""


from argparse import ArgumentParser
import numpy as np


def get_sentences(file_path):
    """Return a list of sentences from a file."""
    with open(file_path, encoding='utf-8') as hfile:
        return hfile.read().splitlines()


def get_top_k_words(sentences, k):
    """Return the k most frequent words as a list."""
    for word in sentencs:
        if word in words:
            words[word] +=1
        else:
            words[word] =1
    return sorted(words, key=words.get, reverse=True)[:k]


def encode(sentence, vocabulary):
    """Return a vector encoding the sentence."""
    mydict = {}
    for i in vocabulary:
        mydict[i]=0
    for word in sentence:
        if word in mydict:
            mydict[word] +=1
    return np.asarray(mydict.values())


def get_top_l_sentences(sentences, query, vocabulary, l):
    """
    For every sentence in "sentences", calculate the similarity to the query.
    Sort the sentences by their similarities to the query.

    Return the top-l most similar sentences as a list of tuples of the form
    (similarity, sentence).
    """
    l = []
    for sen in sentences:
        sim = cosine_sim(encode(sen), encode(query))
        l.append((sim,sen))
    
    return sorted(l, key=lambda tup: tup[0], reverse=True)[:l]


def cosine_sim(u, v):
    """Return the cosine similarity of u and v."""
    
    return np.dot(u,v) / np.linalg.norm(u) * np.linalg.norm(v)


def main():
    arg_parser = ArgumentParser()
    arg_parser.add_argument('INPUT_FILE', help='An input file containing sentences, one per line')
    arg_parser.add_argument('QUERY', help='The query sentence')
    arg_parser.add_argument('-k', type=int, default=1000,
                            help='How many of the most frequent words to consider')
    arg_parser.add_argument('-l', type=int, default=10, help='How many sentences to return')
    args = arg_parser.parse_args()

    sentences = get_sentences(args.INPUT_FILE)
    top_k_words = get_top_k_words(sentences, args.k)
    query = args.QUERY.lower()

    print('using vocabulary: {}\n'.format(top_k_words))
    print('using query: {}\n'.format(query))

    # suppress numpy's "divide by 0" warning.
    # this is fine since we consider a zero-vector to be dissimilar to other vectors
    with np.errstate(invalid='ignore'):
        result = get_top_l_sentences(sentences, query, top_k_words, args.l)

    print('result:')
    for sim, sentence in result:
        print('{:.5f}\t{}'.format(sim, sentence))


if __name__ == '__main__':
    main()
