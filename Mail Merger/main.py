with open("invited.txt", "r") as invited:
    names = invited.readlines()


with open("sample_mail.txt", "r") as sample_text:
    sample = sample_text.read()
    for name in names:
        final_name = name.strip("\n")
        letter = sample.replace("[name]", final_name)
        with open(f"Ready_mails\{final_name}_Invitation", "w") as ready:
            mails = ready.write(letter)
