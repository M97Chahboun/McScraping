from McScrp import mcscrp


def get_attrs(src, tag):
    t = src.count('="')
    n = 0
    di = {}
    a2 = 0
    de = {}
    bi = src.count('<a')
    sc = mcscrp()
    nm = sc.scrp(src, tag)['txt']
    for u in range(bi):
        for i in range(int(t / bi)):
            c = src.find('<{}'.format(tag), n)
            e = src.find(' ', a2 + 1)
            s = src.find('=', e + 1)
            a1 = src.find('"', s + 1)
            a2 = src.find('"', a1 + 1)
            de[src[e + 1:s]] = src[a1 + 1:a2]
        if len(nm[n]) == 0:
            di['a%s' % (n)] = de
        else:
            di[nm[n]] = de
        n += 1
        de = {}

    return di


def get_attr(src,attr):
    h = src.count('{}'.format(attr))
    gt = src.count('</')
    print(gt,h)
    n,q = 0,0
    tg=0
    de ={}
    for i in range(int(h)):
        tg = src.find('<',tg+1)
        q = src.find(attr,q+1)
        d = src.find('=',q+1)
        f = src.find('"',d+1)
        m = src.find('"', f+1)
        print(src[f+1:m])
        de[src[q:d]+str(n+1)] = src[f+1:m]
        n+=1
    return de

a = '<li><div><a href="https://www.britannica.com/place/Afghanistan" class="md-crosslink">Afghanistan</a></div></li><li><div><a href="https://www.britannica.com/place/Albania" class="md-crosslink">Albania</a></div></li><li><div><a href="https://www.britannica.com/place/Algeria" class="md-crosslink">Algeria</a></div></li><li><div><a href="https://www.britannica.com/place/Andorra" class="md-crosslink">Andorra</a></div></li><li><div><a href="https://www.britannica.com/place/Angola" class="md-crosslink">Angola</a></div></li><li><div><a href="https://www.britannica.com/place/Antigua-and-Barbuda" class="md-crosslink">Antigua and Barbuda</a></div></li><li><div><a href="https://www.britannica.com/place/Argentina" class="md-crosslink">Argentina</a></div></li><li><div><a href="https://www.britannica.com/place/Armenia" class="md-crosslink">Armenia</a></div></li><li><div><a href="https://www.britannica.com/place/Australia" class="md-crosslink">Australia</a></div></li><li><div><a href="https://www.britannica.com/place/Austria" class="md-crosslink">Austria</a></div></li><li><div><a href="https://www.britannica.com/place/Azerbaijan" class="md-crosslink">Azerbaijan</a></div></li>'

f = get_attr(a,'href')
print(f)

