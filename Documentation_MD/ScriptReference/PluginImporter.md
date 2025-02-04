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

# PluginImporter

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

[ ]()

### Description

Represents a plugin importer.

### Properties

[DefineConstraints](PluginImporter.DefineConstraints.html)| Allows you to
specify a list of #define directives which controls whether your plug-in
should be included.  
---|---  
[isNativePlugin](PluginImporter-isNativePlugin.html)| Is plugin native or
managed? Note: C++ libraries with CLR support are treated as native plugins,
because Unity cannot load such libraries. You can still access them via
P/Invoke.  
[isPreloaded](PluginImporter-isPreloaded.html)| Is a native plugin loaded
during startup or on demand?  
  
### Constructors

[PluginImporter](PluginImporter-ctor.html)| Constructor.  
---|---  
  
### Public Methods

[ClearSettings](PluginImporter.ClearSettings.html)| Clear all plugin settings
and set the compatability with Any Platform to true.  
---|---  
[GetCompatibleWithAnyPlatform](PluginImporter.GetCompatibleWithAnyPlatform.html)|
Checks whether a plugin is flagged as being compatible with Any Platform.  
[GetCompatibleWithEditor](PluginImporter.GetCompatibleWithEditor.html)| Is
plugin compatible with editor.  
[GetCompatibleWithPlatform](PluginImporter.GetCompatibleWithPlatform.html)| Is
plugin compatible with specified platform.  
[GetEditorData](PluginImporter.GetEditorData.html)| Returns editor specific
data for specified key.  
[GetExcludeEditorFromAnyPlatform](PluginImporter.GetExcludeEditorFromAnyPlatform.html)|
Is Editor excluded when Any Platform is set to true.  
[GetExcludeFromAnyPlatform](PluginImporter.GetExcludeFromAnyPlatform.html)| Is
platform excluded when Any Platform set to true.  
[GetIcon](PluginImporter.GetIcon.html)| Gets the custom icon to associate with
a MonoScript at import time.  
[GetIsOverridable](PluginImporter.GetIsOverridable.html)| Identifies whether
or not this plugin will be overridden if a plugin of the same name is placed
in your project folder.  
[GetPlatformData](PluginImporter.GetPlatformData.html)| Get platform specific
data.  
[SetCompatibleWithAnyPlatform](PluginImporter.SetCompatibleWithAnyPlatform.html)|
Sets compatibility with Any Platform.  
[SetCompatibleWithEditor](PluginImporter.SetCompatibleWithEditor.html)| Sets
compatibility with any editor.  
[SetCompatibleWithPlatform](PluginImporter.SetCompatibleWithPlatform.html)|
Sets compatibility with the specified platform.  
[SetEditorData](PluginImporter.SetEditorData.html)| Sets editor specific data.  
[SetExcludeEditorFromAnyPlatform](PluginImporter.SetExcludeEditorFromAnyPlatform.html)|
Exclude Editor from compatible platforms when Any Platform is set to true.  
[SetExcludeFromAnyPlatform](PluginImporter.SetExcludeFromAnyPlatform.html)|
Exclude platform from compatible platforms when Any Platform is set to true.  
[SetIcon](PluginImporter.SetIcon.html)| Sets the custom icon to associate with
a MonoScript imported by a managed plugin.  
[SetIncludeInBuildDelegate](PluginImporter.SetIncludeInBuildDelegate.html)|
Setting the delegate function to be called by ShouldIncludeInBuild.  
[SetPlatformData](PluginImporter.SetPlatformData.html)| Sets platform specific
data.  
[ShouldIncludeInBuild](PluginImporter.ShouldIncludeInBuild.html)| Identifies
whether or not this plugin should be included in the current build target.  
  
### Static Methods

[GetAllImporters](PluginImporter.GetAllImporters.html)| Returns all plugin
importers for all platforms.  
---|---  
[GetImporters](PluginImporter.GetImporters.html)| Returns all plugin importers
for specfied platform.  
  
### Delegates

[IncludeInBuildDelegate](PluginImporter.IncludeInBuildDelegate.html)| Delegate
to be used with SetIncludeInBuildDelegate.  
---|---  
  
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

