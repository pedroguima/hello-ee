# hello-ee

Simple Python web service that will provide you with three different responses according to the `GET` request. Examples:

```sh
$ curl http://$LB_IP:$PORT/hostname
hello-ee-deployment-6d6fc7bbd6-g4zwm
```

```sh
$ curl http://$LB_IP:$PORT/hello
Hello EE!!
```

```sh
$ curl http://$LB_IP:$PORT/test
Nothing's going on
```

## Build and Deploy steps

### Requirements

You'll need to install and configure the following packages before proceeding.

 * [Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/)
 * [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
 * [Docker](https://docs.docker.com/)


### Start Minikube

```sh
minikube start
```

### Configure the environment to use Minikube's Docker

```sh
eval $(minikube docker-env)
```

### Build the container image

```sh
export VERSION=v1
docker build . -t hello-ee-image:$VERSION
```

### Deploy to Kubernetes

Edit the Deployment docker image version in `k8s.yml` and run:

```sh
kubectl apply -f k8s.yml
```

### Test 

Check that everything is running properly:

```sh
kubectl get all
````

Get the IP of the service LoadBalancer (only applicable if you are using Minikube):

```sh
minikube service hello-ee-service
````

Query the service

```sh
$ curl http://$LB_IP:$PORT/hostname
```


### Scaling

Change the `k8s.yml` file according and run `kubectl apply` or run the following:

```sh
export NUM_REPLICAS=5
kubectl scale --replicas=$NUM_REPLICAS deployment/hello-ee-deployment
```

### Upgrading

Do the necessary changes to your code inside the `app` directory, build the docker image with the new version and run the following:

```sh
kubectl set image deployment hello-ee-deployment hello-ee=hello-ee-image:$NEW_VERSION
```


## File structure

### `app` directory

Contains the necessary code logic for the application.

### `Dockerfile`

Contains the instructions that Docker will run when building the image.

### `k8s.yml`

Kubernetes yml configurations. Contains the `deployment` and `service` definitions. 


## TODO

 - Integrate with a CI system that looks for code changes. When these happen, the code should get tested and a container image should be built automatically with a new version. This image should then be shipped to the k8s deployment. 

