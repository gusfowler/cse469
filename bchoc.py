import os
import uuid
import argparse
import struct
import datetime
from collections import namedtuple

class blockchain:
    def __init__(self, filePath):
        self.filePath = filePath
        self.BLOCK_HEAD_FORMAT = struct.Struct('20s d 16s I 11s I')
        self.BLOCK_DATA_FORMAT = struct.Struct('14s')

    def initiate(self):
        headFormat = struct.Struct('20s d 16s I 11s I')
        headTuple = namedtuple('BLOCK_HEAD', 'hash timestamp case_id item_id state length')
        dataTuple = namedtuple('BLOCK_DATA', 'data')

        try:
            # check if file exists
            fileBuffer = open(self.filePath, 'rb')
            fileBuffer.close()

        except:
            # if file does not exist create it
            timestamp = datetime.timestamp(datetime.now())
            headVals = (str.encode(""), timestamp, str.encode(""), 0, str.encode("INITIAL"), 14)
            dataVal = (str.encode("Initial block"))
            
            packedHeadValues = self.BLOCK_HEAD_FORMAT.pack(*headVals)
            packedDataValue = self.BLOCK_DATA_FORMAT.pack(dataVal)

            currentBlockHead = headTuple._make(self.BLOCK_HEAD_FORMAT.unpack(packedHeadValues))
            currentBlockData = dataTuple._make(self.BLOCK_DATA_FORMAT.unpack(packedDataValue))

            fileBuffer = open(self.filePath, 'wb')
            fileBuffer.write(packedHeadValues)
            fileBuffer.write(packedDataValue)
            fileBuffer.close()

        fileBuffer = open(self.filePath, 'rb')

        try:
            headContent = fileBuffer.read(self.BLOCK_HEAD_FORMAT.size)
            currentBlockHead = headTuple._mkae(self.BLOCK_HEAD_FORMAT.unpack(headContent))

    def insert(self):
        ###
    
    def checkout(self):
        ###

    def checkin(self):
        ###

    def remove(self):
        ###