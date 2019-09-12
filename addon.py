from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()

url1 = "http://feeds.feedburner.com/crooked-conversations" #CROOKEDMINIS
url2 = "http://feeds.feedburner.com/hysteria-podcast" #HYSTERIA
url3 = "http://feeds.feedburner.com/keep-it" #KEEPIT
url4 = "http://feeds.feedburner.com/lovett-or-leave-it" #LOVETTORLEAVEIT
url5 = "http://feeds.feedburner.com/majority-54" #MAJORITY54WITHJASONKANDER
url6 = "http://feeds.feedburner.com/pod-save-america" #PODSAVEUSA
url7 = "http://feeds.feedburner.com/pod-save-the-people" #PODSAVETHEPEOPLE
url8 = "http://feeds.feedburner.com/pod-save-the-world" #PODSAVETHEWORLD
url9 = "http://feeds.feedburner.com/the-wilderness" #THEWILDERNESS
url10 = "http://feeds.feedburner.com/this-land" #THISLAND
url11 = "http://feeds.feedburner.com/with-friends-like-these" #WITHFRIENDLIKETHESE

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001),
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://lh3.googleusercontent.com/FEgSSdv6hb4NUsLa7IUoJ70MNjs66rNP_j_tyLca5K1oEGHckoVD6_rAIKeb=s180-c-e100-rwu-v1"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://crooked.com/wp-content/uploads/2018/06/750x750-e1529000788846.png"},
        {
            'label': plugin.get_string(30003), 
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://crooked.com/wp-content/uploads/2017/12/ki_wide_image_v6-e1528750175180.png"},
        {
            'label': plugin.get_string(30004),
            'path': plugin.url_for('episodes4'),
            'thumbnail': "https://crooked.com/wp-content/uploads/2019/01/750x750.png"},
        {
            'label': plugin.get_string(30005),
            'path': plugin.url_for('episodes5'),
            'thumbnail': "https://crooked.com/wp-content/uploads/2017/11/m54_wide_image-e1528750714358.png"},
        {
            'label': plugin.get_string(30006),
            'path': plugin.url_for('episodes6'),
            'thumbnail': "https://crooked.com/wp-content/uploads/2017/10/show-podsaveamerica@2xtrans-e1528750384834.png"},
        {
            'label': plugin.get_string(30007),
            'path': plugin.url_for('episodes7'),
            'thumbnail': "https://crooked.com/wp-content/uploads/2018/05/pstp_wide_image-e1528750680770.jpg"},
        {
            'label': plugin.get_string(30008),
            'path': plugin.url_for('episodes8'),
            'thumbnail': "https://crooked.com/wp-content/uploads/2019/01/PSTW_540x790.png"},
        {
            'label': plugin.get_string(30009),
            'path': plugin.url_for('episodes9'),
            'thumbnail': "https://crooked.com/wp-content/uploads/2018/07/wilderness_title.png"},
        {
            'label': plugin.get_string(30010),
            'path': plugin.url_for('episodes10'),
            'thumbnail': "https://crooked.com/wp-content/uploads/2019/05/this-land@2x.png"},
        {
            'label': plugin.get_string(30011),
            'path': plugin.url_for('episodes11'),
            'thumbnail': "https://crooked.com/wp-content/uploads/2018/03/wflt_wide_image-e1528750559627.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(url3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items

@plugin.route('/episodes4/')
def episodes4():
    soup4 = mainaddon.get_soup4(url4)
    playable_podcast4 = mainaddon.get_playable_podcast4(soup4)
    items = mainaddon.compile_playable_podcast4(playable_podcast4)
    return items

@plugin.route('/episodes5/')
def episodes5():
    soup5 = mainaddon.get_soup5(url5)
    playable_podcast5 = mainaddon.get_playable_podcast5(soup5)
    items = mainaddon.compile_playable_podcast5(playable_podcast5)
    return items

@plugin.route('/episodes6/')
def episodes6():
    soup6 = mainaddon.get_soup6(url6)
    playable_podcast6 = mainaddon.get_playable_podcast6(soup6)
    items = mainaddon.compile_playable_podcast6(playable_podcast6)
    return items

@plugin.route('/episodes7/')
def episodes7():
    soup7 = mainaddon.get_soup7(url7)
    playable_podcast7 = mainaddon.get_playable_podcast7(soup7)
    items = mainaddon.compile_playable_podcast7(playable_podcast7)
    return items

@plugin.route('/episodes8/')
def episodes8():
    soup8 = mainaddon.get_soup8(url8)
    playable_podcast8 = mainaddon.get_playable_podcast8(soup8)
    items = mainaddon.compile_playable_podcast8(playable_podcast8)
    return items

@plugin.route('/episodes9/')
def episodes9():
    soup1 = mainaddon.get_soup1(url9)
    playable_podcast9 = mainaddon.get_playable_podcast9(soup9)
    items = mainaddon.compile_playable_podcast9(playable_podcast9)
    return items

@plugin.route('/episodes10/')
def episodes10():
    soup10 = mainaddon.get_soup10(url10)
    playable_podcast10 = mainaddon.get_playable_podcast10(soup10)
    items = mainaddon.compile_playable_podcast10(playable_podcast10)
    return items

@plugin.route('/episodes11/')
def episodes11():
    soup11 = mainaddon.get_soup11(url11)
    playable_podcast11 = mainaddon.get_playable_podcast11(soup11)
    items = mainaddon.compile_playable_podcast11(playable_podcast11)
    return items

if __name__ == '__main__':
    plugin.run()
