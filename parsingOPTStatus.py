def count(lines):
    received = 0
    processed = 0
    rejected = 0
    for line in lines:
        if "<h1>" in line:
            status = line.replace('<h1>','').replace('</h1>','')
            if 'Received' in status:
                received += 1
            elif "Rejected" in status:
                rejected += 1
            else:
                processed += 1
    return (received, rejected, processed)
f1 = open('before.txt')
f2 = open('after.txt')
lines1 = f1.readlines()
lines2 = f2.readlines()
(received, rejected, processed) = count(lines1)
print("Case received before me: ", received)
print("Processed before me: ",processed)

(received, rejected, processed) = count(lines2)
print("Case received afer me: ", received)
print("Processed afer me: ",processed)
