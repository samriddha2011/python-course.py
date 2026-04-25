medical_cause = input("Enter the medical cause for your absence? (Y/N): ").strip().upper()
if medical_cause == 'Y':
    print("You are eligible for the exam.")
else:
    atten = int(input("Enter your attendance percentage: "))
    if atten >= 75:
        print("You are eligible for the exam.")
    else:
        print("You are not eligible for the exam.")