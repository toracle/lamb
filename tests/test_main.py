from pyaws_lambda import make_dist_package
from pyaws_lambda import deploy_functions



if __name__ == '__main__':
    make_dist_package()
    deploy_functions()
