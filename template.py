"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
label=""
first=0.0
second=0.0

label=input("label:")
first=float(input("first"))
second=float(input("second"))


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]
difference=second-first
print(difference)
percentage=first*100/second
print(percentage)

# 3. Decide a status and store it in a variable called status.
status=60
if percentage>=60:
 print("OVERLIMIT")
else :
    print("OK")
#    
# 4. Print the report.
#
print("=" * 34)
print(f"difference:{difference:.2f}")
print(f"percentage:{percentage:.2f}%")
print(f"status:{status}")

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
