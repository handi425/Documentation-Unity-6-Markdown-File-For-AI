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

#  [AssetDatabase](AssetDatabase.html).TryGetAssetFolderInfo

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

public static bool TryGetAssetFolderInfo(string path, out bool rootFolder, out
bool immutable);

### Parameters

path | A project relative or absolute path to a file or a folder.  
---|---  
rootFolder | This value will be set to true if the given path is a root folder in the AssetDatabase.  
immutable | This value will be true if the given file or folder can't be modified by the AssetDatabase .  
  
### Returns

**bool** Returns true if the given path is in a folder managed by the
AssetDatabase, false otherwise.

### Description

Get AssetDatabase specific information about a folder.

This method can be used to know whether a path is tracked by the
AssetDatabase. Being tracked means that files added to this folder will have a
.meta file added along them and be imported and available in the current Unity
project. The out arguments can be used to get more information about the given
path. \- rootFolder is true if the given path is the root of a tracked path on
your drive. For example the Assets folder is a root. \- immutable is true if
the given path is under a root folder registered with the immutable flag. For
example files in a package added from the package manager registry will be
immutable.

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

