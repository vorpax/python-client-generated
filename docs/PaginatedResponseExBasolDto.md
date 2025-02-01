# PaginatedResponseExBasolDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **int** | Le nombre total de résultats | [optional] 
**page** | **int** | Le numéro de page actuelle | [optional] 
**total_pages** | **int** | Le nombre total de pages | [optional] 
**data** | [**list[ExBasolDto]**](ExBasolDto.md) | Le tableau contenant la réponse du endpoint | [optional] 
**response_code** | **int** | Le code HTTP de la réponse | [optional] 
**message** | **str** | Le message d&#x27;erreur si applicable | [optional] 
**next** | **str** | Le lien vers la page de résultat suivante | [optional] 
**previous** | **str** | Le lien vers la page de résultat précédente | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

