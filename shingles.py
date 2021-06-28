# -*- coding: UTF-8 -*-
import random
MAXGENPRIMEINDEX = 20
MINGENPRIMTINDEX = 5
 
def gen_prime(index):
    D = {}
    q = 2
    gen_index = 0
    while True:
        if q not in D:
            gen_index += 1
            if gen_index == index:
                return q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
 
 
def readfile(filename):
    with open(filename) as f:
        text = f.read().replace('\n', ' ')

    with open(filename) as f:
        count = sum(1 for _ in f)

    mas_text = []
    FILE = open(filename)
    for i in FILE:
      if i.strip() != '{' and i.strip() != '}':
        mas_text.append(i.strip())
    return [text,count,mas_text]
 
 
def canonize(source):
    source = source.replace(":",'')
    source = source.replace("{",'')
    source = source.replace("}",'')
    stop_symbols = "\n"
    return ([x for x in [y.strip(stop_symbols) for y in source.lower().split()]])

def gen_hash():
    prime = gen_prime(random.randint(MINGENPRIMTINDEX, MAXGENPRIMEINDEX))
    base = random.randint(prime, 2*prime)
    return (base, prime)
 
def prepare_hashes(count):
    return [gen_hash() for i in range(count)]
 
def calc_hash(shingle, func):
    s = ''.join(shingle)
    base, prime = func
    value = 0
    for i in range(len(s)):
        value += ord(s[i])*pow(base, i) % prime
    return value
 
def calc_shingles(text, size, hashes,count_hesh):
    matrix = []
    for i in range(len(text) - (size - 1)):
        shignle = [x for x in text[i:i + size]]
        matrix.append([calc_hash(shignle, func) for func in hashes])
    transposed = list(map(list, zip(*matrix)))
    #print(transposed)
    return [min(transposed[i]) for i in range(count_hesh)]
 
 
def compare_shingles(shingles1, shingles2,count_hesh):
    same = 0.0
    for h1, h2, i in zip(shingles1, shingles2,range(0,count_hesh)):
        if h1 == h2:
            same += 1.0
    return same / count_hesh

def get_shingles(t1,t2):
    start_text1,len_text1,mas_text1 = readfile(t1)
    text1 = canonize(start_text1)
    #print(text1)
    start_text2,len_text2,mas_text2 = readfile(t2)
    text2 = canonize(start_text2)
    
    #print(mas_text1)
    count_hesh = min(len_text1,len_text2)
    hashes = prepare_hashes(count_hesh)
 
    shingles1 = calc_shingles(text1, 2, hashes,count_hesh)
    shingles2 = calc_shingles(text2, 2, hashes,count_hesh)
    
    com_shin = compare_shingles(shingles1, shingles2,count_hesh)
    print ("shingles compare: ", com_shin)

    mas_text_text1 = []
    mas_text_text2 = []
    if com_shin >= 0.4:
      for i in range(0,len(mas_text1)-4):
        for g in range(i-3, i+3):
          if g < len(mas_text2):
            t1 = canonize(mas_text1[i])
            t2 = canonize(mas_text2[g])
          else:
            break

          hs = 84
          h = prepare_hashes(hs)
          try:
            shin1 = calc_shingles(t1,2,h,hs)
            shin2 = calc_shingles(t2,2,h,hs)
          except:
            continue
          c_s = compare_shingles(shin1,shin2,hs)

          if c_s > 0.3 and c_s < 0.8:
            mas_text_text1.append(mas_text1[i])
            mas_text_text2.append(mas_text2[g])
            break

      log_mas = []
      for i in range(0,len(mas_text_text1)):
        log_mas.append(mas_text_text1[i] + " -> " + mas_text_text2[i])
    else:
      log_mas = []
    #for i, log in zip(range(0,len(mas_text1)), log_mas):
      #if log:
     #   print(str(mas_text1[i]).strip() + " -> " + str(mas_text2[i]).strip())
    #print((1-compare_shingles(shingles1, shingles2)))
    return [1- com_shin,log_mas]

#if __name__ == '__main__':
  #get_shingles("1.txt","2.txt")
  #get_shingles("Proverka1.txt","Proverka_pokhozhaya_na_1.txt")
  #get_shingles("Normalizatsia_pokhozhaya_na_1.txt","Normalizatsia2.txt")