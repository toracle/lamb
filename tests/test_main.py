from serverless import make_dist_package
from serverless import deploy_functions



if __name__ == '__main__':
    make_dist_package()
    deploy_functions()
