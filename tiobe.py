# coding:utf-8
'''
every month TIOBE will update the popularity of programming languages.
'''
import argparse
import ConfigParser
import datetime
import os
import re
import sys
import urllib
from glob import glob


def getdata_TIOBE(filename):
    '''update datas from TIOBE,
        write online data to filename using ConfigParser format'''
    dic = {}
    url = r'http://www.tiobe.com/tiobe-index//'
    content = urllib.urlopen(url).read()
    pattern = re.compile('series:(.*)({name :.*)\n', flags=re.S)
    fw = open('content.html', 'w')
    fw.write(content)
    fw.close()
    datas = re.search(pattern, content).group(1)
    sp = datas.split('{')
    for lang_all in sp:
        '''{name : 'Java',data : [[Date.UTC(2001, 5, 30), 26.492], [Date.UTC(2001, 6, 30), 25.028], [Date.UTC(2001, 7, 30), 24.660], [Date.UTC(2001, 8, 28), 24.817], [Date.UTC(2001, 9, 26), 25.676], [Date.UTC(2001, 10, 28), 24.369], [Date.UTC(2001, 11, 31), 24.195], [Date.UTC(2002, 0, 30), 24.063], [Date.UTC(2002, 1, 27), 24.005], [Date.UTC(2002, 2, 29), 24.409], [Date.UTC(2002, 3, 29), 25.049], [Date.UTC(2002, 4, 29), 25.195], [Date.UTC(2002, 5, 29), 24.196], [Date.UTC(2002, 6, 31), 24.534], [Date.UTC(2002, 7, 29), 22.886], [Date.UTC(2002, 8, 29), 24.482], [Date.UTC(2002, 9, 30), 24.201], [Date.UTC(2002, 10, 29), 24.116], [Date.UTC(2002, 11, 31), 24.227], [Date.UTC(2003, 0, 31), 24.791], [Date.UTC(2003, 1, 28), 24.775], [Date.UTC(2003, 2, 31), 24.596], [Date.UTC(2003, 3, 30), 24.664], [Date.UTC(2003, 4, 30), 23.108], [Date.UTC(2003, 5, 30), 22.337], [Date.UTC(2003, 6, 31), 23.209], [Date.UTC(2003, 7, 31), 22.242], [Date.UTC(2003, 8, 30), 21.902], [Date.UTC(2003, 9, 31), 23.084], [Date.UTC(2003, 10, 30), 25.008], [Date.UTC(2003, 11, 31), 23.573], [Date.UTC(2004, 0, 31), 22.564], [Date.UTC(2004, 1, 29), 23.173], [Date.UTC(2004, 2, 31), 24.240], [Date.UTC(2004, 3, 30), 18.692], [Date.UTC(2004, 4, 30), 17.539], [Date.UTC(2004, 5, 30), 17.055], [Date.UTC(2004, 6, 31), 16.997], [Date.UTC(2004, 7, 30), 15.896], [Date.UTC(2004, 8, 30), 17.050], [Date.UTC(2004, 9, 31), 14.804], [Date.UTC(2004, 10, 30), 16.332], [Date.UTC(2004, 11, 31), 17.478], [Date.UTC(2005, 0, 31), 18.340], [Date.UTC(2005, 1, 28), 18.871], [Date.UTC(2005, 2, 31), 16.981], [Date.UTC(2005, 3, 30), 17.397], [Date.UTC(2005, 4, 31), 18.569], [Date.UTC(2005, 5, 30), 19.659], [Date.UTC(2005, 6, 31), 21.206], [Date.UTC(2005, 7, 31), 22.442], [Date.UTC(2005, 8, 30), 21.871], [Date.UTC(2005, 11, 3), 22.128], [Date.UTC(2006, 0, 4), 22.255], [Date.UTC(2006, 1, 2), 22.430], [Date.UTC(2006, 2, 1), 21.889], [Date.UTC(2006, 3, 2), 21.275], [Date.UTC(2006, 4, 1), 21.316], [Date.UTC(2006, 5, 1), 21.128], [Date.UTC(2006, 6, 2), 21.853], [Date.UTC(2006, 7, 2), 22.377], [Date.UTC(2006, 8, 2), 21.532], [Date.UTC(2006, 9, 1), 21.172], [Date.UTC(2006, 10, 2), 20.400], [Date.UTC(2006, 11, 1), 19.907], [Date.UTC(2007, 0, 2), 19.160], [Date.UTC(2007, 1, 3), 18.978], [Date.UTC(2007, 2, 3), 18.044], [Date.UTC(2007, 3, 1), 18.360], [Date.UTC(2007, 4, 5), 19.140], [Date.UTC(2007, 5, 2), 20.025], [Date.UTC(2007, 6, 2), 21.014], [Date.UTC(2007, 7, 5), 21.768], [Date.UTC(2007, 8, 2), 21.701], [Date.UTC(2007, 9, 4), 21.616], [Date.UTC(2007, 10, 4), 20.542], [Date.UTC(2007, 11, 3), 20.049], [Date.UTC(2008, 0, 3), 20.849], [Date.UTC(2008, 1, 7), 21.483], [Date.UTC(2008, 5, 1), 20.890], [Date.UTC(2008, 6, 2), 21.345], [Date.UTC(2008, 7, 3), 21.571], [Date.UTC(2008, 8, 3), 20.715], [Date.UTC(2008, 9, 6), 20.949], [Date.UTC(2008, 10, 2), 20.299], [Date.UTC(2008, 11, 3), 17.917], [Date.UTC(2009, 0, 2), 19.022], [Date.UTC(2009, 1, 1), 19.401], [Date.UTC(2009, 2, 5), 19.797], [Date.UTC(2009, 3, 7), 19.341], [Date.UTC(2009, 4, 1), 19.537], [Date.UTC(2009, 5, 4), 20.147], [Date.UTC(2009, 6, 2), 20.452], [Date.UTC(2009, 7, 1), 19.527], [Date.UTC(2009, 8, 5), 19.383], [Date.UTC(2009, 9, 2), 18.650], [Date.UTC(2009, 10, 2), 18.373], [Date.UTC(2009, 11, 2), 17.061], [Date.UTC(2010, 0, 5), 17.482], [Date.UTC(2010, 1, 7), 17.348], [Date.UTC(2010, 2, 7), 17.509], [Date.UTC(2010, 3, 5), 18.051], [Date.UTC(2010, 4, 15), 17.957], [Date.UTC(2010, 6, 6), 18.673], [Date.UTC(2010, 6, 30), 17.994], [Date.UTC(2010, 8, 11), 17.915], [Date.UTC(2010, 9, 2), 18.166], [Date.UTC(2010, 10, 3), 18.509], [Date.UTC(2010, 11, 7), 17.999], [Date.UTC(2011, 0, 2), 17.773], [Date.UTC(2011, 1, 8), 18.482], [Date.UTC(2011, 2, 8), 19.711], [Date.UTC(2011, 3, 3), 19.043], [Date.UTC(2011, 4, 2), 18.160], [Date.UTC(2011, 5, 5), 18.580], [Date.UTC(2011, 5, 27), 18.580], [Date.UTC(2011, 6, 8), 19.251], [Date.UTC(2011, 7, 3), 19.409], [Date.UTC(2011, 8, 10), 18.761], [Date.UTC(2011, 9, 9), 17.913], [Date.UTC(2011, 10, 7), 17.874], [Date.UTC(2011, 11, 4), 17.561], [Date.UTC(2012, 0, 8), 17.468], [Date.UTC(2012, 1, 5), 17.050], [Date.UTC(2012, 2, 11), 17.110], [Date.UTC(2012, 3, 8), 17.026], [Date.UTC(2012, 4, 9), 16.599], [Date.UTC(2012, 5, 10), 16.265], [Date.UTC(2012, 6, 4), 16.087], [Date.UTC(2012, 7, 10), 16.352], [Date.UTC(2012, 8, 2), 16.267], [Date.UTC(2012, 9, 5), 17.193], [Date.UTC(2012, 10, 4), 17.455], [Date.UTC(2012, 11, 2), 17.567], [Date.UTC(2013, 0, 5), 17.417], [Date.UTC(2013, 1, 8), 18.387], [Date.UTC(2013, 2, 11), 18.156], [Date.UTC(2013, 3, 7), 17.681], [Date.UTC(2013, 4, 8), 16.914], [Date.UTC(2013, 5, 9), 16.656], [Date.UTC(2013, 6, 7), 15.906], [Date.UTC(2013, 6, 12), 15.906], [Date.UTC(2013, 7, 4), 15.978], [Date.UTC(2013, 8, 11), 16.154], [Date.UTC(2013, 9, 10), 16.107], [Date.UTC(2013, 10, 9), 16.521], [Date.UTC(2013, 11, 6), 17.311], [Date.UTC(2014, 0, 1), 16.523], [Date.UTC(2014, 1, 8), 17.316], [Date.UTC(2014, 2, 3), 16.406], [Date.UTC(2014, 3, 10), 17.348], [Date.UTC(2014, 4, 7), 16.907], [Date.UTC(2014, 5, 8), 16.113], [Date.UTC(2014, 6, 6), 15.688], [Date.UTC(2014, 7, 11), 14.984], [Date.UTC(2014, 8, 1), 14.140], [Date.UTC(2014, 9, 3), 13.506], [Date.UTC(2014, 10, 8), 14.391], [Date.UTC(2014, 11, 7), 14.959], [Date.UTC(2015, 0, 6), 15.528], [Date.UTC(2015, 1, 5), 15.345], [Date.UTC(2015, 2, 7), 15.580], [Date.UTC(2015, 3, 13), 16.041], [Date.UTC(2015, 4, 13), 16.869], [Date.UTC(2015, 5, 6), 17.822], [Date.UTC(2015, 6, 12), 17.728], [Date.UTC(2015, 7, 6), 19.274], [Date.UTC(2015, 8, 5), 19.565], [Date.UTC(2015, 9, 4), 19.543], [Date.UTC(2015, 10, 7), 20.403], [Date.UTC(2015, 11, 4), 20.973], [Date.UTC(2016, 0, 2), 21.465], [Date.UTC(2016, 1, 2), 21.145], [Date.UTC(2016, 2, 3), 20.528], [Date.UTC(2016, 3, 7), 20.846], [Date.UTC(2016, 4, 6), 20.956], [Date.UTC(2016, 5, 5), 20.794], [Date.UTC(2016, 6, 4), 19.804], [Date.UTC(2016, 7, 6), 19.010], [Date.UTC(2016, 8, 8), 18.236], [Date.UTC(2016, 9, 7), 18.799], [Date.UTC(2016, 10, 5), 18.755]]}'''
        # print lang_all
        lang = re.search('\'(.+)\'', lang_all)
        if lang != None:
            lang = lang.group(1)
            d = {}
            pattern = re.compile('\((\d+), (\d+), (\d+)\), (\d+\.?\d+)')
            for one in re.findall(pattern, lang_all):
                # print one
                try:
                    date = datetime.date(
                        int(one[0]), int(one[1]) + 1, int(one[2]))
                except:
                    date = datetime.date(int(one[0]), int(
                        one[1]) + 1, int(one[2]) - 1)
                value = float(one[3])
                d[date] = value
            dic[lang] = d
    # print dic.keys()
    cf = ConfigParser.ConfigParser()
    for lang, d in dic.items():
        cf.add_section(lang)
        for date, v in d.items():
            cf.set(lang, str(date), v)
    cf.write(open(filename, 'w'))
    print "[+] Update data completed."


