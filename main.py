__author__ = 'Diego'

import requests

print("sa")


mydata = {
    "ft_ent_identifier":806265299412392,
    "comment_text":".",
    "source":0,
    "client_id":"1417724167079:1088214603",
    "reply_fbid":"",
    "parent_comment_id":"",
    "rootid":"u_jsonp_4_1z",
    "clp":"",
    "attached_sticker_fbid":0,
    "attached_photo_fbid":0,
    "":"",
    "":"",
    "ft[tn]":"[]",
    "ft[fbfeed_location]":"2",
    "ft[id]":806265299412392,
    "ft[author]":520939739,
    "nctr[_mod]":"pagelet_group_mall",
    "av":520939739,
    "__user":"520939739",
    "__a":"1",
    "__dyn":"7nmanEyl2qm9udDgDxyKAEWCueyp9Esx6iqAdBGeqrWo8ponUKezpUgDyQqUkBBzEy6Kdy8-",
    "__req":"22",
   "fb_dtsg":"AQF9H2zsOzb5",
    "ttstamp":"2658170577250122115791229853",
    "__rev":"1518885"
}
myCookies = dict(lu='RwChrf0tHb4vbc-9XlHbecxg',
                 datr='wdWAU28-VThaT2RcgCfZHL1t',
                 p='-2',
                 c_user='520939739',
                 fr='0080EXOw2iN99Pc8t.AWVbYbNXborQYZsKN2ySr-dkfZg.BUgKHr.Cz.AAA.0.AWWR1ZEm',
                 xs='230%3AQqgGPShMo5Sg_w%3A2%3A1417716202%3A18422',
                 csm='2',
                 s='Aa5ONbRHshf2n2JQ.BUgKHr',
                 presence='EM417724160EuserFA2520939739A2EstateFDsb2F1417719739429Et2F_5b_5dElm2FnullEuct2F1417715604BEtrFA2loadA2EtwF2624972753EatF1417724160362G417724160743CEchFDp_5f520939739F222CC',
                 act='1417724164665%2F32',
                 _e_0Idp_26='%5B%220Idp%22%2C1417724164666%2C%22act%22%2C1417724164665%2C32%2C%22-%22%2C%22ufi%22%2C%22-%22%2C%22group_mall%22%2C%22r%22%2C%22%2Fgroups%2Fclasificadosuniandes%2F%22%2C%7B%22ft%22%3A%7B%22tn%22%3A%22%5B%5D%22%2C%22fbfeed_location%22%3A2%2C%22id%22%3A806265299412392%2C%22author%22%3A520939739%7D%2C%22gt%22%3A%7B%22type%22%3A%22click2canvas%22%2C%22fbsource%22%3A703%2C%22ref%22%3A%22nf_generic%22%2C%22engagement%22%3A%7B%22eng_type%22%3A%221%22%2C%22eng_src%22%3A%2215%22%2C%22eng_tid%22%3A%22%22%2C%22eng_data%22%3A%5B%5D%7D%7D%7D%2C0%2C0%2C0%2C0%2C%22mdsftd%22%2C%22%2Fajax%2Fhome%2Fgroup.php%22%2C18%5D'
)

r = requests.post("https://www.facebook.com/ajax/ufi/add_comment.php", data=mydata, cookies=myCookies)


print(r)
print(r.text)
print(r.content)
print(r.url)


print ( 26581727866105505112284105109 > 2658170577250122115791229853)



