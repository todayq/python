#coding=gbk
#��һ��ע�Ͳ���ʡ��ָ������������֧������
#�������ļ���32λ��python 3.4.3�����ͨ��
import urllib
import time
import string
import ctypes
import os,sys
from ctypes import *

path = os.path.dirname(os.path.realpath(__file__))
dll = ctypes.WinDLL(path+'\WmCode.dll')
class WmOcr:
    def init():
        with open(path+'\meitaotao.dat',"rb") as f:
            dat=f.read()
            if dll.UseUnicodeString(1, 1) == False:
                return False
            elif dll.LoadWmFromBufferEx(dat, len(dat),'tomorrow') != 1:
                return False
            else:
                dll.SetWmOptionEx(1,4, 1)
                dll.SetWmOptionEx(1, 6, 80)
                return True

    def ocr(dat):
        Str = create_string_buffer(4)  # �����ı�������
        if (dll.GetImageFromBufferEx(1,dat,len(dat), Str)):
            return Str.raw.decode("gbk")
        else:
            return
