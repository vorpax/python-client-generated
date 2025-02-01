# InstallationClassee

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raison_sociale** | **str** | Raison sociale de l&#x27;installation classee si personne morale ou nom et prenom si personne physique | [optional] 
**adresse1** | **str** | Adresse - Ligne 1 | [optional] 
**adresse2** | **str** | Adresse - Ligne 2 | [optional] 
**adresse3** | **str** | Adresse - Ligne 3 | [optional] 
**code_postal** | **str** | Code postal de l&#x27;installation classee | [optional] 
**code_insee** | **str** | Code INSEE de l&#x27;installation classee | [optional] 
**commune** | **str** | Commune de l&#x27;installation classee | [optional] 
**code_naf** | **str** | Deux premiers caracteres du code NAF de l&#x27;installation classee | [optional] 
**longitude** | **float** | Valeur de la coordonnee longitude | [optional] 
**latitude** | **float** | Valeur de la coordonnee latitude | [optional] 
**bovins** | **bool** | Famille ou sous famille de la nomenclature installation classee | [optional] 
**porcs** | **bool** | Famille ou sous famille de la nomenclature installation classee | [optional] 
**volailles** | **bool** | Famille ou sous famille de la nomenclature installation classee | [optional] 
**carriere** | **bool** | Famille ou sous famille de la nomenclature installation classee | [optional] 
**eolienne** | **bool** | Famille ou sous famille de la nomenclature installation classee | [optional] 
**industrie** | **bool** | Famille ou sous famille de la nomenclature installation classee | [optional] 
**priorite_nationale** | **bool** | Indicateur de priorite nationale | [optional] 
**statut_seveso** | **str** | Presence du champ statut SEVESO | [optional] 
**ied** | **bool** | Indicateur IED | [optional] 
**etat_activite** | **str** | Etat de l&#x27;activite de l&#x27;installation classee | [optional] 
**code_aiot** | **str** | Code unique GUNenv, clef metier | [optional] 
**siret** | **str** | Systeme d&#x27;identification du repertoire des installations classees sur 14 chiffres | [optional] 
**coordonnee_xaiot** | **int** | Valeur de la coordonnee X | [optional] 
**coordonnee_yaiot** | **int** | Valeur de la coordonnee Y | [optional] 
**systeme_coordonnees_aiot** | **str** | Systeme de coordonnees geographiques (projection) de l&#x27;installation classee | [optional] 
**service_aiot** | **str** | Libelle court du service d&#x27;inspection | [optional] 
**regime** | **str** | Regime en vigeur de l&#x27;installation classee | [optional] 
**rubriques** | [**list[RubriqueIC]**](RubriqueIC.md) | Liste des rubriques repondant aux criteres | [optional] 
**inspections** | [**list[Inspection]**](Inspection.md) | Liste des inspections | [optional] 
**documents_hors_inspection** | [**list[MetadataFichier]**](MetadataFichier.md) | Liste des documents hors inpection publies sur Georisques | [optional] 
**date_maj** | **datetime** | Date de dernière mise à jour des données. L&#x27;API renvoie toutes les données ayant été mises à jour à partir de date_maj | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

