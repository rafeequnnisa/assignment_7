# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:38:13 2023

@author: hp
"""
def credit_card_offer(salary,credit_limit):
    if salary<10000:
        credit_limit=salary*10
    elif salary>=10000 and salary<30000:
        credit_limit=salary*30
        return credit_limit
    credit_card_offer(35000,2)
    
def Dmart_discount_offer(purchase_amount,discount):
    if purchase_amount<20000:
        discount="20%"
    elif purchase_amount>=20000 and purchase_amount<=40000:
        discount="30%"
    elif purchase_amount>50000:
        discount="40%"
        return discount

def Amazon_offer(product_type,discount):
    if product_type=="electronic":
        discount="20%"
    elif product_type=="cloth":
        discount="30%"
    elif product_type=="footware":
        discount="40%"
Amazon_offer("electronic",2)