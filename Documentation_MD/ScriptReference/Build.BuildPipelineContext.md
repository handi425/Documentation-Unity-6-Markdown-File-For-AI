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

# BuildPipelineContext

class in UnityEditor.Build

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

Defines the build context for IProcessSceneWithReport during a build event.

This class contains static methods for declaring additional scene dependencies
for the build system. These dependencies are used to trigger scene rebuilds in
cases where dependencies are not explicit in the scene itself.  
  
For example, if the implementation of
[IProcessSceneWithReport](Build.IProcessSceneWithReport.html) loads an Asset
programmatically then
[BuildPipelineContext.DependOnAsset](Build.BuildPipelineContext.DependOnAsset.html)
should be called, unless the same Asset is also referenced by the Scene. Then,
if the Asset is changed and the build run again, Unity will retrigger the
callback and save the latest scene state instead of reusing an out-of-date
cached result.  
  
Dependency tracking is currently only required when
[EditorBuildSettings.UseParallelAssetBundleBuilding](EditorBuildSettings.UseParallelAssetBundleBuilding.html)
is true, for calls to
[BuildPipeline.BuildAssetBundles](BuildPipeline.BuildAssetBundles.html). It
does not currently apply to
[BuildPipeline.BuildPlayer](BuildPipeline.BuildPlayer.html).  
  
Additional resources:
[AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)

### Static Methods

[DependOnAsset](Build.BuildPipelineContext.DependOnAsset.html)| Allows you to
specify that a Scene depends on contents of an asset directly provided.  
---|---  
[DependOnPath](Build.BuildPipelineContext.DependOnPath.html)| Allows you to
specify that a Scene depends on contents of a source asset at the provided
path.  
  
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

