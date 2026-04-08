from qiskit.transpiler import generate_preset_pass_manager
from qiskit.circuit import Parameter

angle = Parameter("angle")  # undefined number

# Create and optimize circuit once
qc = QuantumCircuit(1)
qc.rx(angle, 0)
qc = generate_preset_pass_manager(
    optimization_level=3, basis_gates=["u", "cx"]
).run(qc)

qc.draw("mpl")
