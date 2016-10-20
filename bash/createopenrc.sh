#!/bin/bash

#this function grabs the json_key to create the openrc file
function extract_json_key {
    RESULT=$(echo "$2" | sed "s/.*$1\": \"//g" | sed 's/".*//g')
    echo "$RESULT"
}

JSON_VENDOR_DATA=$(curl -s http://169.254.169.254/openstack/latest/vendor_data.json)
SITE=$(extract_json_key "site" "$JSON_VENDOR_DATA")
PROJECT_ID=$(extract_json_key "project_id" "$JSON_VENDOR_DATA")

# create openrc file; file structure taken from an openstack openrc file
# changing the file by prompting the user to input project name and username
cat > /tmp/openrc <<-EOM
#!/bin/bash

# To use an OpenStack cloud you need to authenticate against the Identity
# service named keystone, which returns a **Token** and **Service Catalog**.
# The catalog contains the endpoints for all services the user/tenant has
# access to - such as Compute, Image Service, Identity, Object Storage, Block
# Storage, and Networking (code-named nova, glance, keystone, swift,
# cinder, and neutron).
#
# *NOTE*: Using the 2.0 *Identity API* does not necessarily mean any other
# OpenStack API is version 2.0. For example, your cloud provider may implement
# Image API v1.1, Block Storage API v2, and Compute API v2.0. OS_AUTH_URL is
# only for the Identity API served through keystone.
export OS_AUTH_URL=https://chi.tacc.chameleoncloud.org:5000/v2.0

# With the addition of Keystone we have standardized on the term **tenant**
# as the entity that owns the resources.
export OS_TENANT_ID=3b3ea9fac1d740398501215181bebda3
read -r OS_PROJECT_INPUT
export OS_TENANT_NAME=\$OS_PROJECT_INPUT
export OS_PROJECT_NAME=\$OS_PROJECT_INPUT

# In addition to the owning entity (tenant), OpenStack stores the entity
# performing the action as the **user**.
echo "Please enter your Chameleon Username: "
read -r OS_USERNAME_INPUT
export OS_USERNAME=\$OS_USERNAME_INPUT

# With Keystone you pass the keystone password.
echo "Please enter your Chameleon Password: "
read -sr OS_PASSWORD_INPUT
export OS_PASSWORD=\$OS_PASSWORD_INPUT

# If your configuration has multiple regions, we set that information here.
# OS_REGION_NAME is optional and only valid in certain environments.
export OS_REGION_NAME="regionOne"
# Don't leave a blank variable, unset it if it was empty
if [ -z "\$OS_REGION_NAME" ]; then unset OS_REGION_NAME; fi
EOM

#source file
source /tmp/openrc
