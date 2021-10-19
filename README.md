# Quantum-Chess
 
A fun variant of chess where people can get a more intuitive sense of some aspects of quantum physics, and play without the aid of pre-existing chess theory.

Pieces randomly change states like a quantum particle making it a game of both wits and luck.

HOW TO RUN:
1. Install Python and its modules, including Pygame
2. Install Qiskit
3. Open Quantum Chess folder in your terminal.
4. Execute main.py using the python command.

HOW TO PLAY:
1. Each piece is assigned two states it may possibly take. Perchance, the two states are the same, the piece behaves like one in classical chess.
2. After each move, the pieces have an equal probabilty of settling into either state. This collapse can be determined by a classical pseudorandom generator, or by accessing the IBM quantum computer.