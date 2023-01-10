#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Ga0weI
# @Time    : 2022.12.13
# @Function: decoder for shiro AES CBC(PKCS5) and GCM

import os
from tkinter import *
import time
from Crypto.Cipher import AES
import base64

LOG_LINE_NUM = 0
keys =[
'kPH+bIxk5D2deZiIxcaaaA==',
    '4AvVhmFLUs0KTA3Kprsdag==',
    'Z3VucwAAAAAAAAAAAAAAAA==',
    'fCq+/xW488hMTCD+cmJ3aQ==',
    '0AvVhmFLUs0KTA3Kprsdag==',
    '1AvVhdsgUs0FSA3SDFAdag==',
    '1QWLxg+NYmxraMoxAXu/Iw==',
    '25BsmdYwjnfcWmnhAciDDg==',
    '2AvVhdsgUs0FSA3SDFAdag==',
    '3AvVhmFLUs0KTA3Kprsdag==',
    '3JvYhmBLUs0ETA5Kprsdag==',
    'r0e3c16IdVkouZgk1TKVMg==',
    '5aaC5qKm5oqA5pyvAAAAAA==',
    '5AvVhmFLUs0KTA3Kprsdag==',
    '6AvVhmFLUs0KTA3Kprsdag==',
    '6NfXkC7YVCV5DASIrEm1Rg==',
    '6ZmI6I2j5Y+R5aSn5ZOlAA==',
    'cmVtZW1iZXJNZQAAAAAAAA==',
    '7AvVhmFLUs0KTA3Kprsdag==',
    '8AvVhmFLUs0KTA3Kprsdag==',
    '8BvVhmFLUs0KTA3Kprsdag==',
    '9AvVhmFLUs0KTA3Kprsdag==',
    'OUHYQzxQ/W9e/UjiAGu6rg==',
    'a3dvbmcAAAAAAAAAAAAAAA==',
    'aU1pcmFjbGVpTWlyYWNsZQ==',
    'bWljcm9zAAAAAAAAAAAAAA==',
    'bWluZS1hc3NldC1rZXk6QQ==',
    'bXRvbnMAAAAAAAAAAAAAAA==',
    'ZUdsaGJuSmxibVI2ZHc9PQ==',
    'wGiHplamyXlVB11UXWol8g==',
    'U3ByaW5nQmxhZGUAAAAAAA==',
    'MTIzNDU2Nzg5MGFiY2RlZg==',
    'L7RioUULEFhRyxM7a2R/Yg==',
    'a2VlcE9uR29pbmdBbmRGaQ==',
    'WcfHGU25gNnTxTlmJMeSpw==',
    'OY//C4rhfwNxCQAQCrQQ1Q==',
    '5J7bIJIV0LQSN3c9LPitBQ==',
    'f/SY5TIve5WWzT4aQlABJA==',
    'bya2HkYo57u6fWh5theAWw==',
    'WuB+y2gcHRnY2Lg9+Aqmqg==',
    'kPv59vyqzj00x11LXJZTjJ2UHW48jzHN',
    '3qDVdLawoIr1xFd6ietnwg==',
    'ZWvohmPdUsAWT3=KpPqda',
    'YI1+nBV//m7ELrIyDHm6DQ==',
    '6Zm+6I2j5Y+R5aS+5ZOlAA==',
    '2A2V+RFLUs+eTA3Kpr+dag==',
    '6ZmI6I2j3Y+R1aSn5BOlAA==',
    'SkZpbmFsQmxhZGUAAAAAAA==',
    '2cVtiE83c4lIrELJwKGJUw==',
    'fsHspZw/92PrS3XrPW+vxw==',
    'XTx6CKLo/SdSgub+OPHSrw==',
    'sHdIjUN6tzhl8xZMG3ULCQ==',
    'O4pdf+7e+mZe8NyxMTPJmQ==',
    'HWrBltGvEZc14h9VpMvZWw==',
    'rPNqM6uKFCyaL10AK51UkQ==',
    'Y1JxNSPXVwMkyvES/kJGeQ==',
    'lT2UvDUmQwewm6mMoiw4Ig==',
    'MPdCMZ9urzEA50JDlDYYDg==',
    'xVmmoltfpb8tTceuT5R7Bw==',
    'c+3hFGPjbgzGdrC+MHgoRQ==',
    'ClLk69oNcA3m+s0jIMIkpg==',
    'Bf7MfkNR0axGGptozrebag==',
    '1tC/xrDYs8ey+sa3emtiYw==',
    'ZmFsYWRvLnh5ei5zaGlybw==',
    'cGhyYWNrY3RmREUhfiMkZA==',
    'IduElDUpDDXE677ZkhhKnQ==',
    'yeAAo1E8BOeAYfBlm4NG9Q==',
    'cGljYXMAAAAAAAAAAAAAAA==',
    '2itfW92XazYRi5ltW0M2yA==',
    'XgGkgqGqYrix9lI6vxcrRw==',
    'ertVhmFLUs0KTA3Kprsdag==',
    '5AvVhmFLUS0ATA4Kprsdag==',
    's0KTA3mFLUprK4AvVhsdag==',
    'hBlzKg78ajaZuTE0VLzDDg==',
    '9FvVhtFLUs0KnA3Kprsdyg==',
    'd2ViUmVtZW1iZXJNZUtleQ==',
    'yNeUgSzL/CfiWw1GALg6Ag==',
    'NGk/3cQ6F5/UNPRh8LpMIg==',
    '4BvVhmFLUs0KTA3Kprsdag==',
    'MzVeSkYyWTI2OFVLZjRzZg==',
    'CrownKey==a12d/dakdad',
    'empodDEyMwAAAAA',
    'LEGEND-CAMPUS-CIPHERKEY==',
    '5RC7uBZLkByfFfJm22q/Zw==',
    '3AvVhdAgUs0FSA4SDFAdBg==',
    'eXNmAAAAAAAAAAAAAAAAAA==',
    'U0hGX2d1bnMAAAAAAAAAAA==',
    'Ymx1ZXdoYWxlAAAAAAAAAA==',
    'UGlzMjAxNiVLeUVlXiEjLw==',
    'FP7qKJzdJOGkzoQzo2wTmA==',
    'MDgBSEFqYIoWYezkWDywig==',
    '0Av6jWaXCkCu5A9nJbPxLI==',
    'fPimdozRt+SSSbZS8/HARA==',
    'empodDEyMwAAAAAAAAAAAA==',
    'A7UzJgh1+EWj5oBFi+mSgw==',
    'YTM0NZomIzI2OTsmIzM0NTueYQ==',
    'c2hpcm9fYmF0aXMzMgAAAA==',
    'i45FVt72K2kLgvFrJtoZRw==',
    'U3BAbW5nQmxhZGUAAAAAAA==',
    'ZnJlc2h6Y24xMjM0NTY3OA==',
    'Jt3C93kMR9D5e8QzwfsiMw==',
    'MTIzNDU2NzgxMjM0NTY3OA==',
    'vXP33AonIp9bFwGl7aT7rA==',
    'V2hhdCBUaGUgSGVsbAAAAA==',
    'Z3h6eWd4enklMjElMjElMjE=',
    'Q01TX0JGTFlLRVlfMjAxOQ==',
    'ZAvph3dsQs0FSL3SDFAdag==',
    'Is9zJ3pzNh2cgTHB4ua3+Q==',
    'NsZXjXVklWPZwOfkvk6kUA==',
    'GAevYnznvgNCURavBhCr1w==',
    '66v1O8keKNV3TTcGPK1wzg==',
    'SDKOLKn2J1j/2BHjeZwAoQ==',
    'MzVeSkYyWTI2OFVLZjRzZg==',
    'U3BAbW5nQmxhZGUAAAAAAA==',
    "kPH+bIxk5D2deZiIxcaaaA==",
    "4AvVhmFLUs0KTA3Kprsdag==",
    "Z3VucwAAAAAAAAAAAAAAAA==",
    "fCq+/xW488hMTCD+cmJ3aQ==",
    "0AvVhmFLUs0KTA3Kprsdag==",
    "1AvVhdsgUs0FSA3SDFAdag==",
    "1QWLxg+NYmxraMoxAXu/Iw==",
    "25BsmdYwjnfcWmnhAciDDg==",
    "2AvVhdsgUs0FSA3SDFAdag==",
    "3AvVhmFLUs0KTA3Kprsdag==",
    "3JvYhmBLUs0ETA5Kprsdag==",
    "r0e3c16IdVkouZgk1TKVMg==",
    "5aaC5qKm5oqA5pyvAAAAAA==",
    "5AvVhmFLUs0KTA3Kprsdag==",
    "6AvVhmFLUs0KTA3Kprsdag==",
    "6NfXkC7YVCV5DASIrEm1Rg==",
    "6ZmI6I2j5Y+R5aSn5ZOlAA==",
    "cmVtZW1iZXJNZQAAAAAAAA==",
    "7AvVhmFLUs0KTA3Kprsdag==",
    "8AvVhmFLUs0KTA3Kprsdag==",
    "8BvVhmFLUs0KTA3Kprsdag==",
    "9AvVhmFLUs0KTA3Kprsdag==",
    "OUHYQzxQ/W9e/UjiAGu6rg==",
    "a3dvbmcAAAAAAAAAAAAAAA==",
    "aU1pcmFjbGVpTWlyYWNsZQ==",
    "bWljcm9zAAAAAAAAAAAAAA==",
    "bWluZS1hc3NldC1rZXk6QQ==",
    "bXRvbnMAAAAAAAAAAAAAAA==",
    "ZUdsaGJuSmxibVI2ZHc9PQ==",
    "wGiHplamyXlVB11UXWol8g==",
    "U3ByaW5nQmxhZGUAAAAAAA==",
    "MTIzNDU2Nzg5MGFiY2RlZg==",
    "L7RioUULEFhRyxM7a2R/Yg==",
    "a2VlcE9uR29pbmdBbmRGaQ==",
    "WcfHGU25gNnTxTlmJMeSpw==",
    "OY//C4rhfwNxCQAQCrQQ1Q==",
    "5J7bIJIV0LQSN3c9LPitBQ==",
    "f/SY5TIve5WWzT4aQlABJA==",
    "bya2HkYo57u6fWh5theAWw==",
    "WuB+y2gcHRnY2Lg9+Aqmqg==",
    "3qDVdLawoIr1xFd6ietnwg==",
    "YI1+nBV//m7ELrIyDHm6DQ==",
    "6Zm+6I2j5Y+R5aS+5ZOlAA==",
    "2A2V+RFLUs+eTA3Kpr+dag==",
    "6ZmI6I2j3Y+R1aSn5BOlAA==",
    "SkZpbmFsQmxhZGUAAAAAAA==",
    "zSyK5Kp6PZAAjlT+eeNMlg==",
    "2cVtiE83c4lIrELJwKGJUw==",
    "fsHspZw/92PrS3XrPW+vxw==",
    "XTx6CKLo/SdSgub+OPHSrw==",
    "sHdIjUN6tzhl8xZMG3ULCQ==",
    "O4pdf+7e+mZe8NyxMTPJmQ==",
    "HWrBltGvEZc14h9VpMvZWw==",
    "rPNqM6uKFCyaL10AK51UkQ==",
    "Y1JxNSPXVwMkyvES/kJGeQ==",
    "lT2UvDUmQwewm6mMoiw4Ig==",
    "MPdCMZ9urzEA50JDlDYYDg==",
    "xVmmoltfpb8tTceuT5R7Bw==",
    "c+3hFGPjbgzGdrC+MHgoRQ==",
    "ClLk69oNcA3m+s0jIMIkpg==",
    "Bf7MfkNR0axGGptozrebag==",
    "1tC/xrDYs8ey+sa3emtiYw==",
    "ZmFsYWRvLnh5ei5zaGlybw==",
    "cGhyYWNrY3RmREUhfiMkZA==",
    "IduElDUpDDXE677ZkhhKnQ==",
    "yeAAo1E8BOeAYfBlm4NG9Q==",
    "cGljYXMAAAAAAAAAAAAAAA==",
    "2itfW92XazYRi5ltW0M2yA==",
    "XgGkgqGqYrix9lI6vxcrRw==",
    "ertVhmFLUs0KTA3Kprsdag==",
    "5AvVhmFLUS0ATA4Kprsdag==",
    "s0KTA3mFLUprK4AvVhsdag==",
    "hBlzKg78ajaZuTE0VLzDDg==",
    "9FvVhtFLUs0KnA3Kprsdyg==",
    "d2ViUmVtZW1iZXJNZUtleQ==",
    "yNeUgSzL/CfiWw1GALg6Ag==",
    "NGk/3cQ6F5/UNPRh8LpMIg==",
    "4BvVhmFLUs0KTA3Kprsdag==",
    "MzVeSkYyWTI2OFVLZjRzZg==",
    "empodDEyMwAAAAAAAAAAAA==",
    "A7UzJgh1+EWj5oBFi+mSgw==",
    "c2hpcm9fYmF0aXMzMgAAAA==",
    "i45FVt72K2kLgvFrJtoZRw==",
    "U3BAbW5nQmxhZGUAAAAAAA==",
    "ZnJlc2h6Y24xMjM0NTY3OA==",
    "Jt3C93kMR9D5e8QzwfsiMw==",
    "MTIzNDU2NzgxMjM0NTY3OA==",
    "vXP33AonIp9bFwGl7aT7rA==",
    "V2hhdCBUaGUgSGVsbAAAAA==",
    "Q01TX0JGTFlLRVlfMjAxOQ==",
    "ZAvph3dsQs0FSL3SDFAdag==",
    "Is9zJ3pzNh2cgTHB4ua3+Q==",
    "NsZXjXVklWPZwOfkvk6kUA==",
    "GAevYnznvgNCURavBhCr1w==",
    "66v1O8keKNV3TTcGPK1wzg==",
    "SDKOLKn2J1j/2BHjeZwAoQ==",
    "tiVV6g3uZBGfgshesAQbjA==",
    "RVZBTk5JR0hUTFlfV0FPVQ==",
    "WkhBTkdYSUFPSEVJX0NBVA==",
    "YystomRZLMUjiK0Q1+LFdw==",
    "QDFCnfkLUs0KTA3Kprsdag==",
    "2adsfasdqerqerqewradsf==",
    "5oiR5piv5p2h5ZK46bG8IQ==",
    "3AvVhmFLUs0KTA3KaTHGFg==",
    "2AvVCXsxUs0FSA7SYFjdQg==",
    "TGMPe7lGO/Gbr38QiJu1/w==",
    "GhrF5zLfq1Dtadd1jlohhA==",
    "sBv2t3okbdm3U0r2EVcSzB==",
    "AztiX2RUqhc7dhOzl1Mj8Q==",
    "QVN1bm5uJ3MgU3Vuc2l0ZQ==",
    "3Av2hmFLAs0BTA3Kprsd6E==",
    "YVd4dmRtVjViM1UlM0QIdn==",
    "5AvVhCsgUs0FSA3SDFAdag==",
    "QUxQSEFNWVNPRlRCVUlMRA==",
    "9Ami6v2G5Y+r5aPnE4OlBB==",
    "sgIQrqUVxa1OZRRIK3hLZw==",
    "mIccZhQt6EBHrZIyw1FAXQ==",
    "wrjUh2ttBPQLnT4JVhriug==",
    "s2SE9y32PvLeYo+VGFpcKA==",
    "3AvVhdAgUs0FSA4SDFAdBg==",
    "3rvVhmFLUs0KAT3Kprsdag==",
    "4WCZSJyqdUQsije93aQIRg==",
    "4rvVhmFLUs0KAT3Kprsdag==",
    "5RC7uBZLkByfFfJm22q/Zw==",
    "FP7qKJzdJOGkzoQzo2wTmA==",
    "NoIw91X9GSiCrLCF03ZGZw==",
    "U0hGX2d1bnMAAAAAAAAAAA==",
    "UGlzMjAxNiVLeUVlXiEjLw==",
    "Ymx1ZXdoYWxlAAAAAAAAAA==",
    "c2hvdWtlLXBsdXMuMjAxNg==",
    "eXNmAAAAAAAAAAAAAAAAAA==",
    "oPH+bIxk5E2enZiIxcqaaA==",
    "QF5HMyZAWDZYRyFnSGhTdQ==",
    "2AvVhdsgUsOFSA3SDFAdag==",
    "fCq+/xW488hMTCE+cmJ3FF==",
    "HOlg7NHb9potm0n5s4ic0Q==",
    "YWdlbnRAZG1AMjAxOHN3Zg==",
    "3AvVhMFLIs0KTA3Kprsdag==",
    "M2djA70UBBUPDibGZBRvrA==",
    "AF05JAuyuEB1ouJQ9Y9Phg==",
    "4AvVhmFLUs0KTA3KAAAAAA==",
    "4AvVhmFLUs0KTA3Kprseaf==",
    "w793pPq5ZVBKkj8OhV4KaQ==",
    "Z3VucwAAAAAAAAAAAAABBB==",
    "pyyX1c5x2f0LZZ7VKZXjKO==",
    "8AvVhdsgUs0FSA3SDFAdag==",
    "B9rPF8FHhxKJZ9k63ik7kQ==",
    "4AvVhmFLUs0KTA3KprSdAg==",
    "2AvVidsaUSofSA3SDFAdog==",
    "3qDVdLawoIr1xFd6ietnsg==",
    "R29yZG9uV2ViAAAAAAAAAA==",
    "2AvVhdsgUs0FSA3SDFAder==",
    "GHxH6G3LFh8Zb3NwoRgfFA==",
    "A+kWR7o9O0/G/W6aOGesRA==",
    "4AvVhmFLUs5KTA1Kprsdag==",
    "2AvVhmFLUs0KTA3Kprsdag==",
    "b2EAAAAAAAAAAAAAAAAAAA==",
    "fcq+/xW488hMTCD+cmJ3aq==",
    "wyLZMDifwq3sW1vhhHpgKA==",
    "YnlhdnMAAAAAAAAAAAAAAA==",
    "3AvVhdAgUs1FSA4SDFAdBg==",
    "ZGdmdwAAAAAAAAAAAAAAAA",
    "Cj6LnKZNLEowAZrdqyH/Ew==",
    "Z3VucwACAOVAKALACAADSA==",
    "duhfin37x6chw29jsne45m==",
    "FjbNm1avvGmWE9CY2HqV75==",
    "2AvVhdsgERdsSA3SDFAdag==",
    "4AvVhmFLUs0TTA3Kprsdag==",
    "2AvVhdsgUs0FSA3SaFAdfg==",
    "4AvVhm2LUs0KTA3Kprsdag==",
    "pbnA+Qzen1vjV3rNqQBLHg==",
    "kPv59vyqzj00x11LXJZTjJ2UHW48jzHN",
    "a69ec781563b1a5d791f7b2bdd117a36",
    "4AvVhdsgUs0F563SDFAdag==",
    "4AvVhmFLUsOKTA3Kprsdag==",
    "9AVvhnFLuS3KTV8KprsdAg==",
    "FJoQCiz0z5XWz2N2LyxNww==",
    "FL9HL9Yu5bVUJ0PDU1ySvg==",
    "GsHaWo4m1eNbE0kNSMULhg==",
    "HeUZ/LvgkO7nsa18ZyVxWQ==",
    "HoTP07fJPKIRLOWoVXmv+Q==",
    "KU471rVNQ6k7PQL4SqxgJg==",
    "QAk0rp8sG0uJC4Ke2baYNA==",
    "Rb5RN+LofDWJlzWAwsXzxg==",
    "SrpFBcVD89eTQ2icOD0TMg==",
    "Us0KvVhTeasAm43KFLAeng==",
    "YWJjZGRjYmFhYmNkZGNiYQ==",
    "ZUdsaGJuSmxibVI2ZHc9PQ",
    "ZjQyMTJiNTJhZGZmYjFjMQ==",
    "aG91c2Vob3VzZWhvdXNlMg==",
    "bXdrXl9eNjY2KjA3Z2otPQ==",
    "fdCEiK9YvLC668sS43CJ6A==",
    "iycgIIyCatQofd0XXxbzEg==",
    "kPH+bIxk5D2deZiIxcabaA==",
    "kPH+bIxk5D2deZiIxcacaA==",
    "l8cc6d2xpkT1yFtLIcLHCg==",
    "lt181dcQVz/Bo9Wb8ws/Cg==",
    "m0/5ZZ9L4jjQXn7MREr/bw==",
    "qQFtSnnj/sx7vu51ixAyEQ==",
    "zIiHplamyXlVB11UXWol8g==",
    "bTBANVpaOUw0ampRWG43TVJFcF5iXjdJ",
    "nhNhwZ6X7xzgXnnZBxWFQLwCGQtJojL3",
    "LEGEND-CAMPUS-CIPHERKEY==",
    "ZWvohmPdUsAWT3=KpPqda",
    "k3+XHEg6D8tb2mGm7VJ3nQ==",
    "CrownKey==a12d/dakdad",
]

