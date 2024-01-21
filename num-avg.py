# Open the input file in read mode and output file in write mode
with open('input.txt', 'r') as infile, open('output4.txt', 'w') as outfile:
    # Read the numbers from the input file
    List = [int(num) for num in infile.read().split()]
    
    sum = 0  
    i = 0  
    while(i < len(List)):  
        sum = sum + List[i]  
        i = i + 1  
    avg = float(sum / len(List))  

    # Write the average to the output file
    outfile.write('The average is: ' + str(avg) + '\n')
