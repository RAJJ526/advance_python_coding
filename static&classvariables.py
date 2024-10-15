# class School:
#     Name="left hand side"
#     def plass(self):
#         game="Right hand side"
#         print("first class")
# A=School()
# print(A.Name)
# B=School()
# B.plass()
# A.plass()

# class Salary:
#     # Public class variable
#     brij_salary = "12 lakh"
    
#     # Protected class variable (by convention)
#     _Raj_salary = "25 lakh"
    
#     # Private class variable (name mangling)
#     __kishan_salary = "10 lakh"
    
#     @classmethod
#     def display(cls):
#         # Accessing public class variable
#         print(f"Brij's salary (public): {cls.brij_salary}")
        
#         # Accessing protected class variable (by convention, not enforced)
#         print(f"Raj's salary (protected): {cls._Raj_salary}")
        
#         # Accessing private class variable (name mangling)
#         # To access the private variable, you need to use the class name
#         print(f"Kishan's salary (private): {cls._Salary__kishan_salary}")
        
#         print("Access modifiers")

# class BaseSalary:
#     # Protected class variable (by convention)
#     _base_salary = "20 lakh"
    
#     def display_base_salary(self):
#         print(f"Base salary (protected): {self._base_salary}")

# class DerivedSalary(BaseSalary):
#     def update_base_salary(self, new_salary):
#         # Modifying the protected class variable from a subclass
#         self._base_salary = new_salary
    
#     def display_base_salary(self):
#         print(f"Updated base salary (protected): {self._base_salary}")

# # Example usage
# base_obj = BaseSalary()
# base_obj.display_base_salary()  # Output: Base salary (protected): 20 lakh

# derived_obj = DerivedSalary()
# derived_obj.display_base_salary()  # Output: Updated base salary (protected): 20 lakh

# # Modifying the protected class variable from the subclass
# derived_obj.update_base_salary("25 lakh")
# derived_obj.display_base_salary()  # Output: Updated base salary (protected): 25 lakh

# # Direct access to the protected variable (not recommended but possible)
# print(derived_obj._base_salary)  # Output: 25 lakh



class Salary:
    # Public class variable
    base_salary = "20 lakh"
    
    # Protected class variable (by convention)
    _protected_salary = "25 lakh"
    
    # Private class variable (name mangling)
    __private_salary = "30 lakh"
    
    def display_salaries(self):
        print(f"Base salary (public): {self.base_salary}")
        print(f"Protected salary: {self._protected_salary}")
        print(f"Private salary: {self.__private_salary}")

# Example usage
employee = Salary()

employee._protected_salary = "27 lakh"



# Display all salaries using a method within the class
employee.display_salaries()