def findevalclass(plainhex):
    if "cafebabe" in plainhex.lower():
        index = plainhex.index("cafebabe")
        classhex = plainhex[index:]
        hexbytes = bytes.fromhex(classhex)
        with open("eval.class", "wb") as f:
            print("\nfind a eval Class,saveed as eval.class\n")
            f.write(hexbytes)
            return  1
    else:
        print("not found classbytes in payload")
        return 0


def gcm_decode(payload,key):
    try:
        mode =  AES.MODE_GCM
        cipher=base64.b64decode(payload)
        iv=cipher[0:16]
        enc=cipher[16:-16]
        tag=cipher[-16:]
        aes = AES.new(base64.b64decode(key), mode, iv)
        plaintext=aes.decrypt_and_verify(enc,tag)
        # print("GCM_decode_plaintext:")
        # print(plaintext)
        plainhex = plaintext.hex()
        if(plainhex.startswith("aced")):
            s=findevalclass(plainhex)
            print("Decode by GCM")
            base64_plaintext=base64.b64encode(plaintext).decode()
            print ("\nbase64_plaintext:\n"+base64_plaintext+"\n")
            if (s):
                os.system("java -jar .\cfr-0.152.jar .\eval.class >eval.java")
                return "eval" + base64_plaintext
            else:
                return base64_plaintext
        else:
            return 0
    except Exception:
        return 0

