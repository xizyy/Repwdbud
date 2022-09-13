# 多因素密码生成
# 这里的因素特指不同的序列，如字母为一因素，数字为一因素，特殊符号为一因素。
# 大写不作为单独的因素添加。
import src.jobnumber as jn
from pathlib import Path


class Factor2:
    def __init__(self, domain, level):
        self.domaim = domain
        self.level = level
        self.year = ['2008','2009','2010','2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
        self.NumExt="./dict/NumExt.txt"
        self.StrExt="./dict/StrExt.txt"
        self.acroName="./dict/acroName217"
        if self.level == 1:
            self.str1 = ["@","!"]
            self.weakdic = "./dict/weakTo6Digit168.txt"
        elif self.level == 2:
            self.str1 = ["@","!","#","$","~","_"]
            self.weakdic = "./dict/weakTo8Digit702.txt"
        elif self.level == 3:
            self.str1 = ['!', "@", "#", "$", "%", "~", "?", "_", "-", "+", "&", ".", "=" , "*"]
            self.weakdic = "./dict/weak1111.txt"
        else:
            pass


    ########################公司名######################################################
    # 公司名+年份
    # Example: Jingdong2019
    def sequence4(self):
        result = []
        year = self.year
        domian = str(self.domaim)
        for x in year:
            result.append(str(domian + x))
        for x in year:
            result.append(domian.capitalize() + x)
        return result

    # 公司名+特殊字符+年份
    # Example: Jingdong@2019
    def sequence5(self):
        result = []
        year = self.year
        str1 = self.str1
        domian = str(self.domaim)
        # domianList1 = list(str(self.domaim))
        for i in str1:
            for x in year:
                result.append(str(domian + i + x))
            for x in year:
                result.append(domian.capitalize() + i + x)
        return result

    # 公司名+特殊字符+top1000弱口令
    # Example: Jingdong@2019
    def sequence6(self):
        result = []
        with open(Path(self.weakdic)) as f:
            pwd = f.readlines()
        str1 = self.str1
        domian = str(self.domaim)
        # domianList1 = list(str(self.domaim))
        for i in str1:
            for x in pwd:
                x = x.replace("\n", "")
                result.append(str(domian + i + x))
            for x in pwd:
                x = x.replace("\n", "")
                result.append(domian.capitalize() + i + x)
        return result

    # 公司名称+年份+特殊字字符
    # Example: Jingdong2021@
    def sequence7(self):
        result = []
        year = self.year
        str1 = self.str1
        domian = str(self.domaim)
        for i in str1:
            for x in year:
                result.append(str(domian + x + i))
            for x in year:
                result.append(domian.capitalize() + x + i)
        return result

    # 公司名称+特殊字符+短数字尾缀
    def sequence8(self):
        result = []
        with open(Path(self.NumExt)) as f:
            pwd = f.readlines()
        str1 = self.str1
        domian = str(self.domaim)
        for i in str1:
            for x in pwd:
                x = x.replace("\n", "")
                result.append(str(domian + i + x))
            for x in pwd:
                x = x.replace("\n", "")
                result.append(domian.capitalize() + i + x)
        return result

    # 公司名称+短数字尾缀
    def sequence9(self):
        result = []
        with open(Path(self.NumExt)) as f:
            pwd = f.readlines()
        domian = str(self.domaim)
        for x in pwd:
            x = x.replace("\n", "")
            result.append(str(domian + x))
        for x in pwd:
            x = x.replace("\n", "")
            result.append(domian.capitalize() + x)
        return result


    # 公司名称+字符尾缀
    def sequence10(self):
        result = []
        with open(Path(self.StrExt)) as f:
            pwd = f.readlines()
        domian = str(self.domaim)
        for x in pwd:
            x = x.replace("\n", "")
            result.append(str(domian + x))
        for x in pwd:
            x = x.replace("\n", "")
            result.append(domian.capitalize() + x)
        return result

    # 公司名称+数字尾缀+字符尾缀
    def sequence11(self):
        result = []
        with open(Path(self.NumExt)) as f:
            pwd = f.readlines()

        str1 = self.str1
        domian = str(self.domaim)
        for i in str1:
            for x in pwd:
                x = x.replace("\n", "")
                result.append(str(domian + x + i))
            for x in pwd:
                x = x.replace("\n", "")
                result.append(domian.capitalize() + x + i)
        return result
