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

# EditorSettings

class in UnityEditor

/

Inherits from:[Object](Object.html)

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

User settings for Unity Editor.

Use EditorSettings to apply Editor Project Settings to your Unity Project. You
can control settings such as version control, streaming settings, and Asset
serialization.  
  
Additional resources: [Editor Project Settings](../Manual/class-
EditorManager.html)

### Static Properties

[assetNamingUsesSpace](EditorSettings-assetNamingUsesSpace.html)| Controls
whether to insert a space before a number in duplicated Asset names.  
---|---  
[assetPipelineMode](EditorSettings-assetPipelineMode.html)| Select the
assetpipeline mode.  
[asyncShaderCompilation](EditorSettings-asyncShaderCompilation.html)| Enable
asynchronous Shader compilation in Game and Scene view.  
[cacheServerDownloadBatchSize](EditorSettings-
cacheServerDownloadBatchSize.html)| Controls the size of the batches used when
making cacheserver download requests.  
[cacheServerEnableAuth](EditorSettings-cacheServerEnableAuth.html)| Toggle
whether to enable authentication to cache server.  
[cacheServerEnableDownload](EditorSettings-cacheServerEnableDownload.html)|
Toggle whether to enable downloading from cache server.  
[cacheServerEnableTls](EditorSettings-cacheServerEnableTls.html)| Toggle
whether to enable TLS encryption to cache server.  
[cacheServerEnableUpload](EditorSettings-cacheServerEnableUpload.html)| Toggle
whether to enable uploading from cache server.  
[cacheServerEndpoint](EditorSettings-cacheServerEndpoint.html)| Cache server
endpoint IP address  
[cacheServerMode](EditorSettings-cacheServerMode.html)| Select cache server
mode  
[cacheServerNamespacePrefix](EditorSettings-cacheServerNamespacePrefix.html)|
Sets the namespace prefix to use for the cache server.  
[cacheServerValidationMode](EditorSettings-cacheServerValidationMode.html)|
Select Accelerator server validation mode.  
[cachingShaderPreprocessor](EditorSettings-cachingShaderPreprocessor.html)|
This property is now obsolete. Unity always uses the Caching Shader
Preprocessor.  
[enableTextureStreamingInEditMode](EditorSettings-
enableTextureStreamingInEditMode.html)| Enable texture mipmap streaming system
when in Edit Mode.  
[enableTextureStreamingInPlayMode](EditorSettings-
enableTextureStreamingInPlayMode.html)| Enable texture mipmap streaming system
when in Play Mode.  
[enterPlayModeOptions](EditorSettings-enterPlayModeOptions.html)| Determines
the state of the Enter Play Mode Options in the Unity Editor.  
[enterPlayModeOptionsEnabled](EditorSettings-
enterPlayModeOptionsEnabled.html)| Determines whether the Enter Play Mode
Options are enabled in the Unity Editor or not.  
[gameObjectNamingDigits](EditorSettings-gameObjectNamingDigits.html)|
Indicates the amount of digits to use for the numbers in a duplicated
GameoObject's name.  
[gameObjectNamingScheme](EditorSettings-gameObjectNamingScheme.html)|
Indicates which naming scheme to use for duplicated GameObjects.  
[lineEndingsForNewScripts](EditorSettings-lineEndingsForNewScripts.html)|
Determines what line endings to use in a new C# file created in the Editor.  
[prefabModeAllowAutoSave](EditorSettings-prefabModeAllowAutoSave.html)| Allow
Auto Save in Prefab Mode for this project.  
[prefabRegularEnvironment](EditorSettings-prefabRegularEnvironment.html)|
Allows you to specify a Scene to use as the editing environment for Prefabs.  
[prefabUIEnvironment](EditorSettings-prefabUIEnvironment.html)| Allows you to
specify a Scene to use as the editing environment for UI Prefabs.  
[projectGenerationRootNamespace](EditorSettings-
projectGenerationRootNamespace.html)| Controls which root namespace gets
written into the c# .csproj projects that Unity generates.  
[projectGenerationUserExtensions](EditorSettings-
projectGenerationUserExtensions.html)| Controls list of extensions of files
that will be included in the c# .csproj projects that Unity generates.  
[referencedClipsExactNaming](EditorSettings-referencedClipsExactNaming.html)|
Controls which referenced clips an humanoid rig is able to update when using
@convention files.  
[refreshImportMode](EditorSettings-refreshImportMode.html)| Controls the
Editor's use of parallel processes when it imports assets during an asset
database refresh, for this project.  
[serializeInlineMappingsOnOneLine](EditorSettings-
serializeInlineMappingsOnOneLine.html)| Forces Unity to write references and
similar YAML structures on one line, which reduces version control noise.  
[spritePackerPaddingPower](EditorSettings-spritePackerPaddingPower.html)|
Power of 2 value to add a boundary (padding) to Sprites packed to the Atlas
(Legacy Sprite Packer).  
[unityRemoteCompression](EditorSettings-unityRemoteCompression.html)| Gets or
sets compression method used for Unity Remote screen stream.  
[unityRemoteDevice](EditorSettings-unityRemoteDevice.html)| Gets or sets
device ID used for Unity Remote feature.  
[unityRemoteJoystickSource](EditorSettings-unityRemoteJoystickSource.html)|
Gets or sets joystick source used in editor when Unity Remote is connected.  
[unityRemoteResolution](EditorSettings-unityRemoteResolution.html)| Gets or
sets resolution used for Unity Remote screen stream.  
[useLegacyProbeSampleCount](EditorSettings-useLegacyProbeSampleCount.html)|
Enable the legacy fixed sample counts for baking Light Probes with Progressive
Lightmapper.  
  
### Inherited Members

### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
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

