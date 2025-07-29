class Inspection:
    def __init__(self, theater_name, location, date, inspector, safety_rating, remarks):
        self.theater_name = theater_name
        self.location = location
        self.date = date
        self.inspector = inspector
        self.safety_rating = safety_rating
        self.remarks = remarks

    def display(self):
        print(f"Theater: {self.theater_name}")
        print(f"Location: {self.location}")
        print(f"Date: {self.date}")
        print(f"Inspector: {self.inspector}")
        print(f"Safety Rating: {self.safety_rating}")
        print(f"Remarks: {self.remarks}")
        print("-" * 30)


class SafetyInspectionSystem:
    def __init__(self):
        self.inspections = []

    def create_inspection(self):
        theater_name = input("Enter theater name: ")
        location = input("Enter location: ")
        date = input("Enter inspection date (YYYY-MM-DD): ")
        inspector = input("Enter inspector name: ")
        safety_rating = input("Enter safety rating (1-10): ")
        remarks = input("Enter remarks: ")

        inspection = Inspection(theater_name, location, date, inspector, safety_rating, remarks)
        self.inspections.append(inspection)
        print("✅ Inspection added successfully.")

    def read_all_inspections(self):
        if not self.inspections:
            print("No inspections found.")
            return
        print("\n--- All Inspection Records ---")
        for idx, inspection in enumerate(self.inspections):
            print(f"ID: {idx}")
            inspection.display()

    def update_inspection(self):
        self.read_all_inspections()
        idx = int(input("Enter the ID of inspection to update: "))
        if 0 <= idx < len(self.inspections):
            print("Enter new details (leave blank to keep old value):")
            i = self.inspections[idx]

            new_name = input(f"Theater name ({i.theater_name}): ") or i.theater_name
            new_location = input(f"Location ({i.location}): ") or i.location
            new_date = input(f"Date ({i.date}): ") or i.date
            new_inspector = input(f"Inspector ({i.inspector}): ") or i.inspector
            new_rating = input(f"Rating ({i.safety_rating}): ") or i.safety_rating
            new_remarks = input(f"Remarks ({i.remarks}): ") or i.remarks

            self.inspections[idx] = Inspection(new_name, new_location, new_date, new_inspector, new_rating, new_remarks)
            print("✅ Inspection updated.")
        else:
            print("❌ Invalid ID.")

    def delete_inspection(self):
        self.read_all_inspections()
        idx = int(input("Enter the ID of inspection to delete: "))
        if 0 <= idx < len(self.inspections):
            del self.inspections[idx]
            print("✅ Inspection deleted.")
        else:
            print("❌ Invalid ID.")

    def run(self):
        while True:
            print("\n--- Theater Safety Inspection System ---")
            print("1. Add Inspection")
            print("2. View All Inspections")
            print("3. Update Inspection")
            print("4. Delete Inspection")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_inspection()
            elif choice == '2':
                self.read_all_inspections()
            elif choice == '3':
                self.update_inspection()
            elif choice == '4':
                self.delete_inspection()
            elif choice == '5':
                print("Exiting system.")
                break
            else:
                print("Invalid choice. Try again.")


# Run the system
system = SafetyInspectionSystem()
system.run()
