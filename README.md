

### user
```commandline
python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/user.proto
```

### router
```commandline
python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/route_guide.proto
```