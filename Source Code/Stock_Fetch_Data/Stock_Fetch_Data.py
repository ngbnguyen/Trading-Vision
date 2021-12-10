import requests
import pandas as pd
import pymongo
from pymongo import MongoClient
import os, json, datetime
client = MongoClient("mongodb+srv://tradingvision:123@cluster0.xmnn8.mongodb.net/TradingVision?retryWrites=true&w=majority")

headers = ["TimeStamp",
           "Time",
           "Name",
           "PreviousClosed",
           "Ceiling",
           "Floor",
           "Highest",
           "Lowest",
           "Volume",
           "Match"
           ]

hose_stocks = [
    "ACB",
    "APH",
    "ASM",
    "BCM",
    "BHN",
    "BID",
    "BMP",
    "BVH",
    "BWE",
    "CII",
    "CTD",
    "CTG",
    "DBC",
    "DCM",
    "DGC",
    "DGW",
    "DHC",
    "DHG",
    "DIG",
    "DPM",
    "DXG",
    "EIB",
    "FLC",
    "FPT",
    "GAS",
    "GEG",
    "GEX",
    "GMD",
    "GTN",
    "GVR",
    "HAG",
    "HBC",
    "HCM",
    "HDB",
    "HDG",
    "HHS",
    "HNG",
    "HPG",
    "HPX",
    "HSG",
    "HT1",
    "HVN",
    "IJC",
    "IMP",
    "ITA",
    "KBC",
    "KDC",
    "KDH",
    "KOS",
    "LCG",
    "LPB",
    "MBB",
    "MSB",
    "MSN",
    "MWG",
    "NLG",
    "NT2",
    "NVL",
    "OCB",
    "PAN",
    "PC1",
    "PDR",
    "PHR",
    "PLX",
    "PME",
    "PNJ",
    "POM",
    "POW",
    "PPC",
    "PVD",
    "PVT",
    "REE",
    "SAB",
    "SAM",
    "SBT",
    "SCS",
    "SJS",
    "SSI",
    "STB",
    "SZC",
    "TCB",
    "TCH",
    "TCM",
    "TLH",
    "TPB",
    "VCB",
    "VCG",
    "VCI",
    "VGC",
    "VHC",
    "VHM",
    "VIB",
    "VIC",
    "VIX",
    "VJC",
    "VND",
    "VNM",
    "VPB",
    "VPI",
    "VRE",
]

hnx_stocks = [
    "AAV",
    "AMV",
    "API",
    "APS",
    "ART",
    "BAB",
    "BCC",
    "BII",
    "BNA",
    "BTS",
    "BVS",
    "C69",
    "CEO",
    "CMS",
    "CSC",
    "CTC",
    "CVN",
    "DDG",
    "DL1",
    "DST",
    "DTC",
    "DTD",
    "DVG",
    "DXP",
    "EVS",
    "FID",
    "GKM",
    "HBS",
    "HHG",
    "HOM",
    "HUT",
    "IDC",
    "IDJ",
    "IPA",
    "ITQ",
    "IVS",
    "KLF",
    "KSF",
    "KSQ",
    "KVC",
    "LAS",
    "LIG",
    "MAC",
    "MBG",
    "MBS",
    "MCO",
    "MST",
    "NAG",
    "NBC",
    "NDN",
    "NDX",
    "NRC",
    "NSH",
    "NTP",
    "NVB",
    "OCH",
    "PCG",
    "PHP",
    "PLC",
    "PSD",
    "PSI",
    "PV2",
    "PVC",
    "PVG",
    "PVI",
    "PVL",
    "PVS",
    "S99",
    "SCG",
    "SCI",
    "SD5",
    "SD6",
    "SD9",
    "SDA",
    "SHS",
    "SPI",
    "SRA",
    "SVN",
    "TA9",
    "TAR",
    "TC6",
    "TDT",
    "THD",
    "THT",
    "TIG",
    "TNG",
    "TTH",
    "TVC",
    "TVD",
    "VC2",
    "VC3",
    "VC7",
    "VC9",
    "VCS",
    "VGS",
    "VHE",
    "VIG",
    "VKC",
    "VTV",
    "WSS",
]

upcom_stocks = [
    "AAS",
    "ABB",
    "AFX",
    "AMS",
    "ANT",
    "APF",
    "BCA",
    "BMS",
    "BOT",
    "BSR",
    "BTN",
    "BVB",
    "BVG",
    "C4G",
    "CBI",
    "CDO",
    "CEN",
    "CLX",
    "CST",
    "CTR",
    "DDV",
    "DFF",
    "DGT",
    "DRI",
    "DVN",
    "EIN",
    "EVF",
    "G36",
    "HAC",
    "HD6",
    "HHV",
    "HMS",
    "HSV",
    "HTE",
    "HU4",
    "ILA",
    "KHB",
    "KLB",
    "KSH",
    "LMH",
    "LPT",
    "LTG",
    "MLS",
    "MPC",
    "MSR",
    "MVC",
    "NAB",
    "NDT",
    "NED",
    "OIL",
    "PAS",
    "PFL",
    "PGB",
    "PGV",
    "PRT",
    "PVM",
    "PVP",
    "PXT",
    "QNS",
    "QTP",
    "SBS",
    "SD3",
    "SD7",
    "SDD",
    "SDP",
    "SGB",
    "SGI",
    "SGP",
    "SKH",
    "SRB",
    "SRT",
    "SSH",
    "STH",
    "TBD",
    "TCI",
    "TID",
    "TIS",
    "TL4",
    "TNS",
    "TTN",
    "TVN",
    "VAB",
    "VBB",
    "VCR",
    "VE9",
    "VEA",
    "VFS",
    "VGI",
    "VGT",
    "VGV",
    "VHG",
    "VLG",
    "VNA",
    "VNB",
    "VNH",
    "VNP",
    "VOC",
    "VTD",
    "VTP",
    "XMC",
]

hose_URL = "https://banggia.cafef.vn/stockhandler.ashx?center=1"
hnx_URL = "https://banggia.cafef.vn/stockhandler.ashx?center=2"
upcom_URL = "https://banggia.cafef.vn/stockhandler.ashx?center=9"


# Lay du lieu ve roi return vao bien se (Stock Exchange). se la 1 bien DataFrame cua Pandas.
def fetch_function(url, se_stocks):
    url_se = url
        
    response = requests.get(url_se)
    se = pd.DataFrame.from_dict(
        pd.json_normalize(response.json()), orient="columns"
    )
    se = se[["Time", "a", "b", "c", "d", "v", "w", "n", "l"]]
    se = se[se["a"].isin(se_stocks)]
    se.insert(0, 'TimeStamp', datetime.datetime.now().strftime("%H:%M %d/%m/%Y"))
    se.columns = headers
    return se


def import_to_mongodb(se,name):
    db = client['StockPrice']
    data = se.to_dict(orient = "records")
    for row in data:
        existing_document = db[f'{name}'].find_one(row)
        if not existing_document:
            db[f'{name}'].insert_one(row)
        else:
            print(str(row) + "existed")
   
   
#-----------------------------------------------------------------------------------------------------------------------------------
#Fetch data    
hose = fetch_function(hose_URL,hose_stocks)
hnx = fetch_function(hnx_URL,hnx_stocks)
upcom = fetch_function(upcom_URL,upcom_stocks)

#Import to MongoDB
import_to_mongodb(hose,'hose')
import_to_mongodb(hnx,'hnx')
import_to_mongodb(upcom,'upcom')