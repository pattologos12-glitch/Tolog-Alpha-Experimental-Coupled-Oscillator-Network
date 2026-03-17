# Tolog-Alpha

Low-cost experimental platform for studying synchronization in oscillator networks

Tolog-Alpha is an open research project exploring synchronization dynamics in small lattices of coupled oscillators.
The project combines numerical simulations, simple analog electronics, and real-time visualization to study how local interactions between oscillators produce global patterns such as synchronization waves and phase structures.

## Architecture

The system is based on a 3×3 lattice of coupled oscillators.
Each oscillator interacts with its nearest neighbors through resistive coupling, allowing the network to exhibit collective synchronization behavior.

Each node includes:
- TL082 oscillator
- LM393 for zero-cross detection
- 74HC86 for phase comparison

Phase signals are acquired by:
- Arduino Mega 2560
- and processed for visualization and analysis

## Scientific Context

The project relates to research in:
- Synchronization
- Kuramoto Model
- Nonlinear Dynamics

The goal is not to claim a new theory, but to create an accessible experimental platform for exploring synchronization phenomena.

## Repository Structure

```
Tolog-Alpha
│
├── README.md
├── docs/
│   └── lattice_architecture_diagram.png
├── simulation/
│   └── lattice_simulation.py
├── hardware/
│   ├── concept.md
│   └── schematic.pdf
└── LICENSE
```

Goals of the Project
- explore synchronization in oscillator lattices
- build a low-cost experimental setup
- connect simulations with physical hardware
- provide an open platform for experimentation

## Open Research

This project is open and experimental.
Researchers, students, and hobbyists are welcome to:
- run simulations
- build the oscillator lattice
- test synchronization dynamics
- contribute improvements

## Author

Patrik – independent exploration of oscillator network dynamics.