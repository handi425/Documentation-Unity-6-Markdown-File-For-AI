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

# SceneManagerAPI

class in UnityEngine.SceneManagement

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Derive from this base class to provide alternative implementations to the C#
behavior of specific [SceneManager](SceneManagement.SceneManager.html)
methods.

The example provided logs if scene loading is done by index and logs a warning
to switch to loading by scene path.

    
    
    using UnityEngine;
    using [Debug](Debug.html) = UnityEngine.Debug;
    using UnityEngine.SceneManagement;  
      
    public class SceneIndexLogger : [SceneManagerAPI](SceneManagement.SceneManagerAPI.html)
    {
        [RuntimeInitializeOnLoadMethod]
        static void OnRuntimeMethodLoad()
        {
            [SceneManagerAPI.overrideAPI](SceneManagement.SceneManagerAPI-overrideAPI.html) = new SceneIndexLogger();
        }  
      
        protected override int GetNumScenesInBuildSettings()
        {
            [Debug.LogWarning](Debug.LogWarning.html)("SceneManager.GetNumScenesInBuildSettings() called, please load scenes by path to avoid issues when scenes are reordered.");
            return base.GetNumScenesInBuildSettings();
        }  
      
        protected override [Scene](SceneManagement.Scene.html) GetSceneByBuildIndex(int buildIndex)
        {
            [Debug.Log](Debug.Log.html)($"[SceneManager.GetSceneByBuildIndex](SceneManagement.SceneManager.GetSceneByBuildIndex.html)(buildIndex = {buildIndex}) called, please load scenes by path to avoid issues when scenes are reordered.");
            return base.GetSceneByBuildIndex(buildIndex);
        }
    }
    

### Static Properties

[overrideAPI](SceneManagement.SceneManagerAPI-overrideAPI.html)| The specific
SceneManagerAPI instance to use to handle overridden SceneManager methods.  
---|---  
  
### Protected Methods

[GetNumScenesInBuildSettings](SceneManagement.SceneManagerAPI.GetNumScenesInBuildSettings.html)|
Override for customizing the behavior of the
SceneManager.sceneCountInBuildSettings function.  
---|---  
[GetSceneByBuildIndex](SceneManagement.SceneManagerAPI.GetSceneByBuildIndex.html)|
Override for customizing the behavior of the SceneManager.GetSceneByBuildIndex
function.  
[LoadFirstScene](SceneManagement.SceneManagerAPI.LoadFirstScene.html)|
Override for customizing the behavior of loading the first Scene in a stub
player build.  
[LoadSceneAsyncByNameOrIndex](SceneManagement.SceneManagerAPI.LoadSceneAsyncByNameOrIndex.html)|
Override for customizing the behavior of the SceneManager.LoadScene and
SceneManager.LoadSceneAsync functions.  
[UnloadSceneAsyncByNameOrIndex](SceneManagement.SceneManagerAPI.UnloadSceneAsyncByNameOrIndex.html)|
Override for customizing the behavior of the SceneManager.UnloadSceneAsync
function.  
  
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

