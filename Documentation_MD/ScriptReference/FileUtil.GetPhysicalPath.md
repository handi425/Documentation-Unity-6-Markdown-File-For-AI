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

#  [FileUtil](FileUtil.html).GetPhysicalPath

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

public static string GetPhysicalPath(string path);

### Parameters

path | Logical path.  
---|---  
  
### Returns

**string** Physical path.

### Description

Converts a logical path to a physical path.

Logical paths in Unity are virtual paths which point to real (or "physical")
file and directory paths on disk. They're designed to be shorter and simpler,
making them easier to work with than the real file paths. For example in Unity
you might see a logical path such as:  
  
**Packages/MyPackage/MyFile.txt**  
  
Which points to a physical file at:  
  
**C:/Users/SomeUser/MyProject/Library/PackageCache/MyPackage@fingerprint/MyFile.txt**  
  
When working inside Unity, these mappings occur automatically, so in most
situations you do not need to call these methods to convert from logical to
physical paths. However in certain situations if you are working with external
tools that are unaware of Unity's logical paths, you may need to use these
methods to provide the mapping between logical and physical paths.  
  
Additional resources: [FileUtil.GetLogicalPath]

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

