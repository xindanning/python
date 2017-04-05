__author__ = 'Administrator'
import configparser

class Mode():
    def __init__(self,mode_config):
        cf=configparser.ConfigParser()
        cf.read(mode_config)
        self.mode=cf["mode"]["mode"]
        self.case_list=eval((cf["mode"]["case_list"]))

    def Get_mode(self):
        mode=self.mode
        return  int(mode)

    def Get_case_list(self):
        case_list=self.case_list
        return  case_list
