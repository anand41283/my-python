"""file handling

in python files are treated in two m0des as text or binary.The file may be in the text or binary format,and each line of
a file is ended with the specia; character.

hence, a file operation can be done in the following order.

->open a file
->read or write-performing operation
->close the file

opening file

python provides an open() function that accepts two argumnents, fil name and access mode in which the file is access.
The function returns a file object which can  be used to perform various operations like reading,writing,etc.

syntax:
file object=open(<file-name>,<access-mode>)

Access MOde

"r"-read- efault value.Opens a file reading,error if the file does not exist
"a"-Append-Opens a file for appending,creates the file if it does not exist
"w"-write-opens a file for writing,creates the file if it does not exist
"x"=create-creats the specified file,returns an error if the file exists
"t"-Text - default value.text mode
"b"-Binary-Binary mode(e g. images)"""

#opens the file ss.txt in read mode
fileptr=open("ss.txt","r")

if fileptr:
    print("file is opened successfully")
#closes The opened file 
fileptr.close()


"""
Reading the content of the file

1.read()
2.readline()-reads a single line
3.readlines() - file content as A list"""