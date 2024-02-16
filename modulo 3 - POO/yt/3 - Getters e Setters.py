class Alarme:
    def __init__(self, ativo=False):
        self._ativo = ativo

    def get_ativo(self):
        return self._ativo

    def set_ativo(self, novo_estado):
        if isinstance(novo_estado, bool):
            self._ativo = novo_estado
        else:
            raise ValueError("O estado do alarme deve ser um booleano.")

# Exemplo de uso
alarme = Alarme()
print("Estado inicial do alarme:", alarme.get_ativo())  # Saída: False

alarme.set_ativo(True)
print("Novo estado do alarme:", alarme.get_ativo())  # Saída: True

# Tentando definir um estado inválido
try:
    alarme.set_ativo("ativado")
except ValueError as e:
    print("Erro:", e)  # Saída: Erro: O estado do alarme deve ser um booleano.
