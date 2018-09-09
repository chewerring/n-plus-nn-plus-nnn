#Read the files
inputfile = open("numin.txt", "r")
outputfile = open("numout.txt", "w")

#Get the value as an integer
value = inputfile.read().split()
value = int(value[0])

#Calculate

#Solution 1
tenvalue = value * 11
thousandvalue = value * 111
answer = value + tenvalue + thousandvalue

#Solution 2
#answer = 123 * value

#Output the answer
outputfile.write(str(answer))

#Close the files
inputfile.close()
outputfile.close()