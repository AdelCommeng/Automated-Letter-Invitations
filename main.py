list_of_names=[]
#NOTE: the file path below will differ for everyone.
with open("Input/Names/invited_names.txt") as name_file:
    data_file=name_file.readlines()
    for x in data_file:
        list_of_names.append(x.strip())
    print(list_of_names)
for name in list_of_names:
    with open(f"Input/Letters/starting_letter.txt",) as letter_file:
        content=letter_file.read()
        content=content.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt","w") as output_file:
        output_file.write(content)
