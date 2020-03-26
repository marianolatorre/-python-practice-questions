import pandas as pd
import numpy as np

def login_table(id_name_verified, id_password):
    """
    :param id_name_verified: (DataFrame) DataFrame with columns: Id, Login, Verified.   
    :param id_password: (numpy.array) Two-dimensional NumPy array where each element
                        is an array that contains: Id and Password
    :returns: (None) The function should modify id_name_verified DataFrame in-place. 
              It should not return anything.
    """ 
    id_name_verified.drop(columns=["Verified"], inplace=True)
    id_password_df = pd.DataFrame(id_password)
    id_password_df.columns = ["Id","Password"]
    return id_name_verified.merge(id_password_df, how="inner")

id_name_verified = pd.DataFrame([[1, "JohnDoe", True], [2, "AnnFranklin", False],[4, "Mariano", False]], columns=["Id", "Login", "Verified"])
id_password = np.array([[1, 987340123], [2, 187031122],[3, 123124]], np.int32)
print(login_table(id_name_verified, id_password))

