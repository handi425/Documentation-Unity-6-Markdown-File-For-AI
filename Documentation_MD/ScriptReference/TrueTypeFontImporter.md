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

# TrueTypeFontImporter

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

AssetImporter for importing Fonts.

### Properties

[ascentCalculationMode](TrueTypeFontImporter-ascentCalculationMode.html)|
Calculation mode for determining font's ascent.  
---|---  
[characterPadding](TrueTypeFontImporter-characterPadding.html)| Border pixels
added to character images for padding. This is useful if you want to render
text using a shader which needs to render outside of the character area (like
an outline shader).  
[characterSpacing](TrueTypeFontImporter-characterSpacing.html)| Spacing
between character images in the generated texture in pixels. This is useful if
you want to render text using a shader which samples pixels outside of the
character area (like an outline shader).  
[customCharacters](TrueTypeFontImporter-customCharacters.html)| A custom set
of characters to be included in the Font Texture.  
[fontNames](TrueTypeFontImporter-fontNames.html)| An array of font names, to
be used when includeFontData is set to false.  
[fontReferences](TrueTypeFontImporter-fontReferences.html)| References to
other fonts to be used looking for fallbacks.  
[fontRenderingMode](TrueTypeFontImporter-fontRenderingMode.html)| Font
rendering mode to use for this font.  
[fontSize](TrueTypeFontImporter-fontSize.html)| Font size to use for importing
the characters.  
[fontTextureCase](TrueTypeFontImporter-fontTextureCase.html)| Use this to
adjust which characters should be imported.  
[fontTTFName](TrueTypeFontImporter-fontTTFName.html)| The internal font name
of the TTF file.  
[includeFontData](TrueTypeFontImporter-includeFontData.html)| If this is
enabled, the actual font will be embedded into the asset for Dynamic fonts.  
[shouldRoundAdvanceValue](TrueTypeFontImporter-shouldRoundAdvanceValue.html)|
Set this property to true if you want to round the internal advance width of
the font to the nearest integer.  
  
### Public Methods

[GenerateEditableFont](TrueTypeFontImporter.GenerateEditableFont.html)| Create
an editable copy of the font asset at path.  
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

