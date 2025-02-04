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

#  [QualitySettings](QualitySettings.html).GetRenderPipelineAssetsForPlatform

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

[Switch to Manual](../Manual/class-QualitySettings.html "Go to QualitySettings
Component in the Manual")

## Declaration

public static void GetRenderPipelineAssetsForPlatform(string
buildTargetGroupName, out HashSet<T> uniqueRenderPipelineAssets);

### Parameters

buildTargetGroupName | The platform to obtain the Render Pipeline Assets.  
---|---  
uniqueRenderPipelineAssets | A collection with the non null selected Render Pipeline Assets for the platform.  
  
### Description

[Editor Only] Obtains a set with the non null Render Pipeline Assets selected
on all the Quality Levels for the given platform.

* * *

## Declaration

public static void GetRenderPipelineAssetsForPlatform(string
buildTargetGroupName, out HashSet<T> uniqueRenderPipelineAssets, out bool
allLevelsAreOverridden);

### Parameters

buildTargetGroupName | The platform to obtain the Render Pipeline Assets.  
---|---  
uniqueRenderPipelineAssets | A collection with the non null selected Render Pipeline Assets for the platform.  
allLevelsAreOverridden | An additional information that state if all quality settings were overridden in the project.  
  
### Description

[Editor Only] Obtains a set with the non null Render Pipeline Assets selected
on all the Quality Levels for the given platform.

    
    
    public T[] GetAllRenderPipelineAssets<T>([BuildTarget](BuildTarget.html) platform)
        where T : [RenderPipelineAsset](Rendering.RenderPipelineAsset.html)
    {
        var activeBuildTargetGroup = BuildPipeline.GetBuildTargetGroup(platform);
        var namedBuildTarget = [NamedBuildTarget.FromBuildTargetGroup](Build.NamedBuildTarget.FromBuildTargetGroup.html)(activeBuildTargetGroup);
        [QualitySettings.GetRenderPipelineAssetsForPlatform](QualitySettings.GetRenderPipelineAssetsForPlatform.html)<T>(namedBuildTarget.TargetName, out var uniqueAssets, out bool allLevelsAreOverridden);
        if(allLevelsAreOverridden)
            return uniqueAssets.ToArray();  
      
        return Array.Empty<T>();
    }

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

