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

#
[AssetImportContext](AssetImporters.AssetImportContext.html).AddObjectToAsset

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

## Declaration

public void AddObjectToAsset(string identifier, [Object](Object.html) obj);

## Declaration

public void AddObjectToAsset(string identifier, [Object](Object.html) obj,
[Texture2D](Texture2D.html) thumbnail);

### Parameters

identifier | A unique identifier associated to this object.  
---|---  
obj | The Unity Object to add to the asset.  
thumbnail | An optional 2D texture to use as the thumbnail for this object.  
  
### Description

Adds an object to the result of the import operation.

Use this method to add objects to the resulting asset. AddObjectToAsset can be
called multiple times if more than one unity object is the result of the
import process. Note: You must make sure that your importer provides a unique
identifier for each added object. You must also make sure that your code
regenerates the same identifier each time the file is re-imported: identifiers
should be deterministic. This allows Unity to keep match previously imported
objects with the newly created objects. The identifier only needs to be unique
within the context of the Asset file and not globally unique across your whole
project.

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

