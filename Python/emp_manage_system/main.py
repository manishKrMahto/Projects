import json
while True:
    option = int(
        input(
            "\n1. Add new Employee record \n2. Search any Employee record by empId \n3. show all employee records  \n4. Exit  \n\nchoose any option : "
        )
    )

    if option == 1:
        empId = input("enter Employee id : ")
        fullName = input("enter full name : ")
        jobTitle = input("enter job title : ")
        department = input("enter department : ")
        gender = input("enter gender : ")
        age = int(input("enter age : "))
        joining_date = input("enter joining date (like dd-mm-yyyy) : ")
        annual_salary = float(input("enter your annual salary : "))
        city_name = input("enter city name : ")
        country_name = input("enter country name : ")
        exit_date = input('enter exiting date if not present then type "No" :')

        # if the employee not left the job then
        if exit_date == "No":
            exit_date = None

        Employee_info = {
            "empId": empId,
            "fullName": fullName,
            "jobTitle": jobTitle,
            "department": department,
            "gender": gender,
            "age": age,
            "joining_date": joining_date,
            "annual_salary": annual_salary,
            "city_name": city_name,
            "country_name": country_name,
            "exit_date": exit_date,
        }

        f = open(
            "record.txt",
            "a",
        )

        # dict ko json me convert karke file me bhej diye
        f.write(json.dumps(Employee_info) + "\n")

        f.close()
    elif option == 2:
        search_by_empId = input("enter empId : ")

        f = open(
            "record.txt",
            "r",
        )
        # allLines ke pass list of each line strings h
        allLines = f.readlines()

        for line in allLines:
            # ab esko dict me convert kiye for better accessbility
            dic = json.loads(line)

            # jo empid match kiya usko print kiye
            if dic["empId"] == search_by_empId:
                print("\nrecord of", search_by_empId, " Employee ")

                for items in dic:
                    print(items, ":", dic[items])
        f.close()
    elif option == 3:
        f = open(
            "record.txt",
            "r",
        )
        allLines = f.readlines()

        i = 1
        for line in allLines:
            dic = json.loads(line)

            print(i, "th Empoyee record : \n", sep="", end="")
            i = i + 1
            for items in dic:
                print(items, ":", dic[items])
            print()
        f.close()
    elif option == 4:
        break
    else:
        print("option misMatched.....!!!")

