Name = input("Enter your name: ")
Citizenship = input("Enter your natinality: ").lower()
Employment_status = input("Enter your employment status(Undergrad/Grad/employed): ").lower()
Scholarship_Enrolled = input("Are you enrolled in any scholarship: ").lower()
Academic_subject = input("enter 5 subjects separated by commas: ").split(",")
academic_qualification = [input(f"Enter grade for {subject}: ") for subject in Academic_subject]
print(academic_qualification)
#accepted_grade = ("A" in academic_qualification) and ("B" in academic_qualification)
accepted_grade = (academic_qualification == "A") and ( academic_qualification == "B")  
print(f"accepted grade {accepted_grade}")
eligibility = (Citizenship == "nigerian") or (Employment_status == "undergraduate") and (Scholarship_Enrolled == "no") and (accepted_grade == True)

print(f"Candidate:{Name}\nCitizenship:{Citizenship}\nEmployment Status:{Employment_status}\nEnrollment: {Scholarship_Enrolled}\nEligible: {eligibility}")