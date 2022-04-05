# WMD
とりあえずやってみたのプログラムです。


文書間の類似度を計算するタスクです。  
計算量が多いのが難点。

## 必要なライブラリ
`$ pip install gensim`  
`$ pip install pyemd`

2015年に提案された手法です。  
[1] Kusner, Matt J., et al. “From word embeddings to document distances.” Proceedings of the 32nd International Conference on Machine Learning (ICML 2015). 2015.  
http://jmlr.org/proceedings/papers/v37/kusnerb15.pdf

Word2Vecには「株式会社白ヤギコーポレーション」の学習済み日本語モデルを使用しています。  
https://aial.shiroyagi.co.jp/2017/02/japanese-word2vec-model-builder/
