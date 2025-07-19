from qiskit import QuantumCircuit # QuantumCircuit: É como uma "placa de circuito" onde vamos montar nosso experimento quântico.
from qiskit_aer import AerSimulator # AerSimulator: É nosso "simulador quântico" (um computador clássico que imita um quântico).
from qiskit.quantum_info import Statevector # Statevector: Mostra o "estado mágico" do qubit (antes de medirmos).
from qiskit.visualization import plot_histogram, plot_bloch_multivector # plot_histogram e plot_bloch_multivector: Ferramentas para ver os resultados como gráficos.

## 1. Mostrar estado quântico
# Qubit: É como um bit normal (que pode ser 0 ou 1), mas com um "poder especial" - pode estar em 0 E 1 ao mesmo tempo (superposição).
qc = QuantumCircuit(1) # Cria circuito com 1 qubit

#Porta Hadamard (h): É como um "truque de mágica" que transforma o bit: (50% chance de ser 0, 50% de ser 1)
qc.h(0) # Aplica porta Hadamard no qubit 0


state = Statevector(qc)
print("Estado quântico:", state)
plot_bloch_multivector(state).savefig('estado_quantico.png')

# 2. Simular medições
qc.measure_all()
simulator = AerSimulator()
result = simulator.run(qc, shots=1000).result()
counts = result.get_counts()
print("\nResultados das medições:", counts)
plot_histogram(counts).savefig('medicoes.png')

print("\nGráficos salvos como 'estado_quantico.png' e 'medicoes.png'")