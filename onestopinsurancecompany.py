# Program description: This program designed for OSIC allows
#                      for new insurance policy information
#                      to be entered and calculated for its
#                      customers.
# Written by:          Jillian Chiarot
# Date written:        July 23 - July 25 - 2023

# Import libraries.
import datetime
from datetime import timedelta
import time
from tqdm import tqdm
import FormatValues as FV

# Open the defaults file and read the values into variables.
f = open('OSICDef.dat', 'r')
NEXT_POLICY_NUM = int(f.readline())
BASIC_PREMIUM = float(f.readline())
ADD_CAR_DISCOUNT = float(f.readline())
EXTRA_LIABILITY_COVERAGE = float(f.readline())
GLASS_COST = float(f.readline())
LOANER_CAR_COST = float(f.readline())
HST_RATE = float(f.readline())
PROCESSING_FEE = float(f.readline())
f.close()

# Main program.
CurrDate = datetime.datetime.now()

# Program inputs.

while True:
    CustFirstName = input("Enter the customer's first name: ").title()
    CustLastName = input("Enter the customer's last name: ").title()
    StAdd = input("Enter the address: ").title()
    City = input("Enter the city: ").title()

    ProvincesList = ['AB', 'BC', 'MB', 'NB', 'NL', 'NT', 'NS', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']

    while True:

        Province = input("Enter the province (QQ): ").upper()

        if Province == "":
            print("Error - Province cannot be blank.")
        elif len(Province) != 2:
            print("Error - Province must be two characters (QQ).")
        elif Province not in ProvincesList:
            print("Error - Must enter a valid province.")
        else:
            break

    PostalCode = input("Enter the postal code (Q1Q 1Q1): ").upper()
    PhoneNum = input("Enter the phone number (111-111-1111): ")
    NumCarInsured = int(input("Enter the number of cars being insured: "))

    ExtraLiability = input("Would you like extra liability up to $1,000,000 (Y / N): ").upper()
    if ExtraLiability == "Y":
        ExtraLiabilityCoverageCost = EXTRA_LIABILITY_COVERAGE * NumCarInsured
        ExtL = "Yes"
    else:
        ExtraLiabilityCoverageCost = 0
        ExtL = "No"

    GlassCoverage = input("Would you like glass coverage (Y / N): ").upper()
    if GlassCoverage == "Y":
        GlassCoverageCost = GLASS_COST * NumCarInsured
        Glass = "Yes"
    else:
        GlassCoverageCost = 0
        Glass = "No"

    LoanerCar = input("Would you like a loaner car (Y / N): ").upper()
    if LoanerCar == "Y":
        LoanerCarCoverageCost = LOANER_CAR_COST * NumCarInsured
        Loan = "Yes"
    else:
        LoanerCarCoverageCost = 0
        Loan = "No"

    PayMethodList = ['Full', 'Monthly']

    while True:
        PayMethod = input("Would you like to pay in full or monthly: ").title()

        if PayMethod == "":
            print("Error - Payment method cannot be blank.")
        elif PayMethod not in PayMethodList:
            print("Error - Payment method must be either full or monthly.")
        else:
            break

# Other calculations.
    InsurancePremium = BASIC_PREMIUM + ((NumCarInsured - 1) * (BASIC_PREMIUM * .75))
    TotExtraCosts = ExtraLiabilityCoverageCost + GlassCoverageCost + LoanerCarCoverageCost
    TotInsurancePremium = InsurancePremium + TotExtraCosts
    HST = HST_RATE * TotInsurancePremium
    TotCost = TotInsurancePremium + HST
    InvDate = CurrDate
    NextMonth = CurrDate + timedelta(days=30)
    NextPayDay = NextMonth.replace(day=1)

# Concatenation.
    CustFullName = CustFirstName + " " + CustLastName
    PostalCodeCont = PostalCode[0:3] + " " + PostalCode[3:6]
    AddCont = City + ", " + Province + ", " + PostalCodeCont

# Print receipt statement.
    print()
    print("       ONE STOP INSURANCE COMPANY")
    print("Where you spend all your money in one place!")
    print("============================================")
    print(f" Invoice date:   {FV.FDateS(InvDate)}")
    print(f" Policy number:  {NEXT_POLICY_NUM:<4d}")
    print(f" Customer name:  {CustFullName:<20s}")
    print(f" Address:        {StAdd:<10s}")
    print(f"{AddCont:>33s}")
    print(f" Phone number:   {PhoneNum:<12s}")
    print(f"--------------------------------------------")
    print(f" Number of cars being insured:             {NumCarInsured:<1d}")
    print(f"--------------------------------------------")
    print(f" Extra liability:   {ExtL:<3s}            {FV.FDollar2(ExtraLiabilityCoverageCost):<10s}")
    print(f" Glass coverage:    {Glass:<3s}            {FV.FDollar2(GlassCoverageCost):<10s}")
    print(f" Loaner car:        {Loan:<3s}            {FV.FDollar2(LoanerCarCoverageCost):<10s}")
    print(f" Total extra costs:                {FV.FDollar2(TotExtraCosts):<10s}")
    print(f" Insurance premium:                {FV.FDollar2(InsurancePremium):<10s}")
    print(f" Total insurance premium:          {FV.FDollar2(TotInsurancePremium):<10s}")
    print("============================================")
    print(f" HST:                              {FV.FDollar2(HST):<10s}")
    print(f" Total cost:                       {FV.FDollar2(TotCost):<10s}")

    if PayMethod == "Full":
        MonthlyPayment = ""
    else:
        MonthlyPayment = (PROCESSING_FEE + TotCost) / 8
        print(f"--------------------------------------------")
        print(f" Monthly payment processing fee:   {FV.FDollar2(PROCESSING_FEE):<7s}")
        print(f" 8 monthly payments of:            {FV.FDollar2(MonthlyPayment):<10s}")
        print(f" Next payment date:               {FV.FDateS(NextPayDay)}")

    print()
    print()
    print("Saving data - please wait")
    # Processing bar
    for _ in tqdm(range(20), desc="Processing", unit="ticks", ncols=100, bar_format="{desc}  {bar}"):
        time.sleep(.1)
    print("Policy information processed and saved.")
    time.sleep(1)

    # Write the policy number, all input values and total insurance premium to Policies.dat
    f = open('Policies.dat', 'a')
    f.write(f"{NEXT_POLICY_NUM},")
    f.write(f"{FV.FDateS(InvDate)},")
    f.write(f"{CustFirstName},")
    f.write(f"{CustLastName},")
    f.write(f"{StAdd},")
    f.write(f"{City},")
    f.write(f"{Province},")
    f.write(f"{PostalCode},")
    f.write(f"{PhoneNum},")
    f.write(f"{NumCarInsured},")
    f.write(f"{ExtraLiability},")
    f.write(f"{GlassCoverage},")
    f.write(f"{LoanerCar},")
    f.write(f"{PayMethod},")
    f.write(f"{TotInsurancePremium}\n")
    f.close()

    # Increase policy number by 1.
    NEXT_POLICY_NUM += 1

    Continue = input("Would you like to process another policy (Y / N): ").upper()
    if Continue == "N":
        print("Thank you for using One Stop Insurance!")
        break

# Write the current values back to the defaults file.
f = open('OSICDef.dat', 'w')
f.write(f"{NEXT_POLICY_NUM}\n")
f.write(f"{BASIC_PREMIUM}\n")
f.write(f"{ADD_CAR_DISCOUNT}\n")
f.write(f"{EXTRA_LIABILITY_COVERAGE}\n")
f.write(f"{GLASS_COST}\n")
f.write(f"{LOANER_CAR_COST}\n")
f.write(f"{HST_RATE}\n")
f.write(f"{PROCESSING_FEE}\n")
f.close()