import os
import csv
import argparse
import warnings
import scipy.constants as C


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--Pre',  type=str, default = 'results.csv')
    parser.add_argument('--Post', type=str, default = 'Standard_results.csv')
    args = parser.parse_args()

'''
rows = [] # List to collect rows with the new format
with open(args.Pre, 'r') as csvfile: # Read the raw data file args.Pre as input
    reader = csv.reader(csvfile)
    for row in reader: # Interate all the rows in the raw data 
        newrow = [] # List to save each new row
        for i in range(0, len(row)):
            if i != 5: # Keep as it is for columns except column 'measurement'
                newrow.append(row[i])
            elif row[i].count('NULL') or row[i].count('#C0') or row[i].count('#V'): # Delete row containing NULL, #C0 or #V, 
                newrow = []
                break
            elif row[i].count('#'): # Split column 'measurement' 
                unit = row[i].split('#')
                for u in range(0, len(unit)):
                    newrow.append(unit[u])
                if len(unit) < 4:
                    newrow.append('')
                if len(unit) < 3:
                    warnings.warn("Something might be wrong", DeprecationWarning)
            else: # Write header of the csv
                newrow.append('Tag')
                newrow.append('measurement')
                newrow.append('Item')
                newrow.append('Hz')
                
        if len(newrow) > 0:
            rows.append(newrow)

with open(args.Post, 'w', newline='') as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerows(rows)
'''

def PerAreaCapCal(k, d):
    '''
    Calculate the capacitance per um^2 in nF
    '''
    epsilon = C.epsilon_0*k
    Cap = epsilon*(10**-12)/(d*10**-10)*10**9

    return Cap

def UnitsCountCal(ChipX, ChipY, BlockSize, BlockSpace, UnitSpace, ScrLine=0, SealRing=6, AASRSpace=10, CornerUints=4):
    '''
    Calculate the number of units in one chip
    Considering the space occupied by:
    1. the Scrubber line: "Scrline"
    2. by the Sealring:  "SealRing"
    3. by the Active area to Sealring space: "AASRSpace"
    Considering the rounding corner
    '''
    AAX = ChipX - (ScrLine + SealRing + AASRSpace)*2
    AAY = ChipY - (ScrLine + SealRing + AASRSpace)*2
    UnitX = BlockSize*2 + BlockSpace + UnitSpace
    UnitY = BlockSize*2 + BlockSpace + UnitSpace
    XUnits = AAX//UnitX
    YUnits = AAY//UnitY
    NUnits = XUnits*YUnits
    
    return NUnits-CornerUints

def UnitTrenchesCal(TrenchLength, TrenchCD, TrenchSpace): 
    '''
    Calculate the number of trenches in one unit
    '''

    return int((TrenchLength+TrenchSpace)/(TrenchCD+TrenchSpace))*4

def TrenchAreaCal(TrenchLength, TrenchCD, TrenchDepth):
    '''
    Calculate the vertical area per trench in um^2
    '''
    return ((TrenchLength+TrenchCD)*2*TrenchDepth)

def UnitAreaCal(TrenchLength, TrenchCD, TrenchDepth, TrenchSpace):
    '''
    Calculate the area per unit in um^2 
    '''
    return (TrenchAreaCal(TrenchLength, TrenchCD, TrenchDepth)*UnitTrenchesCal(TrenchLength, TrenchCD, TrenchSpace)+TrenchLength*TrenchLength)
    

def UnitCapCal(k, d, TrenchLength, TrenchCD, TrenchDepth, TrenchSpace):
    '''
    Calculate the capacitance per unit in nF
    '''
    return (UnitAreaCal(TrenchLength, TrenchCD, TrenchDepth, TrenchSpace)*PerAreaCapCal(k, d))

def main():
    ChipX      = 760
    ChipY      = 760
    BlockSize  = 11
    BlockSpace = 0.1
    UnitSpace  = 0.1
    k          = 6.9
    d          = 5400
    TrenchLength = BlockSize
    TrenchCD     = 1.5
    TrenchDepth  = 45
    TrenchSpace  = 1

    Cap_Unit = UnitCapCal(k, d, TrenchLength, TrenchCD, TrenchDepth, TrenchSpace)
    N_Units = UnitsCountCal(ChipX, ChipY, BlockSize, BlockSpace, UnitSpace)
    Cap = Cap_Unit*N_Units

    print ("Total units: ", N_Units)
    print ("Trenches in one unit: ", UnitTrenchesCal(BlockSize, TrenchCD, TrenchSpace))
    print ("Capacitance Per Area(um2): ", PerAreaCapCal(k, d))
    print ("Capacitance Per Unit(nF): ", Cap_Unit)
    print ("Capacitance(nF): ", Cap)