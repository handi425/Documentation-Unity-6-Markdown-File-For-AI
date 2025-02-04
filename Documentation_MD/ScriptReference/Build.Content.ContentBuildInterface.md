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

# ContentBuildInterface

class in UnityEditor.Build.Content

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

Low level interface for building content for Unity.

Note: this class and its members exist to provide low-level support for the
**Scriptable Build Pipeline** package. This is intended for internal use only;
use the [Scriptable Build Pipeline
package](https://docs.unity3d.com/Packages/com.unity.scriptablebuildpipeline@latest/index.html)
to implement a fully featured build pipeline. You can install this via the
[Unity Package Manager](https://docs.unity3d.com/Packages/com.unity.package-
manager-ui@latest/index.html).

### Static Methods

[ArchiveAndCompress](Build.Content.ContentBuildInterface.ArchiveAndCompress.html)|
Create a Unity archive file, containing the content of one or more resource
files.  
---|---  
[CalculateBuildUsageTags](Build.Content.ContentBuildInterface.CalculateBuildUsageTags.html)|
Calculates the build usage of a set of objects.  
[CalculatePlayerDependenciesForGameManagers](Build.Content.ContentBuildInterface.CalculatePlayerDependenciesForGameManagers.html)|
Calculates dependency information for various internal Unity game manager
classes.  
[CalculatePlayerDependenciesForScene](Build.Content.ContentBuildInterface.CalculatePlayerDependenciesForScene.html)|
Calculates the Scene dependency information.  
[CalculatePlayerSerializationHashForType](Build.Content.ContentBuildInterface.CalculatePlayerSerializationHashForType.html)|
Returns a unique hash for a given type's serialized layout.  
[GenerateAssetBundleBuilds](Build.Content.ContentBuildInterface.GenerateAssetBundleBuilds.html)|
Returns an array of AssetBundleBuild structs that detail the current
AssetBundle layout, as set through the Inspector and stored in the
AssetDatabase.  
[GetGlobalUsageFromActiveScene](Build.Content.ContentBuildInterface.GetGlobalUsageFromActiveScene.html)|
Gets information about the lighting and render settings in the active scene.  
[GetGlobalUsageFromGraphicsSettings](Build.Content.ContentBuildInterface.GetGlobalUsageFromGraphicsSettings.html)|
Returns the global usage information calculated by the Shader Stripping
section of Graphics Settings.  
[GetPlayerAssetRepresentations](Build.Content.ContentBuildInterface.GetPlayerAssetRepresentations.html)|
Returns a list of visible objects directly contained inside of an asset.  
[GetPlayerDependenciesForObject](Build.Content.ContentBuildInterface.GetPlayerDependenciesForObject.html)|
Returns a list of objects referenced by an object.  
[GetPlayerDependenciesForObjects](Build.Content.ContentBuildInterface.GetPlayerDependenciesForObjects.html)|
Returns a list of objects referenced by a set of objects.  
[GetPlayerObjectIdentifiersInAsset](Build.Content.ContentBuildInterface.GetPlayerObjectIdentifiersInAsset.html)|
Returns a list of objects directly contained inside of an asset.  
[GetPlayerObjectIdentifiersInSerializedFile](Build.Content.ContentBuildInterface.GetPlayerObjectIdentifiersInSerializedFile.html)|
Returns a list of objects directly contained inside of a loose serialized
file.  
[GetTypeForObject](Build.Content.ContentBuildInterface.GetTypeForObject.html)|
Returns the System.Type of the ObjectIdentifier specified by objectID.  
[GetTypeForObjects](Build.Content.ContentBuildInterface.GetTypeForObjects.html)|
Returns the System.Type of the ObjectIdentifiers and the referenced
SerializeReference class types specified by objectIDs.  
[GetTypesForObject](Build.Content.ContentBuildInterface.GetTypesForObject.html)|
Returns the System.Type of the ObjectIdentifier and the referenced
SerializeReference class types specified by objectID.  
[ObjectIsSupportedInBuild](Build.Content.ContentBuildInterface.ObjectIsSupportedInBuild.html)|
Returns True if the passed in target object is a valid runtime object.  
[StartProfileCapture](Build.Content.ContentBuildInterface.StartProfileCapture.html)|
Starts a profile capture to record content build profile events.  
[StopProfileCapture](Build.Content.ContentBuildInterface.StopProfileCapture.html)|
Returns an array of ContentBuildProfileEvent structs that contain information
for each occuring event. Also stops the profile capture.  
[WriteGameManagersSerializedFile](Build.Content.ContentBuildInterface.WriteGameManagersSerializedFile.html)|
Writes the current settings of internal Unity game manager classes to the
'globalgamemanagers' file on disk.  
[WriteSceneSerializedFile](Build.Content.ContentBuildInterface.WriteSceneSerializedFile.html)|
Writes Scene objects to a serialized file on disk.  
[WriteSerializedFile](Build.Content.ContentBuildInterface.WriteSerializedFile.html)|
Writes objects to a serialized file on disk.  
  
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

