class mcscrp:

    def __init__(self):
        """ scraping library """

    def __doc__(self):
        return """three methods:\n*get_tags for get tags exsiste in html page\n*scrp for scraping scrp(src,tag) have Two result:\n  -the first result scrp['txt'] = text exsiste between tags,\n  -the second result scrp['tag'] = the src (tags and text) exsiste between tags and method for get attrbs"""

    def scrp(self,src, tag):
        a = 0
        res = []
        ta = []
        tot = {}
        for i in range(src.count("</{}>".format(tag))):
            a = src.find("<{}".format(tag), a + 1)
            h = src.find(">", a + 1)
            c = src.find("</{}>".format(tag), h + 1)
            rs = src[h + 1:c]
            if '</' and '>' in rs:
                ta.append(rs.strip())
            else:
                res.append(rs.strip())
        tot['txt'] = res
        tot['tag'] = ta

        return tot

    def get_attr(self,src, attr):
        h = src.count('{}'.format(attr))
        n, q = 0, 0
        tg = 0
        de = {}
        for i in range(int(h)):
            tg = src.find('<', tg + 1)
            q = src.find(attr, q + 1)
            d = src.find('=', q + 1)
            f = src.find('"', d + 1)
            m = src.find('"', f + 1)
            de[src[q:d] + str(n + 1)] = src[f + 1:m]
            n += 1
        return de

    def get_tags(self,src):
        m = []
        n = 0
        for i in src:
            s = src.find("</", n)
            if s != -1:
                v = src[s:s + 10].find('>')
                v = src[s:s + 1 + v]
                m.append(v)
            n += 1
        z = []
        for c in list(set(m)):
            z.append(c[2:-1])
        return z
