#this is a simulation of the Plate and frame heat exchanger (PFHEX) & includes the RLB HEX

#constants
mass1=6898;
mass2=93810;
mRatio=mass1/mass2;# a constant commonly used in HEX problems& Formulas
effeciency=.9;# the average effeciency for each HEX in the plant is ~.9
cPBrine=.938;#this is the specific heat capacity of the raw brine/treated brine in BTU/Lb
pFTempD=0;
######################################################################################################################
#RLB HEX
rLBMass=91995;

rLBTempA=68;
rLBTempD=0;
for x in range (0,100):
    rLBTempC=(rLBTempA*(rLBMass/mass2)+rLBTempD)/(1+(rLBMass/mass2));
    qIdealRLB=cPBrine*mass2*(rLBTempC-rLBTempD)*-1;
    qRealRLB= qIdealRLB*effeciency;

    rLBTempB= (qRealRLB/(cPBrine*rLBMass))+rLBTempA;



#######################################################################################################################
#P&F heat exchanger Inputs
    pFTempA=rLBTempB; #determined by settler tank output

#actual math from heat exchanger useing "Qa+Qd=Qc+Qb" formula

    pFTempC=(pFTempA*mRatio+pFTempD)/(1+mRatio)

#finds the Q for bottom of HEX then finds Q transfered to B
    qIdealPF=cPBrine*mass2*(pFTempC-pFTempD)*-1
    qRealPF=qIdealPF*effeciency;

    pFTempB=(qRealPF/(cPBrine*mass1))+pFTempA;
#print("pftempC");
#print(pFTempC);
#print ("pftempB")
#print(pFTempB)
#######################################################################################################################

#this is the simulation for the Steam & tube heat exchanger (STHEX)

    massSteam=520;# this is the standard amount of steam used at least from the documents cecil gave me 
    sTTempA=pFTempB;
    sTTempD=345;

    sTTempC=((cPBrine*mass1*sTTempA/massSteam)+sTTempD)/(1+(cPBrine*mass1/massSteam));
    qIdealST=massSteam*(sTTempC-sTTempD)*-1;
    qRealST=qIdealST*effeciency;

    sTTempB=(qRealST/(cPBrine*mass1))+sTTempA;
    pFTempD=sTTempB;
    rLBTempD=pFTempC
#print("STtempC");
    print(sTTempC);
#print ("STtempB")
    #print(sTTempB);