def cbc_decode(payload,key):
    try:
        unpad = lambda s : s[0:-(s[-1])]
        mode =  AES.MODE_CBC
        cipher=base64.b64decode(payload)
        iv=cipher[0:16]
        enc=cipher[16:]
        aes = AES.new(base64.b64decode(key), mode, iv)
        plaintext=aes.decrypt(enc)
        plainhex = plaintext.hex()
        if(plainhex.startswith("aced")):
            print("\nDecode by CBC")
            s=findevalclass(plainhex)
            base64_plaintext = base64.b64encode(unpad(plaintext)).decode()
            print("\nbase64_plaintext:\n" + base64_plaintext + "\n")
            if(s):
                os.system("java -jar .\cfr-0.152.jar .\eval.class >eval.java")
                return "eval"+base64_plaintext
            else:
                return base64_plaintext
        else:
            return 0
    except Exception:
        return 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name

    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("Shiro解码处理工具_v2.0 by Ga0weI")
        self.init_window_name.geometry('1068x681+10+10')

        self.init_data_label = Label(self.init_window_name, text="待解码数据")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="默认编码解码结果")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)
        #文本框
        self.init_data_Text = Text(self.init_window_name, width=67, height=35)  #待解码内容录入
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=70, height=49)  #解码展示框
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 运行日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        #按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="解码", bg="lightblue", width=10,command=self.shiroDecode)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=1, column=11)


    #解码函数
    def shiroDecode(self):
        keyx = 0
        payload = self.init_data_Text.get(1.0,END).strip().replace("\n","")
        payload = payload.replace("rememberMe=","")
        if payload:
            result=""
            flag = 0 #判断是否是解密成功
            for key in keys:
                if (cbc_decode(payload, key) != 0):
                    result = cbc_decode(payload, key)
                    print("\nkey:"+key)
                    keyx =key
                    flag=1
                    break
                if (gcm_decode(payload, key) != 0):
                    result = gcm_decode(payload, key)
                    print("\nkey:" + key)
                    keyx = key
                    flag=1
                    break
            if(flag==0):
                print("此payload非默认编码！！！！！！")
                self.write_log_to_Text("INFO:failed")
                self.result_data_Text.delete(1.0, END)
            else:
                self.result_data_Text.delete(1.0, END)
                if(result.startswith("eval")):
                    self.result_data_Text.insert(1.0, "解码后的内容中存在恶意类，以还原到当前目录下的eval.class文件中,并反编译得到eval.java文件:\n\n"+result[4:])
                    self.write_log_to_Text("INFO:success,key is _{}_ ,".format(keyx))
                else:
                    self.result_data_Text.insert(1.0, result)
                    self.write_log_to_Text("INFO:success,key is _{}_ ,".format(keyx))


    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)


def gui_start():
    init_window = Tk()
    ZMJ_PORTAL = MY_GUI(init_window)
    ZMJ_PORTAL.set_init_window()
    init_window.mainloop()

if __name__ == '__main__':
    gui_start()