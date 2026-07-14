from cost_estimator import CostEstimator


class EstimationStudio:

    def __init__(self):

        self.estimator = CostEstimator()

    def display_menu(self):

        while True:

            print("\n")

            print("=" * 60)

            print("              AI COST ESTIMATOR")

            print("=" * 60)

            print("1. Estimate AI Cost")

            print("2. View Cost History")

            print("3. Cost Statistics")

            print("4. Delete History")

            print("5. Exit")

            choice = input("\nEnter Choice: ").strip()

            if choice == "1":

                try:

                    self.estimator.estimate_cost()

                except ValueError:

                    print("\nInvalid Input.")

            elif choice == "2":

                self.estimator.view_history()

            elif choice == "3":

                self.estimator.statistics()

            elif choice == "4":

                self.estimator.delete_history()

            elif choice == "5":

                print("\nThank You For Using AI Cost Estimator!")

                break

            else:

                print("\nInvalid Choice. Please Try Again.")


if __name__ == "__main__":

    studio = EstimationStudio()

    studio.display_menu()