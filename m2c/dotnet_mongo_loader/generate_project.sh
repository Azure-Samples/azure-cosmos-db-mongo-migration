#!/bin/bash

# Use the dotnet CLI to bootstrap this dotnet console app project.
# See https://www.nuget.org/packages/MongoDB.Driver/
#
# Chris Joakim, Microsoft, July 2021

dotnet new console

dotnet add package MongoDB.Driver
dotnet add package Azure.Storage.Blobs
dotnet add package Microsoft.Azure.Cosmos

cat dotnet_mongo_loader.csproj

dotnet list package
dotnet restore
dotnet build
dotnet run

echo ''
echo 'done'
