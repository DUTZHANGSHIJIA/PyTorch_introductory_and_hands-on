import sys
import os
import time

import littleutils


class TextSpliter(object):
    def __init__(self, corpus_path, encoding='utf-8', max_load_word_length=4):
        self.dict = {}
        self.dict2 = {}
        self.max_word_length = 1
        begin_time = time.time()
        print('start load corpus from %s' % corpus_path)
        #加载语料
        with open(corpus_path, 'r', encoding=encoding) as f:
            for l in f:
                l.replace('[', '')
                l.replace(']', '')
                wds = l.strip().split(' ')#1.strip()去除字符串两端的空白字符（包括换行符）
                                            #2.split(' ')将字符串按空格分割成列表
                last_wd = ''
                for i in range(1, len(wds)):    #下标从1开始，因为每行第一个词是标签？
                    try:
                        wd, wtype = wds[i].split('/')
                    except:
                        continue
                    if len(wd) > self.max_word_length or len(wd) == 0 or not wd.isalpha():
                        continue
                    if wd not in self.dict:
                        self.dict[wd] = 0
                        if len(wd) > self.max_word_length:
                            #更新最大词长度
                            self.max_word_length = len(wd)
                            print('max_word_length=%d, word is %s' % (self.max_word_length, wd))
                    self.dict[wd] += 1
                    if last_wd:
                        if last_wd+':'+wd not in self.dict2:
                            self.dict2[last_wd+':'+wd] = 0
                        self.dict2[last_wd+':'+wd] += 1
                    last_wd = wd
                self.words_cnt = 0
                max_c = 0
                for wd in self.dict:
                    self.words_cnt += self.dict[wd]
                    if self.dict[wd] > max_c:
                        max_c = self.dict[wd]
                self.words2_cnt = sum(self.dict2.values())
                print('load corpus finished, %d words in dict and frequency is %d, %d words in dict2 frequency is %d' % (len(self.dict),len(self.dict2), self.words_cnt, self.words2_cnt), 'msg')
                print('%f seconds elapsed' % (time.time()-begin_time), 'msg')

    def split(self, text):
        sentence = ''
        result = ''
        for ch in text:
            if not ch.isalpha():
                result += self.__split__sentence(sentence) + ' ' + ch + ' '
                sentence = ''
            else:
                sentence += ch
        return result.strip(' ')

    def __get_a_split__(self, cur_split, i):
        if i >= len(self.cur_sentence):
            self.split_set.append(cur_split)
            return
        j = min(self.max_word_length, len(self.cur_sentence) - i + 1)
        while j > 0:
            if j == 1 or self.cur_sentence[i:i+j] in self.dict:
                self.__get_a_split__(cur_split + [self.cur_sentence[i:i+j]], i+j)
                if j == 2:
                    break
            j -= 1

    def __get_cnt__(self, dictx, key):
        #获取出现次数
        try:
            return dictx[key] + 1
        except KeyError:
            return 1

    def __get_word_probablity__(self, wd, pioneer=''):
        if pioneer == '':
            return self.__get_cnt__(self.dict, wd) / self.words_cnt
        return self.__get_cnt__(self.dict2, pioneer + ':' + wd) / self.get_cnt(self.dict, pioneer)

    def __calc_probability__(self, sequence):
        probability = 1.0
        pioneer = ''
        for wd in sequence:
            probability *= self.__get_word_probablity__(wd, pioneer)
            pioneer = wd
        return probability

    def __split__sentence(self, sentence):
        if len(sentence) == 0:
            return ''
        self.cur_sentence = sentence.strip()
        self.split_set = []
        self.__get_a_split__([], 0)
        print(sentence + str(len(self.split_set)))
        max_probability = 0.0
        for splitx in self.split_set:
            probability = self.__calc_probability__(splitx)
            print(str(splitx)+' - '+str(probability))
            if probability > max_probability:
                max_probability = probability
                best_split = splitx
        return ' ',join(best_split)

if __name__ == '__main__':
    btime = time.time()
    base_path = os.path.dirname(os.path.realpath(__file__))
    spliter = TextSpliter(os.path.join(base_path, '199801.txt'))
    with open(os.path.join(base_path, 'test.txt'), 'r', encoding='utf-8') as f:
        with open(os.path.join(base_path, 'result.txt'), 'w', encoding='utf-8') as fr:
            for l in f:
                fr.write(spliter.split(l))
    print('time elapsed %f' % (time.time() - btime))