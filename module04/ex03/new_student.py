import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    """
    Generate a random string of 15 lowercase letters and digits.

    Returns:
        str: A string of 15 random characters.
    """

    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
    """
    A data class representing a student.

    This class automatically generates a student login and ID upon instantiation. 
    The student login is derived from the first letter of the student's name 
    concatenated with their nickname. The student ID is a randomly generated 
    15-character string.

    Attributes:
        name (str): The name of the student.
        nickname (str): The nickname of the student.
        active (bool): A flag indicating whether the student is active. 
                       Default is True. This field is not included in the 
                       generated __init__ method.
        login (str): The student's login ID, generated based on their name 
                     and nickname. This field is not included in the generated 
                     __init__ method.
        student_id (str): A unique identifier for the student, generated 
                          randomly. This field is not included in the generated 
                          __init__ method.

    Example:
        >>> student = Student("John", "Doe")
        >>> print(student.name)
        John
        >>> print(student.nickname)
        Doe
        >>> print(student.active)
        True
        >>> print(student.login)
        jDoe
        >>> print(student.student_id)  # Randomly generated ID
    """

    name: str
    surname: str
    active: bool = field(default=True, init=False)
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """
        Post-initialization processing to set the login attribute based on the
        student's name and nickname.
        """
        self.login = self.name[0].upper() + self.surname
