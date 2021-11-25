//
//  matrix.h
//  Udacity Project 4 Matrix
//
//  Created by Aleksei Leshchankin on 25.11.2021.
//

#ifndef matrix_h
#define matrix_h
#include <vector>
#include <iostream>
#include <stdexcept>

// Header file for the Matrix class

/*
**  TODO:
**    Declare the following private variables:
**      a 2D float vector variable called grid
**      a vector size_type variable called rows
**      a vector size_type variable called cols
*/

class Matrix
{
    
    private:
        std::vector<std::vector<float> > grid;
        std::vector<float>::size_type rows;
        std::vector<float>::size_type cols;

    public:

        // constructor function declarations
        Matrix ();
        Matrix (std::vector< std::vector<float> >);

        // set and get function declarations
        void setGrid(std::vector< std::vector<float> >);

        std::vector< std::vector<float> > getGrid();
        std::vector<float>::size_type getRows();
        std::vector<float>::size_type getCols();

        // matrix function declarations
        Matrix matrix_transpose();
        Matrix matrix_addition(Matrix);
        void matrix_print();
    
};

#endif /* matrix_h */
