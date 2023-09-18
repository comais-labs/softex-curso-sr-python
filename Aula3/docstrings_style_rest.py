"""
Exemplo do uso de docstrings: rest style
"""
"""
Este é um comentário de múltiplas 
linhas a nível de módulo.
"""

class Exemplo1:
    """
    Classe com exemplo do uso de docstrings.

    .. note::
        Esta é uma nota sobre a classe.

    .. warning::
        Esta é um aviso sobre a classe.
    """

    def __init__(self, type_id: int, name: str) -> None:
        """
        Cria objetos do Tipo Exemplo1.

        :param type_id: O ID do tipo do objeto.
        :type type_id: int
        :param name: O nome associado ao objeto.
        :type name: str
        """
        pass
