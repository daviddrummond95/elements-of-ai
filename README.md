# Elements of Artificial Intelligence Showcase

This repository represents numerous projects used in the Elements of Artifical Intelligence class. Many included template code, however,
the templates should be indicated using comments. Each project is descibed below, including which of the files contributed to the project.
All algorithms are implemented from scratch meaning that no packages like Scikit learn or Tensorflow are used. Pandas and Numpy are used.
Note, that some code may be omitted due to ownership by Indiana University. 

## IJK

IJK is a multiplayer variant on the popular mobile game 2048, developed by instructors for the EAI course. It is both random, turned-based,and competitive,
so to create an AI that could compete in this, I created an Expecti-mini-max algorithm. This algorithm is recursive and can run at any depth of future levels.
However, as a class, we had a competition and in order to compete, the AI had to complete its turn in some given time period. In this case, the AI could only anticipate
one move ahead before it had to make a decision. However, it turns out, this was sufficient to be undefeated in the competition. This project includes

- [IJK_AI.py](https://github.com/daviddrummond95/elements-of-ai/blob/master/IJK_AI.py)

## Yahtzee
This is a simplified version of Yahtzee using expected value theory. This is only a snipet of the code used in class with little documention. There is not much to see here.
## Maze Solver
Maze Solver is a classic Depth First Search algorithm. It is able to record its path in the space in readable terms.This code operates using:

- [map.txt](https://github.com/daviddrummond95/elements-of-ai/blob/master/map.txt)

- [maze_solver.py](https://github.com/daviddrummond95/elements-of-ai/blob/master/maze%20solver)

Unfortunately, I do not recall to what degree the skeleton code contribute to the overall implemenation on this one. It was my first ever coding project.

## Image Orientation Detection

This was the final for the class, we had to detect what orientation a picture was in. This was a group task and each of us were assigned a type of ML algorithm to
implement and my job was to implement a fully connected neural network with a single hidden layer. The code included in the repository is only the class that will
make the predictions on the image using the neural network. This will not load the image or preprocess the image.

- [nnet.py](https://github.com/daviddrummond95/elements-of-ai/blob/master/nnet.py)

## NRooks Variation

The classic N Rooks problem dictates that you place N rooks on a chess board such that no rook can attack another rook. In this variation, there are randomly placed 
barriers that the rooks can hide behind. This uses a heuristic A* search to find the maximum number of rooks that can be placed on the board.

- [nrooks_variant.py](https://github.com/daviddrummond95/elements-of-ai/blob/master/nrooks%20variant)
