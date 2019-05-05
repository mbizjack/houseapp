def HPI_lookup(year, quarter):
	return None

def qtrPropValChange(month,quarter,year,propVal):
    if quarter < 4:
        CHPI = HPI_lookup(year,quarter)
        NHPI = HPI_lookup(year,quarter+1)
    else:
        CHPI = HPI_lookup(year,quarter)
        NHPI = HPI_lookup(year+1,1)

    return propVal * NHPI/CHPI

def amortization(principal,term,apr,state,yearstart):

	mo = 1
	yr = 1

	termMo = term
	aprMo = apr/12
	mopayment = (aprMo)*principal/(1-((1+aprMo)**(-termMo)))

	currentloan = principal
	intdue = currentloan*(apr/12)
	principalpaid = mopayment - intdue

	equity = principal - currentloan
	loanremain = currentloan-principalpaid
	propertyvalue = principal

	pPropTax = 0.025
	pFedTax = 0.25

	out = []
	outYr = []

	out.append([mo,yr,currentloan,equity,intdue,principalpaid,loanremain,propertyvalue])

	while mo <= termMo-1:
		currentloan = loanremain
		intdue = currentloan*aprMo

		if intdue + currentloan >= mopayment:
			currpmt = mopayment
		else:
			currpmt = intdue + currentloan

		equity = principal - loanremain

		principalpaid = currpmt - intdue
		loanremain = currentloan - principalpaid

		if mo % 12 == 0:
			intDueYr = 0
			principalPaidYr = 0
			
			for Xmo,Xyr,Xcurrentloan,Xequity,XintDue,XprincipalPaid,Xloanremain,Xpropertyvalue in out[-12:]:
				intDueYr = intDueYr+XintDue
				principalPaidYr = principalPaidYr + XprincipalPaid
			
			propertyTax = out[-1][7] * pPropTax
			fedTaxSave = pFedTax*(propertyTax + intDueYr)
			
			try:		
				outYr.append((yr,out[-12][2],intDueYr,principalPaidYr,out[-1][6],out[-1][7],propertyTax,fedTaxSave))
			except:
				outYr.append((yr,out[-len(out)][2],intDueYr,principalPaidYr,out[-1][6],out[-1][7],propertyTax,fedTaxSave))
				

			yr += 1

		mo += 1

		out.append([mo,yr,currentloan,equity,intdue,principalpaid,loanremain,propertyvalue])
		
		roundOutput = lambda x: round(x,2)

		out = [list(map(roundOutput,i)) for i in out]
		outYr = [list(map(roundOutput,i)) for i in outYr]

	return out,outYr