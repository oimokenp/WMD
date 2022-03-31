import MeCab
from gensim.models.word2vec import Word2Vec

def mecab_analysis(text):
    tagger = MeCab.Tagger("Ochasen")
    tagger.parse("")
    node = tagger.parseToNode(text)
    out = []

    while node:
        if node.surface != "":
            word_type = node.feature.split(",")[0]
            # if word_type in "名詞":
            out.append(node.surface)
        node = node.next
        if node is None:
            break
    return out

def main():
    model = Word2Vec.load("./shiroyagi/word2vec.gensim.model")

    # text_list1 = ['今日','は','いい','天気です']
    # text_list2 = ['私','は','犬','が','好き','です']
    text_list1 = mecab_analysis('私は猫が好きです')
    text_list2 = mecab_analysis('私は犬が好きです')
    sim_value = model.wv.wmdistance(text_list1,text_list2)
    
    print(text_list1)
    print(text_list2)
    print(sim_value)

if __name__ == '__main__':
    main()