import sys

with open(sys.argv[1]) as file:
    cases = int(file.readline())
    case = 1
    while case <= cases:
        key = "case #" + str(case) + ":"
        value = ""

        g_buses = int(file.readline())
        line_2 = file.readline()
        temp_cities_range = line_2.split(" ")
        # If the last item of the split list is '\n' string literal delete it
        if temp_cities_range[-1] == '\n':
            del temp_cities_range[-1]
        # Convert the cities to integers
        for i in range(0,len(temp_cities_range)):
            temp_cities_range[i] = int(temp_cities_range[i])
        
        cities_range = []
        for i in range (0, len(temp_cities_range), 2):
            temp = [temp_cities_range[i], temp_cities_range[i+1]]
            cities_range.append(temp)

        P = int(file.readline())
        for i in range (0,P):
            city = int(file.readline())
            counter = 0
            for item in cities_range:
                if (city >= item[0] and city <= item[1]):
                    counter+=1
            value = value + " " + str(counter)
        print(key, value)
        # Increment the case
        case+=1
        # Read the empty line
        file.readline()