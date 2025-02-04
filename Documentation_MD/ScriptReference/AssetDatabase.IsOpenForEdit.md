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

#  [AssetDatabase](AssetDatabase.html).IsOpenForEdit

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

public static bool IsOpenForEdit([Object](Object.html) assetObject,
[StatusQueryOptions](StatusQueryOptions.html) statusOptions =
StatusQueryOptions.UseCachedIfPossible);

## Declaration

public static bool IsOpenForEdit(string assetOrMetaFilePath,
[StatusQueryOptions](StatusQueryOptions.html) statusOptions =
StatusQueryOptions.UseCachedIfPossible);

## Declaration

public static bool IsOpenForEdit([Object](Object.html) assetObject, out string
message, [StatusQueryOptions](StatusQueryOptions.html) statusOptions =
StatusQueryOptions.UseCachedIfPossible);

## Declaration

public static bool IsOpenForEdit(string assetOrMetaFilePath, out string
message, [StatusQueryOptions](StatusQueryOptions.html) statusOptions =
StatusQueryOptions.UseCachedIfPossible);

### Parameters

assetObject | Object representing the asset whose status you wish to query.  
---|---  
assetOrMetaFilePath | Path to the asset file or its .meta file on disk, relative to project folder.  
message | Returns a reason for the asset not being open for edit.  
statusOptions | Options for how the version control system should be queried. These options can effect the speed and accuracy of the query. Default is [StatusQueryOptions.UseCachedIfPossible](StatusQueryOptions.UseCachedIfPossible.html).  
  
### Returns

**bool** True if the asset is considered open for edit by the selected version
control system.

### Description

Query whether an Asset file is open for editing in version control.

Your version control system may be configured to only allow a single user at a
time to edit certain types of files, to avoid conflicts that arise when
multiple users edit a file at the same time. In this case a user must 'open'
that file for editing (also known as 'checking out') to ensure that they have
permission to edit the file. Use this function to query the 'open for edit'
status of a file in a version control system that supports it.  
  
File paths that are outside of Unity project folder, or not under version
controlled folders (for example, "Library" or "Temp"), are always considered
open for editing. `IsOpenForEdit` returns `true` for these paths.  
  
File paths that refer to non-local Package folders are always considered to be
non-editable. `IsOpenForEdit` returns `false` for these paths.  
  
When no version control system is active, then file paths inside the project
are all considered open for editing.  
  
When a version control system is active, then for example under Perforce VCS,
"added" and "checked out locally" files are considered open for editing, and
other files are not.  
  
Additional resources:
[AssetDatabase.IsMetaFileOpenForEdit](AssetDatabase.IsMetaFileOpenForEdit.html),
[StatusQueryOptions](StatusQueryOptions.html),
[AssetDatabase.MakeEditable](AssetDatabase.MakeEditable.html).

* * *

## Declaration

public static void IsOpenForEdit(string[] assetOrMetaFilePaths, List<string>
outNotEditablePaths, [StatusQueryOptions](StatusQueryOptions.html)
statusQueryOptions = StatusQueryOptions.UseCachedIfPossible);

### Parameters

assetOrMetaFilePaths | Paths to Assets or their .meta files, relative to the project folder.  
---|---  
outNotEditablePaths | Destination list of non-editable Asset paths.  
statusQueryOptions | Specifies how Unity should query the version control system. The default value is [StatusQueryOptions.UseCachedIfPossible](StatusQueryOptions.UseCachedIfPossible.html).  
  
### Description

Query which of the provided Asset files are open for editing in version
control.

This variant of the `IsOpenForEdit` function can query multiple Asset paths at
once. It writes paths for Assets that are not 'open for edit' into the
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

