#include <iostream>
int main(int argc, char** argv){
    for(int i = 0; i < argc; i++){
        std::cout<<"Argument: " << argv[i] << std::endl;
    }
    return 1999999999;
}