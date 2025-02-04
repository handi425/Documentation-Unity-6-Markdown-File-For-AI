[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# SpeedTreeImporter

class in UnityEditor

/

Inherits from:[AssetImporter](AssetImporter.html)

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[Switch to Manual](../Manual/class-SpeedTreeImporter.html "Go to
SpeedTreeImporter Component in the Manual")

### Description

AssetImporter for importing SpeedTree model assets.

### Static Properties

[windQualityNames](SpeedTreeImporter-windQualityNames.html)| Gets an array of
name strings for wind quality value.  
---|---  
  
### Properties

[alphaTestRef](SpeedTreeImporter-alphaTestRef.html)| Gets and sets a default
alpha test reference values.  
---|---  
[animateCrossFading](SpeedTreeImporter-animateCrossFading.html)| Indicates if
the cross-fade LOD transition, applied to the last mesh LOD and the billboard,
should be animated.  
[bestWindQuality](SpeedTreeImporter-bestWindQuality.html)| Returns the best-
possible wind quality on this asset (configured in SpeedTree modeler).  
[billboardTransitionCrossFadeWidth](SpeedTreeImporter-
billboardTransitionCrossFadeWidth.html)| Proportion of the last 3D mesh LOD
region width which is used for cross-fading to billboard tree.  
[castShadows](SpeedTreeImporter-castShadows.html)| Gets and sets an array of
booleans to enable shadow casting for each LOD.  
[castShadowsByDefault](SpeedTreeImporter-castShadowsByDefault.html)| Gets and
sets a boolean to toggle whether the imported SpeedTree casts shadows.  
[defaultBillboardShader](SpeedTreeImporter-defaultBillboardShader.html)|
Returns the default SpeedTree billboard shader for the active render pipeline,
or null if the asset is a SpeedTree v8 asset.  
[defaultShader](SpeedTreeImporter-defaultShader.html)| Returns the default
SpeedTree shader for the active render pipeline (either v7 or v8 according to
the asset version).  
[enableBump](SpeedTreeImporter-enableBump.html)| Gets and sets an array of
booleans to enable normal mapping for each LOD.  
[enableBumpByDefault](SpeedTreeImporter-enableBumpByDefault.html)| Gets and
sets a boolean to enable normal mapping on the imported SpeedTree model.  
[enableHue](SpeedTreeImporter-enableHue.html)| Gets and sets an array of
booleans to enable hue variation effect for each LOD.  
[enableHueByDefault](SpeedTreeImporter-enableHueByDefault.html)| Gets and sets
a boolean to enable hue variation effect on the imported SpeedTree model.  
[enableSettingOverride](SpeedTreeImporter-enableSettingOverride.html)| Gets
and sets an array of booleans to customize importer settings for a specific
LOD.  
[enableSmoothLODTransition](SpeedTreeImporter-enableSmoothLODTransition.html)|
Enables smooth LOD transitions.  
[enableSubsurface](SpeedTreeImporter-enableSubsurface.html)| Gets and sets an
array of booleans to enable the subsurface scattering effect for each LOD
(affects only SpeedTree v8 assets).  
[enableSubsurfaceByDefault](SpeedTreeImporter-enableSubsurfaceByDefault.html)|
Gets and sets a boolean to enable the subsurface scattering effect for the
SpeedTree asset (affects only SpeedTree v8 assets).  
[fadeOutWidth](SpeedTreeImporter-fadeOutWidth.html)| Proportion of the
billboard LOD region width which is used for fading out the billboard.  
[generateColliders](SpeedTreeImporter-generateColliders.html)| Gets and sets
the boolean to toggle collider object generation during import.  
[generateRigidbody](SpeedTreeImporter-generateRigidbody.html)| Gets and sets
the boolean to toggle Rigidbody generation during import.  
[hasBillboard](SpeedTreeImporter-hasBillboard.html)| Tells if there is a
billboard LOD.  
[hasImported](SpeedTreeImporter-hasImported.html)| Tells if the SPM file has
been previously imported.  
[hueVariation](SpeedTreeImporter-hueVariation.html)| Gets and sets a default
hue variation color and amount (in alpha).  
[isV8](SpeedTreeImporter-isV8.html)| Returns true if the asset is a SpeedTree
v8 asset.  
[LODHeights](SpeedTreeImporter.LODHeights.html)| Gets and sets an array of
floats of each LOD's screen height value.  
[mainColor](SpeedTreeImporter-mainColor.html)| Gets and sets a default main
color.  
[materialFolderPath](SpeedTreeImporter-materialFolderPath.html)| Returns the
folder path where generated materials will be placed in.  
[materialLocation](SpeedTreeImporter-materialLocation.html)| Material import
location options.  
[receiveShadows](SpeedTreeImporter-receiveShadows.html)| Gets and sets an
array of booleans to enable shadow receiving for each LOD.  
[receiveShadowsByDefault](SpeedTreeImporter-receiveShadowsByDefault.html)|
Gets and sets a boolean to enable whether the SpeedTree asset receives shadows
from other objects in your scene.  
[scaleFactor](SpeedTreeImporter-scaleFactor.html)| How much to scale the tree
model compared to what is in the imported SpeedTree model file.  
[selectedWindQuality](SpeedTreeImporter-selectedWindQuality.html)| Gets and
sets an integer corresponding to the SpeedTreeWind enum values. The value is
clamped by SpeedTreeImporter.bestWindQuality internally.  
[useLightProbes](SpeedTreeImporter-useLightProbes.html)| Gets and sets an
array of booleans to enable Light Probe lighting for each LOD.  
[useLightProbesByDefault](SpeedTreeImporter-useLightProbesByDefault.html)|
Gets and sets a boolean to enable light probe lighting for the imported
SpeedTree model.  
[windQualities](SpeedTreeImporter-windQualities.html)| Gets and sets an array
of integers of the wind qualities on each LOD. Values will be clamped by
SpeedTreeImporter.bestWindQuality internally.  
  
### Constructors

[SpeedTreeImporter](SpeedTreeImporter-ctor.html)| Construct a new
SpeedTreeImporter object.  
---|---  
  
### Public Methods

[GenerateMaterials](SpeedTreeImporter.GenerateMaterials.html)| Generates all
necessary materials under materialFolderPath. If Version Control is enabled
please first check out the folder.  
---|---  
[SearchAndRemapMaterials](SpeedTreeImporter.SearchAndRemapMaterials.html)|
Search the project for matching materials and use them instead of the internal
materials.  
  
### Inherited Members

### Properties

[assetBundleName](AssetImporter-assetBundleName.html)| Get or set the
AssetBundle name.  
---|---  
[assetBundleVariant](AssetImporter-assetBundleVariant.html)| Get or set the
AssetBundle variant.  
[assetPath](AssetImporter-assetPath.html)| The path name of the asset for this
importer. (Read Only)  
[importSettingsMissing](AssetImporter-importSettingsMissing.html)| The value
is true when no meta file is provided with the imported asset.  
[userData](AssetImporter-userData.html)| Get or set any user data.  
[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[AddRemap](AssetImporter.AddRemap.html)| Map a sub-asset from an imported
asset (such as an FBX file) to an external Asset of the same type.  
---|---  
[GetExternalObjectMap](AssetImporter.GetExternalObjectMap.html)| Gets a copy
of the external object map used by the AssetImporter.  
[RemoveRemap](AssetImporter.RemoveRemap.html)| Removes an item from the map of
external objects.  
[SaveAndReimport](AssetImporter.SaveAndReimport.html)| Save asset importer
settings if asset importer is dirty.  
[SetAssetBundleNameAndVariant](AssetImporter.SetAssetBundleNameAndVariant.html)|
Set the AssetBundle name and variant.  
[SupportsRemappedAssetType](AssetImporter.SupportsRemappedAssetType.html)|
Checks if the AssetImporter supports remapping the given asset type.  
[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[GetAtPath](AssetImporter.GetAtPath.html)| Retrieves the asset importer for
the asset at path.  
---|---  
[GetImportLog](AssetImporter.GetImportLog.html)| Retrieves logs generated
during the import of the asset at path.  
[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

