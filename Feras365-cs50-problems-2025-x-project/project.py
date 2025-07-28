#ZekaChat Zeka-> intelligence

import csv


File="AI.csv"

def main():
    chatbot()
def write_csv(question: str,answer: str):
    #opening a csv open for writing
    with open(File,"a") as file:
        if file:
            writer=csv.DictWriter(file,fieldnames=["question","answer"])
            writer.writerow({"question":question.lower(),"answer":answer})
            return True
        else:
            return False

def read_csv(question: str) -> str:
    with open(File) as file:
        reader=csv.DictReader(file)
        for row in reader:
            if row["question"]==question:
                return row["answer"]

def chatbot():
    print(f"🤖 Chatbot: Salam! Ask me something (type 'exit' to stop).")
    while True:
        user: str = input("You: ").lower().strip()
        if user=="exit":
            print("🤖 Chatbot: Farewell, my Sultan!")
            break
        if  read_csv(user):
            print(f"🤖 Chatbot: {read_csv(user)}")
        else:
            response: str = input("🤖 Chatbot: I do not know the answer. What should I reply next time? ")
            write_csv(user,response)
            print("🤖 Chatbot: I have learned this for the future!")



if __name__=="__main__":
    main()











