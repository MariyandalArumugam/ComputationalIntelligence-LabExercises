def get_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val >= 0:
                return val
            else:
                print("Enter positive value!")
        except:
            print("Invalid input!")


# -------------------------------
# 1. SIMPLE PROBABILITY (DICE)
# -------------------------------
def simple_probability():
    print("\n--- Simple Probability (Dice) ---")

    total_outcomes = get_int("Enter total outcomes of die: ")
    even_count = get_int("Enter number of even outcomes: ")
    greater4_count = get_int("Enter number of outcomes > 4: ")

    p_even = even_count / total_outcomes
    p_greater4 = greater4_count / total_outcomes

    print("\nP(Even) =", p_even)
    print("P(Number > 4) =", p_greater4)


# -------------------------------
# 2. BAYES THEOREM
# -------------------------------
def bayes_theorem():
    print("\n--- Bayes Theorem ---")

    pS = get_prob("Enter P(S) (Prior - student studies): ")
    pP = get_prob("Enter P(P) (Overall pass probability): ")
    pP_given_S = get_prob("Enter P(P | S) (Conditional): ")

    if pP == 0:
        print("Cannot compute Bayes!")
        return

    pS_given_P = (pP_given_S * pS) / pP

    print("\nP(S | P) =", pS_given_P)
    print("(Conditional Probability using Bayes Theorem)")


# -------------------------------
# 3. JOINT PROBABILITY (A, B, C)
# -------------------------------
def joint_probability():
    print("\n--- Joint Probability Table (A, B, C) ---")
    print("Enter frequency values (like given table)\n")

    # A row
    A_B_C = get_int("A, B, C: ")
    A_B_nC = get_int("A, B, ~C: ")
    A_nB_C = get_int("A, ~B, C: ")
    A_nB_nC = get_int("A, ~B, ~C: ")

    # ~A row
    nA_B_C = get_int("~A, B, C: ")
    nA_B_nC = get_int("~A, B, ~C: ")
    nA_nB_C = get_int("~A, ~B, C: ")
    nA_nB_nC = get_int("~A, ~B, ~C: ")

    total = (A_B_C + A_B_nC + A_nB_C + A_nB_nC +
             nA_B_C + nA_B_nC + nA_nB_C + nA_nB_nC)

    print("\nTotal =", total)

    # Probabilities
    P_A = (A_B_C + A_B_nC + A_nB_C + A_nB_nC) / total
    P_B = (A_B_C + A_B_nC + nA_B_C + nA_B_nC) / total
    P_C = (A_B_C + A_nB_C + nA_B_C + nA_nB_C) / total

    # Conditional
    P_A_given_BC = A_B_C / (A_B_C + nA_B_C) if (A_B_C + nA_B_C) != 0 else 0
    P_B_given_A = (A_B_C + A_B_nC) / (A_B_C + A_B_nC + A_nB_C + A_nB_nC)

    print("\n--- Results ---")
    print("P(A) =", P_A, "(Prior Probability)")
    print("P(B) =", P_B, "(Prior Probability)")
    print("P(C) =", P_C, "(Prior Probability)")
    print("P(A | B, C) =", P_A_given_BC, "(Conditional Probability)")
    print("P(B | A) =", P_B_given_A, "(Conditional Probability)")


# -------------------------------
# MAIN MENU
# -------------------------------
def main():
    while True:
        print("\n====== MENU ======")
        print("1. Simple Probability (Dice)")
        print("2. Bayes Theorem")
        print("3. Joint Probability (A, B, C)")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            simple_probability()

        elif choice == '2':
            bayes_theorem()

        elif choice == '3':
            joint_probability()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
