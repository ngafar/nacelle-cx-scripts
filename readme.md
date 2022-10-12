# nacelle-orphan-tool

A tool for sifting out instances where the Nacelle dashboard has the correct data, but the API returns incorrect data. More specifically, querying by `handles` should return an incorrect/older data. However, querying by `nacelleEntryIds` should return the expected response. This discrepancy — where querying by `nacelleEntryIds` returns the right data, but `handles` does not — is a tell tale sign of an "orphaned" entry. 

Orphaned entries are usually the result of a handle change. 