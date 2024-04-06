import os

from domain.archive import Archive
from model.transparence import Transparency

if __name__ == '__main__':
    file_name = "dados_transparencia.csv"
    arquivo = Archive(file_name)
    if os.path.exists(file_name):
        data = arquivo.file_read()

        # Edita o segundo registro
        novo_registro = Transparency(
            "123456",
            "Novo nome órgão superior",
            "1234",
            "Novo nome órgão",
            "5678",
            "Nova nome unidade gestora",
            "Nova categoria econômica",
            "Nova origem receita",
            "Nova espécie receita",
            "Novo detalhamento",
            "1000.00",
            "900.00",
            "800.00",
            "80.00",
            "2023-03-10",
            "2024",
        )
        arquivo.editar_dados(data, 1, novo_registro)

        # Exclui o terceiro registro
        arquivo.excluir_dados(data, 2)

        # Grava os dados atualizados
        arquivo.gravar_dados(data)