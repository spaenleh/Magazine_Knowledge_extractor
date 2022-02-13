import re

hidden_bookmark = re.compile(r"_Hlk|_Hlt\d{8}", re.IGNORECASE)
bau = re.compile(r"bau|baut\d+", re.IGNORECASE)
goback = re.compile(r"_GoBack\d*", re.IGNORECASE)
author_id = re.compile(r"baep-author-id\d*", re.IGNORECASE)
heading = re.compile(r"_heading|_PMH\d+_", re.IGNORECASE)
sref = re.compile(r"sref|_Ref|sbref\d*", re.IGNORECASE)
obj_pref = re.compile(r"OBJ_PREFIX_|cts\d+-cit-\d+|OLE_LINK\d+|acel\d+", re.IGNORECASE)
gj_symbol = re.compile(r"_gj|__UnoMark__", re.IGNORECASE)
sd_d = re.compile(r"s\d+_\d+", re.IGNORECASE)

DEFAULT = "default"

rules = {
    "ABE": [
        bau,
        goback,
        author_id,
        heading,
        sref,
        gj_symbol,
        obj_pref,
        sd_d,
        hidden_bookmark,
    ],
    "LBCS": [
        hidden_bookmark,
    ],
    DEFAULT: [
        bau,
        hidden_bookmark,
    ]
}

MAG = 'magazine'
ISSUE_NUMBER = 'numero'
DATE = 'date'
TITLE = 'titre'
ARTICLE = 'article'
PAGE = 'page'

titles = {
    "ABE": re.compile(r"(?P<magazine>\w+)-(?P<numero>\d+)-(?P<date>\w+-\d+)-(?P<titre>[\w-]+)-"),
    "LBCS": re.compile(r"(?P<magazine>\w+)-(?P<numero>\d+)-(?P<date>\w+-\d+)-(?P<titre>[\w-]+)-"),
}

levels = {
    "ABE": [1],
    "LBCS": [2],
}
