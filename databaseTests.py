from Database import Database

def main():
    #Setup
    db = Database()
    db.setup()

    #User Commands
    db.addUser("Suyash", 231)
    print(db.getChatID("Suyash"))
    print(db.getUsername(231))
    print(db.getChatID("Suysdash"))
    print(db.getUsername(12223))

    # db.addEntryToTotals("Suyash", "Haozhe", 396.23)
    print(db.moneyOwed("Suyash", "Haozhe"))
    print(db.moneyOwed("Haozhe", "Suyash"))
    print(db.moneyOwed("Shitian", "Suyash"))
    print(db.moneyOwed("Haozhe", "Junkai"))
    db.addReceipt("Haozhe", "Junkai", "Firecracker Chicken", 4.50)
    db.addReceipt("Haozhe", "Junkai", "Dabao", 4.50)
    db.addReceipt("Junkai", "Haozhe", "Dabao", 60)
    db.addReceipt("Haozhe", "Junkai", "Dabao", 200)
    db.addReceipt("shitian95", "Haozhe321", "Dabao", 200)

    print("Self-history:")
    db.selfHistory("Junkai")


    db.history("Junkai")

    db.hasNotPaid("Haozhe")
    db.hasNotPaid("Junkai")
    db.hasNotPaid("shitian95")
    db.owesMoneyTo("Suyash")
    db.hasNotPaid("Haozhe")
    db.hasNotPaid("Junkai")
    db.hasNotPaid("Suyash")

    db.printTable("receipt")
    print(" ")
    db.paidEverything("Haozhe", "Shitian")
    print("  ")

    db.transactionHistory("Haozhe", "Junkai")

    print(" ")
    db.printTable("total")


if __name__ == '__main__':
    main()
