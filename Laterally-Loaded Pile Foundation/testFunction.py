#!usr/bin/pyton3
# -*- coding: UTF-8 -*-

import math
import numpy as np 
from scipy import interpolate

def get_pyParam ( pyDepth, gamma, phiDegree, b, pEleLength, puSwitch, kSwitch, gwtSwitch):
# soil unit weight (kN/m^3)
    pyDepth=3.1
    gamma = 17.0
    # soil internal friction angle (degrees)
    phiDegree = 36.0
    # soil shear modulus at pile tip (kPa)
    Gsoil = 150000.0
    # length of pile head (above ground surface) (m)
    L1 = 1.0
    # length of embedded pile (below ground surface) (m)
    L2 = 20.0
    # pile diameter
    b = 1.0
    # number of pile elements
    nElePile = 84
    # pile element length 
    pEleLength = (L1+L2)/nElePile
    # number of total pile nodes
    nNodePile =  1 + nElePile
    puSwitch=1
    kSwitch=1
    gwtSwitch=1
    #----------------------------------------------------------
    #  define ultimate lateral resistance, pult 
    #----------------------------------------------------------

    # pult is defined per API recommendations (Reese and Van Impe, 2001 or API, 1987) for puSwitch = 1
    #  OR per the method of Brinch Hansen (1961) for puSwitch = 2

    pi = 3.14159265358979
    phi = phiDegree * (pi/180)
    zbRatio = pyDepth / b

    #-------API recommended method-------

    if puSwitch == 1:

      # obtain loading-type coefficient A for given depth-to-diameter ratio zb
      #  ---> values are obtained from a figure and are therefore approximate
        zb = []
        dataNum = 41
        zb=np.linspace(0.0,5.0,dataNum)
        As = [2.8460, 2.7105, 2.6242, 2.5257, 2.4271, 2.3409, 2.2546, 2.1437, 2.0575, 1.9589, 1.8973, 1.8111, 1.7372, 1.6632, 1.5893, 1.5277, 1.4415, 1.3799, 1.3368, 1.2690, 1.2074, 1.1581, 
            1.1211, 1.0780, 1.0349, 1.0164, 0.9979, 0.9733, 0.9610, 0.9487, 0.9363, 0.9117, 0.8994, 0.8994, 0.8871, 0.8871, 0.8809, 0.8809, 0.8809, 0.8809, 0.8809] 
        f=interpolate.interp1d(zb,As)
      # linear interpolation to define A for intermediate values of depth:diameter ratio
        
        if zbRatio >= 5.0:
            A = 0.88
        else :
            A=f(zbRatio)
      # define common terms
        alpha = phi / 2
        beta = pi / 4 + phi / 2
        K0 = 0.4
        
        tan_1 = math.tan(pi / 4 - phi / 2)        
        Ka = math.pow(tan_1 , 2) 

      # terms for Equation (3.44), Reese and Van Impe (2001)
        tan_2 = math.tan(phi)
        tan_3 = math.tan(beta - phi)
        sin_1 = math.sin(beta)
        cos_1 = math.cos(alpha)
        c1 = K0 * tan_2 * sin_1 / (tan_3*cos_1)
        
        tan_4 = math.tan(beta)
        tan_5 = math.tan(alpha)
        c2 = (tan_4/tan_3)*tan_4 * tan_5
        c3 = K0 * tan_4 * (tan_2 * sin_1 - tan_5)
        c4 = tan_4 / tan_3 - Ka

        # terms for Equation (3.45), Reese and Van Impe (2001)
        pow_1 = math.pow(tan_4,8)
        pow_2 = math.pow(tan_4,4)
        c5 = Ka * (pow_1-1)
        c6 = K0 * tan_2 * pow_2

      # Equation (3.44), Reese and Van Impe (2001)
        pst = gamma * pyDepth * (pyDepth * (c1 + c2 + c3) + b * c4)

      # Equation (3.45), Reese and Van Impe (2001)
        psd = b * gamma * pyDepth * (c5 + c6)

      # pult is the lesser of pst and psd. At surface, an arbitrary value is defined
        if pst <=psd:
            if pyDepth == 0:
                pu = 0.01
              
            else:
                pu = A * pst
              
        else:
            pu = A * psd
          
      # PySimple1 material formulated with pult as a force, not force/length, multiply by trib. length
        pult = pu * pEleLength

    #-------Brinch Hansen method-------
    elif puSwitch == 2:
      # pressure at ground surface
        cos_2 = math.cos(phi)
        
        tan_6 = math.tan(pi/4+phi/2) 
        
        sin_2 = math.sin(phi)
        sin_3 = math.sin(pi/4 + phi/2)
        
        exp_1 = math.exp((pi/2+phi)*tan_2)
        exp_2 = math.exp(-(pi/2-phi) * tan_2)
        
        Kqo = exp_1 * cos_2 * tan_6 - exp_2 * cos_2 * tan_1
        Kco = (1/tan_2) * (exp_1 * cos_2 * tan_6 - 1)

      # pressure at great depth
        exp_3 = math.exp(pi * tan_2)
        pow_3 = math.pow(tan_2,4)
        pow_4 = math.pow(tan_6,2)
        dcinf = 1.58 + 4.09 * (pow_3)
        Nc = (1/tan_2)*(exp_3)*(pow_4 - 1)
        Ko = 1 - sin_2
        Kcinf = Nc * dcinf
        Kqinf = Kcinf * Ko * tan_2

      # pressure at an arbitrary depth
        aq = (Kqo/(Kqinf - Kqo))*(Ko*sin_2/sin_3)
        KqD = (Kqo + Kqinf * aq * zbRatio)/(1 + aq * zbRatio)

      # ultimate lateral resistance
        if pyDepth == 0:
            pu = 0.01
        else:
            pu = gamma * pyDepth * KqD * b
               
      # PySimple1 material formulated with pult as a force, not force/length, multiply by trib. length
        pult  = pu * pEleLength
        
    #----------------------------------------------------------
    #  define displacement at 50% lateral capacity, y50
    #----------------------------------------------------------

    # values of y50 depend of the coefficent of subgrade reaction, k, which can be defined in several ways.
    #  for gwtSwitch = 1, k reflects soil above the groundwater table
    #  for gwtSwitch = 2, k reflects soil below the groundwater table
    #  a linear variation of k with depth is defined for kSwitch = 1 after API (1987)
    #  a parabolic variation of k with depth is defined for kSwitch = 2 after Boulanger et al. (2003)

    # API (1987) recommended subgrade modulus for given friction angle, values obtained from figure (approximate)

    ph = [28.8, 29.5, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0]    

    # subgrade modulus above the water table
    if gwtSwitch == 1:
        k = [10, 23, 45, 61, 80, 100, 120, 140, 160, 182, 215, 250, 275]
        
    else:
        k = [10, 20, 33, 42, 50, 60, 70, 85, 95, 107, 122, 141, 155]
    f=interpolate.interp1d(ph,k)
    khat=f(phiDegree)            

    # change units from (lb/in^3) to (kN/m^3)
    k_SIunits = khat * 271.45

    # define parabolic distribution of k with depth if desired (i.e. lin_par switch == 2)
    sigV = pyDepth * gamma

    if sigV == 0:
         sigV = 0.01
         
    if kSwitch == 2:
       # Equation (5-16), Boulanger et al. (2003)
        cSigma = math.pow(50 / sigV , 0.5)
       # Equation (5-15), Boulanger et al. (2003)
        k_SIunits = cSigma * k_SIunits

    # define y50 based on pult and subgrade modulus k

    # based on API (1987) recommendations, p-y curves are described using tanh functions.
    #  tcl does not have the atanh function, so must define this specifically

    #  i.e.  atanh(x) = 1/2*ln((1+x)/(1-x)), |x| < 1

    # when half of full resistance has been mobilized, p(y50)/pult = 0.5
    x = 0.5
    log_1 = math.log((1+x)/(1-x))
    atanh_value = 0.5 * log_1

    # need to be careful at ground surface (don't want to divide by zero)
    if pyDepth == 0.0:
        pyDepth = 0.01

    y50 = 0.5 * (pu/ A)/(k_SIunits * pyDepth) * atanh_value
    # return pult and y50 parameters
    outResult = []
    outResult.append(pult)
    outResult.append(y50)

return outResult