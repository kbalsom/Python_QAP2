# A program for St. John's Marina & Yacht Club
# to prepare receipts for yearly fees.

# Written by Kara Balsom
# Date Written: February 1, 2022

# Define Constants:

HST_RATE = 0.15
EVEN_SITE_RATE = 80.00
ODD_SITE_RATE = 120.00
ALT_MEM_RATE = 5.00
SITE_CLEAN_RATE = 50.00
VID_SURV_RATE = 35.00
PROCESS_FEE = 59.99
CANCEL_FEE_RATE = 0.60
MON_DUE_STND = 75.00
MON_DUE_EXEC = 150.00

# User inputs and validations:

SiteNum = int(input("Enter Site Number: "))
MemName = input("Enter Member Name: ")
print()
StreetAdd = input("Enter Street Address: ")
City = input("Enter City: ")
Province = input("Enter Province (XX): ").upper()
Postal = input("Enter Postal Code (X1X 1X1): ").upper()
PhoneNum = input("Enter Home Phone Number (9999999999): ")
CellNum = input("Enter Cell Number (9999999999): ")
print()
while True:
    MemType = input("Enter Membership Type ( S / E ): ").upper()
    if MemType == "":
        print("Membership Type cannot be blank. Please enter S or E.")
    elif MemType != "S" and MemType != "E":
        print("Please enter S or E for Membership Type.")
    else:
        break

NumAltMem = int(input("Enter Number of Alternate Members: "))

while True:
    WeekClean = input("Weekly Cleaning Selected? ( Y / N ): ").upper()
    if WeekClean == "":
        print("Please enter Y if Weekly Cleaning was Selected, or N if Weekly Cleaning was not selected.")
    elif WeekClean != "Y" and WeekClean != "N":
        print("Please enter Y if Weekly Cleaning was Selected, or N if Weekly Cleaning was not selected.")
    else:
        break

while True:
    VidSurv = input("Video Surveillance Selected? ( Y / N ): ")
    if VidSurv == "":
        print("Please enter Y if Video Surveillance was selected, or N if Video Surveillance was not selected.")
    elif VidSurv.upper()!= "Y" and VidSurv.upper()!= "N":
        print("Please enter Y if Video Surveillance was selected, or N if Video Surveillance was not selected.")
    else:
        break

# Perform required calculations:

if (SiteNum % 2) == 0:
    EvenOddSiteChrg = EVEN_SITE_RATE
else:
    EvenOddSiteChrg = ODD_SITE_RATE

AltMemChrg =  NumAltMem * ALT_MEM_RATE
SiteChrgTot = EvenOddSiteChrg + AltMemChrg


if WeekClean == "Y":
    SiteCleanChrg = SITE_CLEAN_RATE
else:
    SiteCleanChrg = 0

if VidSurv == "Y":
    VidSurvChrg = VID_SURV_RATE
else:
    VidSurvChrg = 0


ExtChrgTot = SiteCleanChrg + VidSurvChrg
SubTot = SiteChrgTot + ExtChrgTot
TaxTot = SubTot * HST_RATE
TotMonChrg = SubTot + TaxTot


if MemType == "S":
    MonDue = MON_DUE_STND
else:
    MonDue = MON_DUE_EXEC


TotMonFee = TotMonChrg + MonDue
YearFee = TotMonFee * 12
MonPay = (YearFee + PROCESS_FEE) / 12
CanFee = YearFee * CANCEL_FEE_RATE

# Print Outputs and format

print()
print("   St. John's Marina & Yacht Club")
print("        Yearly Member Receipt")
print()
print("_____________________________________")
print()
print("Client Name and Address:")
print()
print("{:<24s}".format(MemName))
print("{:<24s}".format(StreetAdd))
CityDsp = City + ","
print("{:<14s} {:<2s} {:<6s}".format(CityDsp, Province, Postal))
print()
print("Phone: {:<10s} (H)".format(PhoneNum))
print("Phone: {:<10s} (C)".format(CellNum))
print()
if MemType == "S":
    MemTypeDsp = "STANDARD"
else:
    MemTypeDsp = "EXECUTIVE"
print("Site #: {:>3d} Member type: {:<9s}".format( SiteNum, MemTypeDsp))
print()
print("Alternate members:              {:<2d}".format(NumAltMem))
if WeekClean == "Y":
    WeekCleanDsp = "YES"
else:
    WeekCleanDsp = "NO"
print("Weekly site cleaning:          {:>3s}".format(WeekCleanDsp))
if VidSurv == "Y":
    VidSurvDsp = "YES"
else:
    VidSurvDsp = "NO"
print("Video Surveillance:            {:>3s}".format(VidSurvDsp))
print()
SiteChrgTotDsp = "${:,.2f}".format(SiteChrgTot)
print("Site charges::           {:>9s}".format(SiteChrgTotDsp))
ExtChrgTotDsp = "${:,.2f}".format(ExtChrgTot)
print("Extra charges:            {:>8s}".format(ExtChrgTotDsp))
print("                      -------------")
SubTotDsp = "${:,.2f}".format(SubTot)
print("Subtotal:                {:>9s}".format(SubTotDsp))
TaxTotDsp = "${:,.2f}".format(TaxTot)
print("Sales tax (HST):          {:>8s}".format(TaxTotDsp))
print("                      -------------")
TotMonChrgDsp = "${:,.2f}".format(TotMonChrg)
print("Total monthly charges:   {:>9s}".format(TotMonChrgDsp))
MonDueDsp = "${:,.2f}".format(MonDue)
print("Monthly Dues:             {:>8s}".format(MonDueDsp))
print("                      -------------")
TotMonFeeDsp = "${:,.2f}".format(TotMonFee)
print("Total monthly fees:      {:>9s}".format(TotMonFeeDsp))
YearFeeDsp = "${:,.2f}".format(YearFee)
print("Total yearly fees:      {:>10s}".format(YearFeeDsp))
print()
MonPayDsp = "${:,.2f}".format(MonPay)
print("Monthly payment:         {:>9s}".format(MonPayDsp))
print()
print("___________________________________")
print()
print("Issued: YYYY-MM-DD")
print("HST Reg No: 549-33-5849-4720-9885")
print()
CanFeeDsp = "${:,.2f}".format(CanFee)
print("Cancellation Fee:        {:>9s}".format(CanFeeDsp))
