# Tacotron 2

A PyTorch implementation of Tacotron2, described in [Natural TTS Synthesis By Conditioning Wavenet On Mel Spectrogram Predictions](https://arxiv.org/pdf/1712.05884.pdf), an end-to-end text-to-speech(TTS) neural network architecture, which directly converts character text sequence to speech.

## Dataset

[Zeroth-Korean](http://www.openslr.org/40/) contains transcriebed audio data for Korean. There are 51.6 hours transcribed Korean audio for training data (22,263 utterances, 105 people, 3000 sentences) and 1.2 hours transcribed Korean audio for testing data (457 utterances, 10 people)..

## Dependency

- Python 3.5.2
- PyTorch 1.0.0

## Usage
### Data Pre-processing
Extract zeroth_korean.tar.gz:
```bash
$ python extract.py
```

Pro-process training & test data:
```bash
$ python pre_process.py
```

### Train
```bash
$ python train.py
```

If you want to visualize during training, run in your terminal:
```bash
$ tensorboard --logdir runs
```

### Demo
Generate mel-spectrogram for text "강판사는심문시간이길어질것으로보고오후한시육분부터한시간동안휴정을선언하기도했다"
```bash
$ python demo.py
```
![image](https://github.com/foamliu/GST-Tacotron-Korean/raw/master/images/mel_spec.jpg)
