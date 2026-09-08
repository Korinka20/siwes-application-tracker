import json
applications = []
while True:
  print("    SIWES APPLICATION TRACKER"    )
  print("1. Add Application")
  print("2. View Application")
  print("3. Search Applications")
  print("4. Update Applicaions")
  print("5. Save Applications")
  print("6. Exit")
  choice = input("Choose an Option: ")
  if choice=="1":
    # all your add application stuff
    company= input("Company:")
    role= input("Role:")
    status= input("Status:") 
   
    application = {     
      "Company": company,
      "Role": role,
      "Status": status
}
    applications.append(application)
    print("Application Added!")  
  elif choice =="2":
    print(applications)
  elif choice == "3":
    search = input("Enter Company name:")
    for application in applications:
        if application["Company"]. lower() == search.lower():
          print(application)
  elif choice == "4":
    company = input("Enter company name:")
    new_status = input("Enter new status:")
    for application in applications:
        if   application["Company"].lower() == company.lower(): 
          application["Status"]= new_status
          print("Status updated!")  
  elif choice =="5":
    with open("applications.json","w") as file:
      json.dump(applications,file, indent=4)
      print("Applications saved!")
  elif choice == "6":
     print("Goodbye!")
     break
  input("Press Enter to return to menu...")