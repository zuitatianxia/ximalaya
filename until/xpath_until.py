#多条件拼接xpath
#"//*[contains(@text,'更') and @text='更多' and text='显示']"
class XpathUntil:
    def make_xpath_unit_feature(self,loc):
        """
        xapth拼接中间部分
        :return: 
        """
        feature=""
        arg = loc.split(",")
        if len(arg) == 2:
            feature = "contains(@" + arg[0] + ",'" + arg[1] + "')"
        elif len(arg) == 3:
            if arg[2] == "1":
                feature = "@" + arg[0] + "='" + arg[1] + "'"
            elif arg[2] == "0":
                feature = "contains(@" + arg[0] + ",'" + arg[1] + "')"
        return feature

    #单个条件拼接xpath
    #"//*[contains(@text,'更多')]"
    #"//*[@text='更多']"
    def make_xpath_feature(self,loc):
        feature_start="//*["
        feature_end="]"
        feature=""
        #当loc为字符串时
        if isinstance(loc,str):
            if loc.startswith("//"):
                return loc
            else:
                feature=self.make_xpath_unit_feature(loc)
        #当loc为列表时
        # elif isinstance(loc,[]):
        else:
            count=0
            for i in loc:
                count+=1
                feature+=self.make_xpath_unit_feature(i)
                if count<len(loc):
                    feature += " and "

        loc=feature_start+feature+feature_end
        return loc
if __name__ == '__main__':
    loc="text,更多,1"
    #loc=["text,更多,0","text,显示,1","index,20,1"]
    #loc="//*[contains(@text,'更多')]"
    #make_xpath_feature(loc)
    xpath_until=XpathUntil()
    xx=xpath_until.make_xpath_feature(loc)
    print(xx)

