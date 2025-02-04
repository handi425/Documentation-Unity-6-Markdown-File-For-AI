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
[BuildAssetBundlesParameters](BuildAssetBundlesParameters.html).bundleDefinitions

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

public AssetBundleBuild[] bundleDefinitions;

### Description

Array defining the name and contents of each AssetBundle. (optional)

An array of [AssetBundleBuild](AssetBundleBuild.html) structs that define the
names and contents of each AssetBundle, e.g. the "Build Map". When provided
Unity builds only the AssetBundles as specified, and ignores any AssetBundle
assignments that had been made in the Editor user interface. This approach
makes it convenient to programmatically define AssetBundle contents or to
perform builds with different content within the same project.  
  
This field can be left unassigned, e.g. null, in which case
[BuildPipeline.BuildAssetBundles](BuildPipeline.BuildAssetBundles.html) uses
the AssetBundle assignments made in the Editor to determine the AssetBundles
and their contents. Those assignments are stored in the AssetDatabase and in
the .meta files and can also be accessed programmatically, see
[AssetImporter.assetBundleName](AssetImporter-assetBundleName.html),
[AssetDatabase.GetAssetPathsFromAssetBundle](AssetDatabase.GetAssetPathsFromAssetBundle.html)
and
[AssetDatabase.GetImplicitAssetBundleName](AssetDatabase.GetImplicitAssetBundleName.html).

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

