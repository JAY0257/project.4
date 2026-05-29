data=[]
while True:
    print("\nWelcome to the Data  Analyzer and Transformer program")
    print("Main Menu:")
    print("1.Input Data")
    print("2.Display Data Summary (Built-in Function)")
    print("3.Calcute Factorial (Recursion)")
    print("4.Filter Data by Threshold (Lambda FUnction)")
    print("5.Sort Data")
    print("6.Display Dataset Statistics (Return Multiple values)")
    print("7.Exit Program")
    choice=int(input("Enter Your choice"))

    if choice==1:
        print("\nStep 1: Input Data")
        numbers= input("Enter data for 1D array (separated by spaces):")
        data= [int(x) for x in numbers.split()]
        print("\nData has been stored successfully!")
    elif choice==2:
        if len(data)==0:
            print("\nNo data available! Please input data first.")
        else:
            print("Data Summary:")
            print("Total element:",len(data))
            print("Minimum value:",min(data))
            print("maximum value:",max(data))
            print("Sum of all values:",sum(data))
            print("Average value:",sum(data)/len(data))
    elif choice==3:
        def factorial(n):
            fact=1
            for i in range(1,n + 1):
                fact *=i
            return fact
        num=int(input("Enter a number to get its factiroal: "))
        print(f"factorial of {num} is: ",factorial(num))
    elif choice==4:
        if len(data)==0:
            print("no data available please input data first")
        else:
            threshold=int(input("Enter a threshold value to filter out data above this value: "))
            filter_data=list(filter(lambda x:x>threshold,data))
            print("filtered data(values >= 50): ",filter_data)
    elif choice==5:
        if len(data)==0:
            print("\n No data available")
        else:
            sorted_data=sorted(data)
            print("\nSorted Data (Ascending):", sorted_data)
            sorted_desc= sorted(data, reverse=True)
            print("Sorted Data (Descending):",sorted_desc)
    elif choice==6:
        if len(data)==0:
            print("\nNo data available!")
        else:
            minimum= min(data)
            maximum= max(data)
            total= sum(data)
            average= total / len(data)
            
            print("\nDataset Statistics")
            print("Minimum:", minimum)
            print("Maximum:", maximum)
            print("Total:",total)
            print("Average:",average)
        
    elif choice==7:
        print("Thank You for using the data analyzer and transformer program. Goodbye!")
        break          