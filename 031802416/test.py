import unittest
import project

class MyTest(unittest.TestCase):

    def test_add(txts):
        with open("orig.txt", "r", encoding='utf-8') as fp:
            orig_text = fp.read()
        with open("orig_0.8_add.txt", "r", encoding='utf-8') as fp:
            copy_text = fp.read()
        similarity = project.getText(orig_text, copy_text)
        similarity = round(similarity.similar(), 2)
        print("orig_0.8_add.txt 相似度")
        print(similarity)

    def test_del(txts):
        with open("orig.txt", "r", encoding='utf-8') as fp:
            orig_text = fp.read()
        with open("orig_0.8_del.txt", "r", encoding='utf-8') as fp:
            copy_text = fp.read()
        similarity = project.getText(orig_text, copy_text)
        similarity = round(similarity.similar(), 2)
        print("orig_0.8_del.txt 相似度")
        print(similarity)

    def test_dis_1(txts):
        with open("orig.txt", "r", encoding='utf-8') as fp:
            orig_text = fp.read()
        with open("orig_0.8_dis_1.txt", "r", encoding='utf-8') as fp:
            copy_text = fp.read()
        similarity = project.getText(orig_text, copy_text)
        similarity = round(similarity.similar(), 2)
        print("orig_0.8_dis_1.txt 相似度")
        print(similarity)

    def test_dis_3(txts):
        with open("orig.txt", "r", encoding='utf-8') as fp:
            orig_text = fp.read()
        with open("orig_0.8_dis_3.txt", "r", encoding='utf-8') as fp:
            copy_text = fp.read()
        similarity = project.getText(orig_text, copy_text)
        similarity = round(similarity.similar(), 2)
        print("orig_0.8_dis_3.txt 相似度")
        print(similarity)

    def test_dis_7(txts):
        with open("orig.txt", "r", encoding='utf-8') as fp:
            orig_text = fp.read()
        with open("orig_0.8_dis_7.txt", "r", encoding='utf-8') as fp:
            copy_text = fp.read()
        similarity = project.getText(orig_text, copy_text)
        similarity = round(similarity.similar(), 2)
        print("orig_0.8_dis_7.txt 相似度")
        print(similarity)

    def test_dis_10(txts):
        with open("orig.txt", "r", encoding='utf-8') as fp:
            orig_text = fp.read()
        with open("orig_0.8_dis_10.txt", "r", encoding='utf-8') as fp:
            copy_text = fp.read()
        similarity = project.getText(orig_text, copy_text)
        similarity = round(similarity.similar(), 2)
        print("orig_0.8_dis_10.txt 相似度")
        print(similarity)

    def test_dis_15(txts):
        with open("orig.txt", "r", encoding='utf-8') as fp:
            orig_text = fp.read()
        with open("orig_0.8_dis_15.txt", "r", encoding='utf-8') as fp:
            copy_text = fp.read()
        similarity = project.getText(orig_text, copy_text)
        similarity = round(similarity.similar(), 2)
        print("orig_0.8_dis_15.txt 相似度")
        print(similarity)

    def test_mix(txts):
        with open("orig.txt", "r", encoding='utf-8') as fp:
            orig_text = fp.read()
        with open("orig_0.8_mix.txt", "r", encoding='utf-8') as fp:
            copy_text = fp.read()
        similarity = project.getText(orig_text, copy_text)
        similarity = round(similarity.similar(), 2)
        print("orig_0.8_mix.txt 相似度")
        print(similarity)

    def test_rep(txts):
        with open("orig.txt", "r", encoding='utf-8') as fp:
            orig_text = fp.read()
        with open("orig_0.8_rep.txt", "r", encoding='utf-8') as fp:
            copy_text = fp.read()
        similarity = project.getText(orig_text, copy_text)
        similarity = round(similarity.similar(), 2)
        print("orig_0.8_rep.txt 相似度")
        print(similarity)


if __name__ == '__main__':
    unittest.main()
