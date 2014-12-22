#!/usr/bin/python

import xml.etree.ElementTree as ET
import random
class Config():

   def __init__(self,filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        self.client_count = 0
        self.bank_count   = 0
        self.client_access_details = dict()
        self.no_of_servers     = dict()
        self.timeout           = 0
        self.retry             = 0
        self.lsequence_no      = 100



  # 	request_packet        = dict()
        self.request_packet = dict()
        for bank in root.findall('bank'):
          self.bank_count = self.bank_count + 1
          server = int(bank.find('server_num').text)
          name = bank.get('name')

          self.no_of_servers[name] = server
       #   print name, server

#	for key in head_tail_details.items():
#	    print key


        for client in root.findall('client'):
          self.client_count = self.client_count + 1
          access_details = dict()
          self.client_access_details[client.get('number')] = access_details
          for access_num in client.findall('access_bank'):
             name = access_num.get('name')
             accountNo = int(access_num.get('accountno'))
             access_details[name] = accountNo
  #           print name,accountNo

        for client in root.findall('client'):
          request_no = 0
          request_packet_details = dict()
          self.request_packet[int(client.get('number'))] = request_packet_details
          for request in client.findall('request_packet'):
             name = request.get('name')
             accountNo = int(request.get('accountno'))
             operation_Type = int(request.get('operation_Type'))
             amount = int(request.get('amount'))
             sequence_no = int(request.get('sequence_no'))
             request_packet_details[request_no] = {'bank_name':name,'accountNo':accountNo,'operation_Type':operation_Type,'amount':amount,'sequence_no':sequence_no}
             request_no = request_no + 1
          for request in client.findall('probability_packet'):
              name = request.get('name')
              seed = int(request.get('seed'))
              no_request = int(request.get('no_request'))
              get_balance = float(request.get('get_balance'))
              deposit_prob = float(request.get('deposit_prob'))
              withdraw_prob = float(request.get('withdraw_prob'))
              random.seed(seed)

             ### LOGIC FOR RANOMNESSS #######3

              for i in range(no_request):
                val = random.random()

                request_no = request_no + 1
                self.lsequence_no = self.lsequence_no + 1
                if (val >= 0 and val < get_balance):

                  request_packet_details[request_no] = {'bank_name':"JP",'accountNo':random.randint(0,100),'operation_Type' :2,'amount':0,'sequence_no':self.lsequence_no}

                elif (val >= get_balance and val <  get_balance + deposit_prob):

                  request_packet_details[request_no] = {'bank_name':"JP",'accountNo':random.randint(0,100),'operation_Type' :1,'amount':random.randint(0,100),'sequence_no':self.lsequence_no}

                elif (val >= get_balance + deposit_prob and val < get_balance + deposit_prob + withdraw_prob ):

                  request_packet_details[request_no] = {'bank_name':"JP",'accountNo':random.randint(0,100),'operation_Type' :0,'amount':random.randint(1,100),'sequence_no':self.lsequence_no}



#             print name,accountNo,operation_Type,amount
                 ### LOGIC FOR RANOMNESSS #######3


        self.timeout =  int(root.find('timeout').text)
        self.retry   =  int(root.find('retry').text)








