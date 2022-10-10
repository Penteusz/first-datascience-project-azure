from azureml.core import Workspace
from azureml.core.authentication import InteractiveLoginAuthentication
import os


# subscription_id = os.getenv("SUBSCRIPTION_ID", default="692da6ab-d591-4771-9fe5-c63cfc577f90")
# resource_group = os.getenv("RESOURCE_GROUP", default="datascience-rg")
# workspace_name = os.getenv("WORKSPACE_NAME", default="azureml-kamil")
# # workspace_region = os.getenv("WORKSPACE_REGION", default="eastus2")

# interactive_auth = InteractiveLoginAuthentication(tenant_id="346c2fe3-f238-49ba-8c73-2e6e5260d586", force=True)

# ws = Workspace(subscription_id=subscription_id, 
#                resource_group=resource_group, 
#                workspace_name=workspace_name,
#                auth=interactive_auth)


ws = Workspace.from_config()
# # ws = Workspace(subscription_id=subscription_id, resource_group=resource_group, workspace_name=workspace_name)
print(ws)


