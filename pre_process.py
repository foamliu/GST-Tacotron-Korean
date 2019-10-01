import os
import pickle

from config import train_folder, test_folder, vocab_file


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
            tokens = line.strip().split(sep=' ', maxsplit=2)
            audiopath = tokens[0]
            audiopath = os.path.join(folder_path, '{}.flac'.format(audiopath))
            text = tokens[1]
            samples.append('{}|{}\n'.format(audiopath, text))
            print(audiopath)
            print(text)

    return samples

    # for i, line in enumerate(lines):
    #     tokens = line.strip().split()
    #     audiopath = 'data/km_kh_male/wavs/{}.wav'.format(tokens[0])
    #     text = ''.join(tokens[1:])
    #     for token in text:
    #         build_vocab(token)
    #
    #
    # valid_ids = random.sample(range(len(samples)), 100)
    # train = []
    # valid = []
    # for id in range(len(samples)):
    #     sample = samples[id]
    #     if id in valid_ids:
    #         valid.append(sample)
    #     else:
    #         train.append(sample)
    #
    # ensure_folder('filelists')
    # print('num_train: ' + str(len(train)))
    # print('num_valid: ' + str(len(valid)))


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
    data['char2idx'] = char2idx
    data['idx2char'] = idx2char

    with open(vocab_file, 'wb') as file:
        pickle.dump(data, file)

    data = dict()
    data['train'] = get_data(train_folder)
    data['test'] = get_data(test_folder)

    print('vocab_size: ' + str(len(data['char2idx'])))
    print('char2idx: ' + str(char2idx))
