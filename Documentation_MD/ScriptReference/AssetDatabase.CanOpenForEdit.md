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

#  [AssetDatabase](AssetDatabase.html).CanOpenForEdit

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

public static bool CanOpenForEdit([Object](Object.html) assetObject,
[StatusQueryOptions](StatusQueryOptions.html) statusOptions =
StatusQueryOptions.UseCachedIfPossible);

## Declaration

public static bool CanOpenForEdit(string assetOrMetaFilePath,
[StatusQueryOptions](StatusQueryOptions.html) statusOptions =
StatusQueryOptions.UseCachedIfPossible);

## Declaration

public static bool CanOpenForEdit([Object](Object.html) assetObject, out
string message, [StatusQueryOptions](StatusQueryOptions.html) statusOptions =
StatusQueryOptions.UseCachedIfPossible);

## Declaration

public static bool CanOpenForEdit(string assetOrMetaFilePath, out string
message, [StatusQueryOptions](StatusQueryOptions.html) statusOptions =
StatusQueryOptions.UseCachedIfPossible);

### Parameters

assetObject | Object representing the asset whose status you wish to query.  
---|---  
assetOrMetaFilePath | Path to the asset file or its .meta file on disk, relative to project folder.  
message | Returns a reason for the asset not being available for edit.  
statusOptions | Options for how the version control system should be queried. These options can effect the speed and accuracy of the query. Default is [StatusQueryOptions.UseCachedIfPossible](StatusQueryOptions.UseCachedIfPossible.html).  
  
### Returns

**bool** True if the asset is considered available for edit by the selected
version control system.

### Description

Query whether an Asset file can be opened for editing in version control and
is not exclusively locked by another user or otherwise unavailable.

See [AssetDatabase.IsOpenForEdit](AssetDatabase.IsOpenForEdit.html) for
detailed explanation.  
  
Additional resources: [StatusQueryOptions](StatusQueryOptions.html),
[AssetDatabase.MakeEditable](AssetDatabase.MakeEditable.html).

* * *

## Declaration

public static void CanOpenForEdit(string[] assetOrMetaFilePaths, List<string>
outNotEditablePaths, [StatusQueryOptions](StatusQueryOptions.html)
statusQueryOptions = StatusQueryOptions.UseCachedIfPossible);

### Parameters

assetOrMetaFilePaths | Paths to Assets or their .meta files, relative to the project folder.  
---|---  
outNotEditablePaths | Destination list of non-editable Asset paths.  
statusQueryOptions | Specifies how Unity should query the version control system. The default value is [StatusQueryOptions.UseCachedIfPossible](StatusQueryOptions.UseCachedIfPossible.html).  
  
### Description

Query which of the provided Asset files can be opened for editing in version
control and are not remotely locked or otherwise unavailable.

This variant of the `CanOpenForEdit` function can query multiple Asset paths
at once. It writes paths for Assets that are not 'available for edit' into the
`outNotEditablePaths` list.

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

