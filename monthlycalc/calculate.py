

def amortization(principal,term,apr):

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

	out = []

	out.append([mo,yr,currentloan,equity,intdue,principalpaid,loanremain])

	while mo <= termMo-1:
		currentloan = loanremain
		intdue = currentloan*aprMo

		if intdue + currentloan >= mopayment:
			currpmt = mopayment
		else:
			currpmt = intdue + currentloan

		principalpaid = currpmt - intdue
		loanremain = currentloan - principalpaid

		equity = principal - loanremain

		if mo % 12 == 0:
			yr += 1

		mo += 1

		out.append([mo,yr,currentloan,equity,intdue,principalpaid,loanremain])
		
		roundOutput = lambda x: round(x,2)

		out = [list(map(roundOutput,i)) for i in out]

	return out