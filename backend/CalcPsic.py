from math import exp, log

#TBS = float(input("TBS: "))
#UR = float(input("UR: "))

def CalcPsic(TBS, UR):
	TBS = float(TBS)
	UR = float(UR)
	TBU = 0.1

	while True:
		TBU += 0.01
		kPA = float(101.325 * 1000)
		TBS_k = TBS + 273.15
		TBU_k = TBU + 273.15
		
		c1, c2, c3, c4, c5, c6, c7 = -5800.2206, 1.3914993, -0.048640239, 0.000041764768, -0.00000001445209, 0, 6.5459673
		PVS = exp((c1/TBS_k)+(c2)+ (c3*TBS_k) + (c4 * (TBS_k ** 2)) + (c5 * (TBS_k ** 3)) + (c6*(TBS_k ** 6)) + (c7*(log(TBS_k))))
		PPV = PVS * (UR/100)
		RMS = (0.62198) * (PVS/(kPA-PVS))
		RM = (0.62198) * (PPV/((kPA)-PPV))
		
		TPO = -35.957-(1.8726*log(PPV))+((1.1689*(log(PPV))**2))

		v = ((1/kPA)*287.055*TBS_k*(1+1.16078*RM))/(1+RM)
		p = 1/v
		
		PVS2 = exp((c1/TBU_k)+(c2)+ (c3*TBU_k) + (c4 * (TBU_k ** 2)) + (c5 * (TBU_k ** 3)) + (c6*(TBU_k ** 6)) + (c7*(log(TBU_k))))
		RMS2 = (0.62198) * (PVS2/(kPA-PVS2))

		h = (1.006*TBS) + RM * (2501 + (1.805*TBU))
		hs = (1.006*TBU) + RMS2 * (2501+1.805*TBU)
		ha = 4.186 * TBU

		equation = (hs-(h+ha*(RMS-RM)))
	  
		
		
		if round(equation,1) == 0:
		    values = {"PVS": PVS, "PPV": PPV, "RMS": RMS, "RM": RM, "TPO": TPO, "v": v, "p": p, "h": h, "TBU": TBU}
		    for i in values:
		        if values[i] < 1:
		            print(f'{i}: {round(values[i],4)}')

		        else:
		            print(f'{i}: {round(values[i], 2)}')
		    break


