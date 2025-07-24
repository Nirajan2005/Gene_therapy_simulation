import random

class Vector:
    def __init__(self, name, risk, targeting, success_rate, suitable_organs):
        self.name = name
        self.risk = risk
        self.targeting = targeting
        self.success_rate = success_rate
        self.suitable_organs = suitable_organs

    def suitability_hint(self, organ):
        if organ.lower() not in [o.lower() for o in self.suitable_organs]:
            print(f"⚠️ Poor targeting efficiency for {organ} tissues with {self.name}.")

    def deliver_gene(self, organ, mutation_type):
        print(f"\nDelivering gene using {self.name} to {organ}...")
        print(f"Mutation Type: {mutation_type}")
        print(f"Risk Factors: {self.risk}")
        print(f"Tissue Targeting: {self.targeting}")
        print(f"Edit Success Rate: {self.success_rate*100}%")
        success = random.random() < self.success_rate
        if success:
            if mutation_type == "Insert":
                print("✅ Gene inserted successfully!")
            elif mutation_type == "Replace":
                print("✅ Gene replaced successfully!")
            elif mutation_type == "Silence":
                print("✅ Gene silenced successfully!")
            else:
                print("✅ Gene delivery successful!")
        else:
            print("❌ Gene delivery failed.")

def main():
    vectors = {
        "1": Vector(
            "Retrovirus",
            "Insertional mutagenesis, immune response",
            "Dividing cells (e.g., bone marrow)",
            0.7,
            ["bone marrow", "blood", "immune system"]
        ),
        "2": Vector(
            "Adenovirus",
            "Strong immune response, transient expression",
            "Wide range, including non-dividing cells",
            0.5,
            ["lung", "liver", "muscle", "eye"]
        ),
        "3": Vector(
            "Lipid Nanoparticle (LNP)",
            "Low immunogenicity, off-target delivery",
            "Liver, some other tissues",
            0.6,
            ["liver"]
        )
    }

    organs = ["brain", "muscle", "liver", "lung", "eye", "bone marrow", "blood", "immune system"]
    mutation_types = ["Insert", "Replace", "Silence"]

    print("🧪 Gene Therapy Delivery Simulation V2")
    print("Choose a disease/target organ:")
    for idx, organ in enumerate(organs, 1):
        print(f"{idx}. {organ.capitalize()}")
    organ_choice = input("Enter the number of your choice: ").strip()
    organ = organs[int(organ_choice)-1] if organ_choice.isdigit() and 1 <= int(organ_choice) <= len(organs) else "unknown"

    print("\nChoose a vector type:")
    print("1. Retrovirus")
    print("2. Adenovirus")
    print("3. LNP (Lipid Nanoparticle)")
    vector_choice = input("Enter the number of your choice: ").strip()

    print("\nChoose mutation type:")
    for idx, mtype in enumerate(mutation_types, 1):
        print(f"{idx}. {mtype}")
    mutation_choice = input("Enter the number of your choice: ").strip()
    mutation_type = mutation_types[int(mutation_choice)-1] if mutation_choice.isdigit() and 1 <= int(mutation_choice) <= len(mutation_types) else "Insert"

    if vector_choice in vectors:
        vectors[vector_choice].suitability_hint(organ)
        vectors[vector_choice].deliver_gene(organ, mutation_type)
    else:
        print("Invalid vector choice.")

if __name__ == "__main__":
    main()