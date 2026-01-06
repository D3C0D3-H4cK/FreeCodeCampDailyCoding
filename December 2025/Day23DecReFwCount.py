def email_chain_count(subject):

    subject = subject.lower()
    markers = ["fw:", "fwd:", "re:"]
    counter = 0

    for m in markers:
        counter += subject.count(m)
    print(counter)
email_chain_count("Re: Fwd: Re: Fw: Re: Meeting Notes")