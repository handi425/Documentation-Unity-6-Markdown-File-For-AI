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
[IProcessSceneWithReport](Build.IProcessSceneWithReport.html).OnProcessScene

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

public void OnProcessScene([SceneManagement.Scene](SceneManagement.Scene.html)
scene, [Build.Reporting.BuildReport](Build.Reporting.BuildReport.html)
report);

### Parameters

scene | The current Scene being processed.  
---|---  
report | A report containing information about the current build. When this callback is invoked for Scene loading during Editor playmode, this parameter will be null.  
  
### Description

Implement this function to receive a callback for each Scene during the build.

This callback is invoked during Player and AssetBundle builds, and also as a
scene is reloaded while entering Editor playmode.
[BuildPipeline.isBuildingPlayer](BuildPipeline-isBuildingPlayer.html) can be
used to determine in which context the callback is being called.  
  
Additional resources:
[BuildPipeline.BuildPlayer](BuildPipeline.BuildPlayer.html),
[BuildPipeline.BuildAssetBundles](BuildPipeline.BuildAssetBundles.html),
[BuildCallbackVersionAttribute](Build.BuildCallbackVersionAttribute.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Build;
    using UnityEditor.Build.Reporting;
    using UnityEngine;  
      
    [BuildCallbackVersion(1)]
    class MyCustomBuildProcessor : [IProcessSceneWithReport](Build.IProcessSceneWithReport.html)
    {
        public int callbackOrder { get { return 0; } }
        public void OnProcessScene(UnityEngine.SceneManagement.Scene scene, [BuildReport](Build.Reporting.BuildReport.html) report)
        {
            [Debug.Log](Debug.Log.html)("MyCustomBuildProcessor.OnProcessScene " + scene.name);
        }
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

