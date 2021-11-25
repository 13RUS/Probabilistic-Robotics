//
//  main.cpp
//  Udacity Lesson 4
//
//  Created by Aleksei Leshchankin on 25.11.2021.
//

#include <iostream>
#include "gaussian.hpp"

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    
    Gaussian mygaussian(30.0,100.0);
    Gaussian othergaussian(10.0,25.0);
    
    std::cout << "average " << mygaussian.getMu() << std::endl;
    std::cout << "evaluation " << mygaussian.evaluate(15.0) << std::endl;

    std::cout << "mul results variance " << mygaussian.mul(othergaussian).getSigma2() << std::endl;
    std::cout << "mul results average " << mygaussian.mul(othergaussian).getMu() << std::endl;

    std::cout << "add results variance " << mygaussian.add(othergaussian).getSigma2() << std::endl;
    std::cout << "add results average " << mygaussian.add(othergaussian).getMu() << std::endl;

    
    Gaussian gaussianone (40.0, 225.0);
    Gaussian gaussiantwo (35.6, 12.25);

    std::cout << gaussianone.evaluate(10.5) << "\n";
    std::cout << gaussianone.evaluate(55.4) << "\n";
    std::cout << gaussiantwo.evaluate(35.6) << "\n";
    std::cout << gaussiantwo.evaluate(29.4) << "\n";

    gaussianone.setMu(45.0);
    gaussiantwo.setSigma2(15.4);
    std::cout << gaussianone.getMu() << "\n";
    std::cout << gaussiantwo.getSigma2() << "\n";

    Gaussian gaussianthree = gaussianone.mul(gaussiantwo);
    std::cout << gaussianthree.getMu() << "\n";
    std::cout << gaussianthree.getSigma2() << "\n";

    Gaussian gaussianfour = gaussianone.add(gaussiantwo);
    std::cout << gaussianfour.getMu() << "\n";
    std::cout << gaussianfour.getSigma2() << "\n";
    
    return 0;
}
