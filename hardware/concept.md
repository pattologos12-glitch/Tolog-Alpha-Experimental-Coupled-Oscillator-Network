# Tolog-Alpha Hardware Concept

Tolog-Alpha is an experimental oscillator lattice designed to explore synchronization behavior in small coupled networks.

Each node of the lattice consists of:
- TL082 operational amplifier oscillator  
- LM393 comparator for zero-cross detection  
- 74HC86 XOR gate for phase comparison

Oscillators are coupled through resistive connections to create a 3×3 nearest-neighbor lattice.

Phase signals are digitized and sent to an Arduino Mega for data acquisition and real-time visualization.

The goal is to create a low-cost experimental platform for studying synchronization dynamics in oscillator networks.