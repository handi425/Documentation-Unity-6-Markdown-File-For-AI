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
[AssetImportContext](AssetImporters.AssetImportContext.html).selectedBuildTarget

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

public [BuildTarget](BuildTarget.html) selectedBuildTarget;

### Description

Returns the current build target and creates a dependency on the target
platform within a scripted importer.

This property returns the current build target platform (similar to
EditorUserBuildSettings.activeBuildTarget), however this property is provided
specifically as a way for you to create a dependency on the build target
within a scripted importer.  
  
You should use this property if you are writing a scripted importer and you
want your importer to generate different results based on the target platform.
Using this property within a scripted importer creates a platform dependency
in your importer. This means when you change the Editor's active build target,
all assets imported by this importer will be automatically re-imported to
reflect any changes caused by the dependency you set up.  
  
_Note: If you are not writing an importer, and just want to read the currently
selected build target, you should use_
[EditorUserBuildSettings.activeBuildTarget](EditorUserBuildSettings-
activeBuildTarget.html).

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

