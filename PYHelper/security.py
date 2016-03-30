# -*- coding: utf-8 -*-
import bleach


'''

    Cross Site Script Avoid


'''

class XSS(object):


    def avoid(self,string):

        self.string = string
        self.Flag = False
        if bleach.clean(self.string) == self.string:
            self.Flag = False
            return self.Flag
        else:
            self.Flag = True
            return self.Flag
'''
   Remote Code Execution  Avoid
'''


class RCE(object):

    def avoidRCE(self,pgetParameter):

        self.is_check = pgetParameter
        self.Flag = False
        if re.findall(";|\$\(|\|\||&&",self.is_check):
            return self.Flag
        else:
            self.Flag = True
            return self.Flag