def plot_TIOBE(filename):
    '''plot from filename using ConfigParser format'''
    cf = ConfigParser.ConfigParser()
    cf.read(filename)
    secs = cf.sections()
    plt.figure(figsize=(20, 15))
    xxs = []
    yys = []
    langs = []
    for idx, lan in enumerate(secs):
        # color = 'rgbyckrgbyck'[idx]
        datas = []
        for date, v in cf.items(lan):
            date_f = datetime.datetime.strptime(date, '%Y-%m-%d')
            datas.append(
                (datetime.date(date_f.year, date_f.month, date_f.day), float(v)))
        datas.sort()
        xxs.append([i[0] for i in datas])
        yys.append([i[1] for i in datas])
        langs.append(lan)
    for xx, yy, lang in zip(xxs, yys, langs):
        plt.plot(xx, yy, label=lang)
        xy = (xx[len(xx) / 2], yy[len(yy) / 2])
        plt.text(xy[0], xy[1], lang)
    plt.legend()
    plt.grid()
    plt.savefig("popularity.png")
    plt.show()
    plt.close()

if __name__ == '__main__':

    datafilename = "data.conf"
    path = os.path.dirname(os.path.realpath(__file__))
    parser = argparse.ArgumentParser(
        description='''description: get popularity of programming languages,
        author: Zhaopeng Zhang''')
    parser.add_argument('-u', '--update', action='store_true',
                        help='update data.')
    parser.add_argument('-p', '--plot', action='store_true',
                        help='plot data.')
    args = parser.parse_args()
    if args.update:
        getdata_TIOBE(os.path.join(path, datafilename))
    if args.plot:
        import matplotlib.pyplot as plt
        plot_TIOBE(datafilename)
