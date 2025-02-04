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

#  [AssetBundleBuild](AssetBundleBuild.html).assetBundleName

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

public string assetBundleName;

### Description

AssetBundle name.

When building an AssetBundle this property is converted to lowercase and used
as the filename of the AssetBundle. On platforms with case sensitive file
systems, such as Linux, the AssetBundle load would fail unless the lowercase
form of the AssetBundle name is specified. To avoid surprises we recommend
choosing a lowercase name for your AssetBundle.  
  
The name may start with folder names, for example "level1/materials/bundle_a",
in which case the build creates those as subfolders of the output path.  
  
The provided name can end with a file extension, but typically AssetBundles
are built with no extension because of the way AssetBundle variants work.  
  
In the case of AssetBundle variants, the name of the AssetBundle file is this
string, concatenated with the
[AssetBundleBuild.assetBundleVariant](AssetBundleBuild-
assetBundleVariant.html) property as its extension, and all converted to
lowercase.

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

