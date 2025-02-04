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

# ThreeDSMaterialDescriptionPreprocessor

class in UnityEditor.AssetImporters

/

Inherits from:[AssetPostprocessor](AssetPostprocessor.html)

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

[ ]()

### Description

This is a default implementation for
AssetPostProcessor.OnPreprocessMaterialDescription, this implementation
converts material descriptions imported from .3DS assets into materials for
the internal rendering pipeline.

### Inherited Members

### Properties

[assetImporter](AssetPostprocessor-assetImporter.html)| Reference to the asset
importer.  
---|---  
[assetPath](AssetPostprocessor-assetPath.html)| The path name of the asset
being imported.  
[context](AssetPostprocessor-context.html)| The import context.  
  
### Public Methods

[GetPostprocessOrder](AssetPostprocessor.GetPostprocessOrder.html)| Override
the order in which importers are processed.  
---|---  
[GetVersion](AssetPostprocessor.GetVersion.html)| Returns the version of the
asset postprocessor.  
  
### Messages

[OnAssignMaterialModel](AssetPostprocessor.OnAssignMaterialModel.html)| Feeds
a source material.  
---|---  
[OnPostprocessAllAssets](AssetPostprocessor.OnPostprocessAllAssets.html)| This
is called after importing of any number of assets is complete (when the Assets
progress bar has reached the end).  
[OnPostprocessAnimation](AssetPostprocessor.OnPostprocessAnimation.html)| This
function is called when an AnimationClip has finished importing.  
[OnPostprocessAssetbundleNameChanged](AssetPostprocessor.OnPostprocessAssetbundleNameChanged.html)|
Handler called when asset is assigned to a different asset bundle.  
[OnPostprocessAudio](AssetPostprocessor.OnPostprocessAudio.html)| Add this
function to a subclass to get a notification when an audio clip has completed
importing.  
[OnPostprocessCubemap](AssetPostprocessor.OnPostprocessCubemap.html)| Add this
function to a subclass to get a notification just before a cubemap texture has
completed importing.  
[OnPostprocessGameObjectWithAnimatedUserProperties](AssetPostprocessor.OnPostprocessGameObjectWithAnimatedUserProperties.html)|
This function is called when the animation curves for a custom property are
finished importing.  
[OnPostprocessGameObjectWithUserProperties](AssetPostprocessor.OnPostprocessGameObjectWithUserProperties.html)|
Gets called for each GameObject that had at least one user property attached
to it in the imported file.  
[OnPostprocessMaterial](AssetPostprocessor.OnPostprocessMaterial.html)| Add
this function to a subclass to get a notification when a new Material is
created during an import of a ModelImporter.  
[OnPostprocessMeshHierarchy](AssetPostprocessor.OnPostprocessMeshHierarchy.html)|
This function is called when a new transform hierarchy has finished importing.  
[OnPostprocessModel](AssetPostprocessor.OnPostprocessModel.html)| Add this
function to a subclass to get a notification when a model has completed
importing.  
[OnPostprocessPrefab](AssetPostprocessor.OnPostprocessPrefab.html)| Gets a
notification when a Prefab completes importing.  
[OnPostprocessSpeedTree](AssetPostprocessor.OnPostprocessSpeedTree.html)| Add
this function to a subclass to get a notification when a SpeedTree asset has
completed importing.  
[OnPostprocessSprites](AssetPostprocessor.OnPostprocessSprites.html)| Add this
function to a subclass to get a notification when an texture of sprite(s) has
completed importing.  
[OnPostprocessTexture](AssetPostprocessor.OnPostprocessTexture.html)| Add this
function to a subclass to get a notification when a texture2D has completed
importing just before Unity compresses it.  
[OnPostprocessTexture2DArray](AssetPostprocessor.OnPostprocessTexture2DArray.html)|
Add this function to a subclass to get a notification when a texture2DArray
has completed importing just before Unity compresses it.  
[OnPostprocessTexture3D](AssetPostprocessor.OnPostprocessTexture3D.html)| Add
this function to a subclass to get a notification when a texture3D has
completed importing just before Unity compresses it.  
[OnPreprocessAnimation](AssetPostprocessor.OnPreprocessAnimation.html)| Add
this function to a subclass to get a notification just before animation from a
model (.fbx, .mb file etc.) is imported.  
[OnPreprocessAsset](AssetPostprocessor.OnPreprocessAsset.html)| Add this
function to a subclass to get a notification just before any Asset is
imported.  
[OnPreprocessAudio](AssetPostprocessor.OnPreprocessAudio.html)| Add this
function to a subclass to get a notification just before an audio clip is
being imported.  
[OnPreprocessCameraDescription](AssetPostprocessor.OnPreprocessCameraDescription.html)|
Add this function to a subclass to receive a notification when a camera is
imported from a Model Importer.  
[OnPreprocessLightDescription](AssetPostprocessor.OnPreprocessLightDescription.html)|
Add this function to a subclass to recieve a notification when a light is
imported from a Model Importer.  
[OnPreprocessMaterialDescription](AssetPostprocessor.OnPreprocessMaterialDescription.html)|
Add this function to a subclass to recieve a notification when a new material
is created during the import of a ModelImporter.  
[OnPreprocessModel](AssetPostprocessor.OnPreprocessModel.html)| Add this
function to a subclass to get a notification just before a model (.fbx, .mb
file etc.) is imported.  
[OnPreprocessSpeedTree](AssetPostprocessor.OnPreprocessSpeedTree.html)| Add
this function to a subclass to get a notification just before a SpeedTree
asset (.spm file) is imported.  
[OnPreprocessTexture](AssetPostprocessor.OnPreprocessTexture.html)| Add this
function to a subclass to get a notification just before the texture importer
is run.  
  
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

