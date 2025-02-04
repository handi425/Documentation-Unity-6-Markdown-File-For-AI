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

#  [LightProbes](LightProbes.html).GetInstantiatedLightProbesForScene

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

public static [LightProbes](LightProbes.html)
GetInstantiatedLightProbesForScene([SceneManagement.Scene](SceneManagement.Scene.html)
scene);

### Parameters

scene | The scene to get the shared light probe data for.  
---|---  
  
### Returns

**LightProbes** The cloned light probe data for the scene.

### Description

Gets an instantiated clone of the `LightProbes` object for a specific scene.

If you modify the `LightProbes` object returned by this method, you will only
affect the lighting of `scene`. Modifications will not affect assets.  
  
**Note** : This function automatically instantiates the `LightProbes` object
and makes it unique to the passed scene. You need to destroy the `LightProbes`
object when it's no longer needed. You can also use
[Resources.UnloadUnusedAssets](Resources.UnloadUnusedAssets.html) to destroy a
`LightProbes` object, which will be called automatically when you switch to a
new scene.  
  
Additional resources:
[LightProbes.GetSharedLightProbesForScene](LightProbes.GetSharedLightProbesForScene.html).

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

