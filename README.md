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


## Container build

Build your container image by running the following command:

```sh
docker build . -t hello-ee-image:$VERSION
```

## k8s deployment

Assuming Minikube and `kubectl` are properly configured:
```sh
kubectl apply -f k8s.yml
```

## Running the App

Check that everything is running properly:

```sh
kubectl get all
````

Get the IP of the service LoadBalancer (only applicable if you are using Minikube):

```sh
minikube service hello-ee-service
````

## Scaling the App

Change the `k8s.yml` file according and run `kubectl apply` or run the following:

```sh
kubectl scale --replicas=$NUM_REPLICAS deployment/hello-ee-deployment
```


## File structure

### `app` directory

Contains the necessary code logic for the application.

### `Dockerfile`

Contains the instructions that Docker will run when building the image.

### `k8s.yml`

Kubernetes yml configurations. Contains the `deployment` and `service` definitions. 


## TODO

 - Integrate with a CI system so the container image gets built and deployed automatically to k8s

