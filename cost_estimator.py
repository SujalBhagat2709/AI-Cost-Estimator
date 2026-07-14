import json
import os


class CostEstimator:

    def __init__(self):

        self.file_name = "cost_history.json"

        self.history = []

        self.models = {

            "GPT-4o": {

                "input": 5.00,

                "output": 15.00

            },

            "GPT-4.1": {

                "input": 2.00,

                "output": 8.00

            },

            "GPT-4.1 Mini": {

                "input": 0.40,

                "output": 1.60

            },

            "GPT-5": {

                "input": 1.25,

                "output": 10.00

            },

            "GPT-5 Mini": {

                "input": 0.25,

                "output": 2.00

            },

            "Gemini 2.5 Flash": {

                "input": 0.30,

                "output": 2.50

            },

            "Claude Sonnet": {

                "input": 3.00,

                "output": 15.00

            }

        }

        self.load_history()

    def load_history(self):

        if os.path.exists(self.file_name):

            try:

                with open(

                    self.file_name,

                    "r",

                    encoding="utf-8"

                ) as file:

                    self.history = json.load(file)

            except:

                self.history = []

    def save_history(self):

        with open(

            self.file_name,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                self.history,

                file,

                indent=4

            )

    def list_models(self):

        print("\n========== AVAILABLE MODELS ==========\n")

        models = list(

            self.models.keys()

        )

        for number, model in enumerate(

            models,

            start=1

        ):

            print(

                f"{number}. {model}"

            )

        return models

    def estimate_cost(self):

        models = self.list_models()

        try:

            choice = int(

                input(

                    "\nSelect Model: "

                )

            )

        except ValueError:

            print("\nInvalid Choice.")

            return

        if choice < 1 or choice > len(models):

            print("\nInvalid Choice.")

            return

        model = models[choice - 1]

        input_tokens = int(

            input(

                "Input Tokens: "

            )

        )

        output_tokens = int(

            input(

                "Output Tokens: "

            )

        )

        requests = int(

            input(

                "Number of Requests: "

            )

        )

        input_cost = (

            input_tokens /

            1000000

        ) * self.models[model]["input"]

        output_cost = (

            output_tokens /

            1000000

        ) * self.models[model]["output"]

        total_cost = (

            input_cost +

            output_cost

        ) * requests

        average_cost = total_cost / requests

        result = {

            "model": model,

            "input_tokens": input_tokens,

            "output_tokens": output_tokens,

            "requests": requests,

            "total_cost": round(

                total_cost,

                6

            ),

            "average_cost": round(

                average_cost,

                6

            )

        }

        self.history.append(

            result

        )

        self.save_history()

        print("\n========== ESTIMATION ==========\n")

        print(

            "Model :", model

        )

        print(

            "Input Tokens :",

            input_tokens

        )

        print(

            "Output Tokens :",

            output_tokens

        )

        print(

            "Requests :",

            requests

        )

        print(

            "Estimated Cost : $",

            round(

                total_cost,

                6

            )

        )

        print(

            "Average Per Request : $",

            round(

                average_cost,

                6

            )

        )

    def view_history(self):

        if not self.history:

            print("\nNo Estimation History.")

            return

        print("\n========== COST HISTORY ==========\n")

        for number, item in enumerate(

            self.history,

            start=1

        ):

            print(

                "Estimate :", number

            )

            print(

                "Model :", item["model"]

            )

            print(

                "Requests :", item["requests"]

            )

            print(

                "Total Cost : $",

                item["total_cost"]

            )

            print(

                "Average Cost : $",

                item["average_cost"]

            )

            print("-" * 60)

    def statistics(self):

        if not self.history:

            print("\nNo Statistics Available.")

            return

        total_estimations = len(

            self.history

        )

        total_cost = sum(

            item["total_cost"]

            for item in self.history

        )

        total_requests = sum(

            item["requests"]

            for item in self.history

        )

        average = total_cost / total_estimations

        print("\n========== COST STATISTICS ==========\n")

        print(

            "Estimations :",

            total_estimations

        )

        print(

            "Total Requests :",

            total_requests

        )

        print(

            "Total Estimated Cost : $",

            round(

                total_cost,

                6

            )

        )

        print(

            "Average Estimate : $",

            round(

                average,

                6

            )

        )

    def delete_history(self):

        if not self.history:

            print("\nHistory Empty.")

            return

        choice = input(

            "\nDelete Entire History? (yes/no): "

        ).lower()

        if choice == "yes":

            self.history.clear()

            self.save_history()

            print("\nHistory Deleted Successfully.")

        else:

            print("\nCancelled.")