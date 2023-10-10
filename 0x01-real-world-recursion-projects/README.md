PART II: PROJECTS 201

10
FILE FINDER 203
The Complete File-Search Program . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 204
The Match Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205
Finding the Files with an Even Number of Bytes . . . . . . . . . . . . . . . . . . . . . 206
Finding the Filenames That Contain Every Vowel . . . . . . . . . . . . . . . . . . . . . 206
The Recursive walk() Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 207
Calling the walk() Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208
Useful Python Standard Library Functions for Working with Files . . . . . . . . . . . . . . . . 209
Finding Information About the File’s Name . . . . . . . . . . . . . . . . . . . . . . . . . 209
Finding Information About the File’s Timestamps . . . . . . . . . . . . . . . . . . . . . 210
Modifying Your Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 212
Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213
Further Reading . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213




11
MAZE GENERATOR 215
The Complete Maze-Generator Program . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 216
Setting Up the Maze Generator’s Constants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221
Creating the Maze Data Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 222
Printing the Maze Data Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223
Using the Recursive Backtracker Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 225
Starting the Chain of Recursive Calls . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 228
Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 229
Further Reading . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 229

12
SLIDING-TILE SOLVER 231
Solving 15-Puzzles Recursively . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232
The Complete Sliding-Tile Solver Program . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 234
Setting Up the Program’s Constants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243
Representing the Sliding-Tile Puzzle as Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243
Displaying the Board . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244
Creating a New Board Data Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . 245
Finding the Coordinates of the Blank Space . . . . . . . . . . . . . . . . . . . . . . . . 245
Making a Move . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246
Undoing a Move . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247
Setting Up a New Puzzle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 248
Recursively Solving the Sliding-Tile Puzzle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 251
The solve() Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 251
The attemptMove() Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253
Contents in Detail   xiii
Starting the Solver . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 255
Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 256
Further Reading . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 257


13
FRACTAL ART MAKER 259
The Built-in Fractals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 260
The Fractal Art Maker Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261
The Complete Fractal Art Maker Program . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 263
Setting Up Constants and the Turtle Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . 267
Working with the Shape-Drawing Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 267
The drawFilledSquare() Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 268
The drawTriangleOutline() Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270
Using the Fractal Drawing Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 271
Setting Up the Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 272
Using the Specifications Dictionary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 272
Applying the Specifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275
Creating the Example Fractals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 277
Four Corners . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 277
Spiral Squares . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 277
Double Spiral Squares . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278
Triangle Spiral . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278
Conway’s Game of Life Glider . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278
Sierpiński Triangle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279
Wave . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279
Horn . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279
Snowflake . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 280
Producing a Single Square or Triangle . . . . . . . . . . . . . . . . . . . . . . . . . . . . 280
Creating Your Own Fractals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 281
Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 282
Further Reading . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 282


14
DROSTE MAKER 283
Installing the Pillow Python Library . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 284
Painting Your Image . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 285
The Complete Droste Maker Program . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 286
Setting Up . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 288
Finding the Magenta Area . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 289
Resizing the Base Image . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 291
Recursively Placing the Image Within the Image . . . . . . . . . . . . . . . . . . . . . . . . . . . . 294
