from pyaws_lambda import make_dist_package
from pyaws_lambda import deploy_functions



def main():
    make_dist_package()
    deploy_functions()
