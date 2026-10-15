from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Grover's Search Circuit
n_qubits = 3
qc = QuantumCircuit(n_qubits)

# Initialize qubits in superposition
qc.h(range(n_qubits))

# Oracle: Mark the desired state |101⟩
qc.cz(0, 2)
qc.barrier()

# Grover Diffuser: Amplify the marked state
qc.h(range(n_qubits))
qc.x(range(n_qubits))
qc.h(n_qubits-1)
qc.mcx(list(range(n_qubits-1)), n_qubits-1)  # Multi-controlled X
qc.h(n_qubits-1)
qc.x(range(n_qubits))
qc.h(range(n_qubits))

# Measure
qc.measure_all()

# Simulate the circuit
backend = AerSimulator()
job = backend.run(transpile(qc, backend), shots=1024)
result = job.result()
counts = result.get_counts()

# Visualize the results
plot_histogram(counts)
plt.show()