# =================================  TESTY  ===================================
# Testy do tego pliku zostały podzielone na dwie kategorie:
#
#  1. `..._invalid_input`:
#     - Sprawdzające poprawną obsługę nieprawidłowych danych wejściowych.
#
#  2. `..._correct_solution`:
#     - Weryfikujące poprawność wyników dla prawidłowych danych wejściowych.
# =============================================================================
import numpy as np


def spare_matrix_Abt(m: int, n: int) -> tuple[np.ndarray, np.ndarray] | None:
    """Funkcja tworząca zestaw składający się z macierzy A (m,n) i
    wektora b (m,) na podstawie pomocniczego wektora t (m,).

    Args:
        m (int): Liczba wierszy macierzy A.
        n (int): Liczba kolumn macierzy A.

    Returns:
        (tuple[np.ndarray, np.ndarray]):
            - Macierz A o rozmiarze (m,n),
            - Wektor b (m,).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    if not isinstance(m, int) or not isinstance(n, int) or n<1 or m<1:
        return None

    wek = np.linspace(0,1,num=m)
    b = np.cos(4*wek)
    A = np.vander(wek, n, increasing=True)

    return (A ,b)
    pass


def square_from_rectan(
    A: np.ndarray, b: np.ndarray
) -> tuple[np.ndarray, np.ndarray] | None:
    
    if not isinstance(A, np.ndarray) or not isinstance(b, np.ndarray):
        return None
    if b.ndim != 1:
        return None
    if A.shape[0] != b.shape[0]:
        return None
    if A.ndim != 2:
        return None

    A_new = np.matmul(A.T, A)
    b_new = np.matmul(A.T, b)
    return (A_new, b_new)

def residual_norm(A: np.ndarray, x: np.ndarray, b: np.ndarray) -> float | None:
    if not isinstance(A, np.ndarray) or not isinstance(x, np.ndarray) or not isinstance(b, np.ndarray):
        return None
    
    if A.ndim != 2 or x.ndim != 1 or b.ndim != 1:
        return None
    if A.shape[1] != x.shape[0]:
        return None
    if A.shape[0] != b.shape[0]:
        return None

    Ax = np.dot(A, x)
    
    residuum = b - Ax
    
    norma = np.linalg.norm(residuum)
    
    return norma
    pass
