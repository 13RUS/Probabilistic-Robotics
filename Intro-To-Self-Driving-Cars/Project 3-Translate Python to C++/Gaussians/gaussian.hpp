//
//  gaussian.hpp
//  Udacity Lesson 4
//
//  Created by Aleksei Leshchankin on 25.11.2021.
//

#ifndef gaussian_hpp
#define gaussian_hpp

#include <stdio.h>

#endif /* gaussian_hpp */

class Gaussian
{
    private:
        float mu, sigma2;

    public:
        
        // constructor functions
        Gaussian ();
        Gaussian (float, float);

        // change value of average and standard deviation
        void setMu(float);
        void setSigma2(float);

        // output value of average and standard deviation
        float getMu();
        float getSigma2();

        // functions to evaluate
        float evaluate (float);
        Gaussian mul (Gaussian);
        Gaussian add (Gaussian);
};
