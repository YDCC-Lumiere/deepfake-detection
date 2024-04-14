# deepfake-detection
## Dataset:
https://www.kaggle.com/datasets/huynhngotrungtruc/faceswap-thesis
## Feature generator:
- FAFI (Landmark)
- MSR
## Feature extractor:
- ViT: Vision Transformer
- ResNet
- MobileNet
## Run train/test
Setup enviroment
```
pip install -r requirements.txt
pip install .
```
Train
```
python src/test.py -c configs/train.yml
```
Test
```
python src/test.py -c configs/test.yml
```
## Start API demo
Setup enviroment
```
pip install -r requirements.txt
pip install .
```
Start
```
python demo/api.py
```
