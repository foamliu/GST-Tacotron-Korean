import os
import pickle

from config import train_folder, test_folder, vocab_file, data_file


def get_data(folder):
    samples = []
    dirs = [d for d in os.listdir(folder)]
    for d in dirs:
        folder_path = os.path.join(folder, d)
        tran_file = '{}_003.trans.txt'.format(d)
        tran_file = os.path.join(folder_path, tran_file)
        with open(tran_file, 'r') as file:
            lines = file.readlines()
        for i, line in enumerate(lines):
            tokens = line.strip().split()
            audiopath = tokens[0]
            audiopath = os.path.join(folder_path, '{}.flac'.format(audiopath))
            text = ''.join(tokens[1:])
            for token in text:
                build_vocab(token)
            text = [char2idx[ch] for ch in text]
            samples.append({'audiopath': audiopath, 'text': text})

    return samples


def build_vocab(token):
    global char2idx, idx2char
    if not token in char2idx:
        next_index = len(char2idx)
        char2idx[token] = next_index
        idx2char[next_index] = token


if __name__ == "__main__":
    char2idx = {}
    idx2char = {}

    data = dict()
    data['train'] = get_data(train_folder)
    data['test'] = get_data(test_folder)
    with open(data_file, 'wb') as file:
        pickle.dump(data, file)

    print('num_train: ' + str(len(data['train'])))
    print('num_test: ' + str(len(data['test'])))

    data = dict()
    data['char2idx'] = char2idx
    data['idx2char'] = idx2char
    with open(vocab_file, 'wb') as file:
        pickle.dump(data, file)

    print('vocab_size: ' + str(len(data['char2idx'])))
    print('char2idx: ' + str(char2idx))
